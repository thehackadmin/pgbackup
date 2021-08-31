import pytest
import subprocess
from os import getenv
import tempfile

from pgbackup import storage

@pytest.fixture
def infile():
    f = tempfile.TemporaryFile()
    f.write(b'Testing')
    f.seek(0)
    return f

def test_storing_file_locally(infile):
    """
    Writes content from on file-like to another
    """

    outfile = tempfile.NamedTemporaryFile(delete=False)

    storage.local(infile, outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing'

def test_storing_file_s3(mocker, infile):
    """
    Writes content from on file-like to aws s3
    """
    client = mocker.Mock()
    storage.s3(client, infile, 'bucket_name', 'file_name')
    client.upload_fileobj.assert_called_with(infile, 'bucket_name', 'file_name')


