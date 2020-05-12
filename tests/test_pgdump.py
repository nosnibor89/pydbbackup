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


def test_dump_file_name_without_timestamp():
    """
    pg_dump.dump_file_name returns the file name without timestamp
    """
    file_name = pgdump.dump_file_name(url)
    assert file_name == 'db_one.sql'


def test_dump_file_name_with_timestamp():
    """
    pg_dump.dump_file_name returns the file name with timestamp
    """
    import time
    now = time.localtime()
    file_name = pgdump.dump_file_name(url, now)
    assert file_name == f'db_one-{now}.sql'
