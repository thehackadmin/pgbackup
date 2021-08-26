import pytest
from os import getenv
from pgbackup import cli

dbuser = getenv('dbuser')
dbpwd = getenv('dbpwd')
dbsrv = '172.31.19.169:80'
dbinst = 'sample'
dburl = "postgres://" + dbuser + ":" + dbpwd + "@" + dbsrv + "/" + dbinst
# Goals:
# $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
# $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

#pknown_driversrint(known_drivers)


@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    If driver is not spesified, will exit:
    """

    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([dburl])

def test_parser_with_parser(parser):
    """
    If destination is absent, will exit:
    """

    with pytest.raises(SystemExit):
        parser.parse_args([dburl, "--driver", "local"])

def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown.
    """

    with pytest.raises(SystemExit):
        parser.parse_args([dburl, '--driver', 'foo', 'destination'])

def test_parser_with_known_driver(parser):
    """
    The parser will continue with known driver name input.
    """

    for driver in ['local', 's3']:
        assert parser.parse_args([dburl, '--driver', driver, 'destination'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and destination
    """

    args = parser.parse_args([dburl, '--driver', 'local', '/some/path'])

    assert args.driver == 'local'
    assert args.destination == '/some/path'
    assert args.url == dburl

