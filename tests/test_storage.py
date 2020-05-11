import pytest
import tempfile
from pgbackup.storage import local, remote
from pgbackup.remotes import aws


@pytest.fixture
def source_file():
    f = tempfile.TemporaryFile()
    f.write(b'Testing')
    f.seek(0)
    return f


def test_storing_file_locally(source_file):
    """
    Writes content from one file to another
    """
    dest_file = tempfile.NamedTemporaryFile(delete=False)

    local(source_file, dest_file)

    with open(dest_file.name, 'rb') as f:
        content = f.read()
        assert content == b'Testing'


def test_storing_file_in_s3(mocker, source_file):
    """
    Writes content from one file to s3
    """
    client = aws.Remote()
    client.put_file = mocker.MagicMock()
    bucket_name = 'my-bucket'
    file_name = 'file1.txt'
    remote(client, source_file, bucket_name, file_name)
    client.put_file.called_with(source_file, bucket_name, file_name)
