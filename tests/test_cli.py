import pytest

url = "postgres://bob@example.com:5431/db_one"


@pytest.fixture()
def parser():
    from pgbackup import cli
    return cli.create_parser()


# pgbackup postgres://bob@example.com:5431/db_one --driver s3 backups
def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parses will exit uf ut receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])


def test_parser_with_unknown_driver(parser):
    """
    Parser will exit if driver name is unknown
    """
    driver = 'unknown'
    destination = '/some/path'

    with pytest.raises(ValueError):
        parser.parse_args([url, '--driver', driver, destination])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver destination
    """
    driver = 'local'
    destination = '/some/path'
    args = parser.parse_args([url, '--driver', driver, destination])

    assert args.url == url
    assert args.driver == driver
    assert args.destination == destination
