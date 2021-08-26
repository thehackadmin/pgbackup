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
    parser.add_argument('url', help='URL of the PostgreSQL DB to be backed up')
    parser.add_argument('--driver',
            help='How and where to store backups of the DB',
            nargs=2,
            action=DriverAction,
            required=True,
            )
    return parser




