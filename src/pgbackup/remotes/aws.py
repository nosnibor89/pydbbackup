import boto3
from pgbackup.storage import RemoteClient


class Remote(RemoteClient):
    def put_file(self, infile, bucket, name):
        """
            Put file in AWS s3
            params:
                infile: file object to be upload/put in S3
                bucket: Destination bucket
                name: file name
            """
        boto3.setup_default_session(profile_name='slsuser')
        client = boto3.client('s3')
        client.upload_fileobj(infile, bucket, name)
