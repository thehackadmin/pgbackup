import pytest
import subprocess
from os import getenv

from pgbackup import pgdump

dbuser = 'dbuser'
dbpwd = 'dbpwd'
dbsrv = '172.31.19.169:80'
dbinst = 'sample'
dburl = "postgres://" + dbuser + ":" + dbpwd + "@" + dbsrv + "/" + dbinst

def test_dump_calls_pgdump(mocker):
    """
    Utilize pgdump with the DB URL
    """

    mocker.patch('subprocess.Popen')
    assert pgdump.dump(dburl)
    subprocess.Popen.assert_called_with(['pg_dump', dburl], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error is pg_dump is not installed.
    """

    mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(dburl)

def test_dump_filename_without_timestamp():
    """
    returns the name of the DB
    """
    assert pgdump.dump_filename(dburl) == f"{dbinst}.sql"

def test_dump_filename_with_timestamp():
    """
    returns the name of the DB with a timestamp
    """
    timestamp = '2017-12-03T13-14-10'
    assert pgdump.dump_filename(dburl, timestamp) == f"{dbinst}-{timestamp}.sql"

