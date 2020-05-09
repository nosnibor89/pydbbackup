import pytest
import subprocess
from pgbackup import pgdump

url = 'postgres://bob@example.com:5432/db_one'


def test_dump_calls_pgdump(mocker):
    """
    Utilize pg_dump with database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['/usr/bin/pg_dump', url], stdout=subprocess.PIPE)


def test_handle_os_errors(mocker):
    """
    pg_dump.dump returns a reasonable error if pg_dump is not installed
    """
    mocker.patch('subprocess.Popen', side_effect=FileNotFoundError('no such file'))

    with pytest.raises(SystemExit):
        assert pgdump.dump(url)
