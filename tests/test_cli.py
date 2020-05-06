import pytest

from pgbackup import cli

url = "postgres://bob@example.com:5431/db_one"


# pgbackup postgres://bob@example.com:5431/db_one --driver s3 backups
def test_parser_without_driver():
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])


def test_parser_with_driver():
    """
    The parses will exit uf ut receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url, "--driver", "local"])


def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives a driver destination
    """
    driver = 'local'
    destination = '/some/path'
    parser = cli.create_parser()
    args = parser.parse_args([url, '--driver', driver, destination])

    assert args.driver == driver
    assert args.destination == destination
