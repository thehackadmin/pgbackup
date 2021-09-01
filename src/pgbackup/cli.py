from argparse import ArgumentParser, Action
known_drivers = ['local', 's3']


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver.  Available drivers are:  " + str(known_drivers))
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description='This script will back up a PostgresSQL DB from a URL, to either #1 local storeage; or #2 a s3 bucket')
    parser.add_argument('url', help='URL of the PostgreSQL DB to be backed up.  example:  postgres://dbuser:dbpwd@dbip:80/sample')
    parser.add_argument('--driver', '-d',
            help='How and where to store backups of the DB',
            nargs=2,
            action=DriverAction,
            metavar=('driver', 'destination'),
            required=True,
            )
    return parser

def main():
    import boto3
    from pgbackup import pgdump, storage
    import time

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver =='s3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H-%M-%S", time.localtime())
        filename = pgdump.dump_filename(args.url, timestamp)
        print(f"Backing the db up to {args.destination} in s3 as {filename}")
        storage.s3(client, dump.stdout, args.destination, filename)
    else:
        outfile = open(args.destination, 'wb')
        print(f"Backing the db up locally to {args.destination}")
        storage.local(dump.stdout, outfile)



