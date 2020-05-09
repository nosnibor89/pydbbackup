from argparse import ArgumentParser, Action

allowed_drives = ['local', 's3']


class DriverAction(Action):
    def __call__(self, parses, namespace, values, option_string=None):
        driver, destination = values

        if driver.lower() not in allowed_drives:
            raise ValueError('Incorrect values for --driver')

        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(
        description="""
        Backup postgres sql database locally or to AWS S3
        """
    )

    parser.add_argument('url', help="URL of the database to backup")

    parser.add_argument(
        '--driver', '-d',
        help="how and where to store the backup",
        nargs=2,
        metavar=('DRIVER', 'DESTINATION'),
        action=DriverAction,
        required=True
    )

    return parser


def main():
    import time
    from pgbackup import pgdump, storage
    from pgbackup.remotes import aws

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)

    if args.driver == 's3':
        now = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp=now)
        s3_client = aws.Remote()
        print(f'Backing database up to AWS S3 as {file_name}...')
        storage.remote(s3_client, dump.stdout, args.destination, file_name)

    else:
        local_file = open(args.destination, 'wb')
        print('Backing database up to local directory')
        storage.local(dump.stdout, local_file)

    print('Done!')
