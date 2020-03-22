class RemoteClient:
    def put_file(self, infile, bucket, name):
        """
        Override this method with you own implementation with the cloud provided SDK to store the file in destination
        params:
            infile: file object to be upload/put in the provided cloud storage service (AWS S3, soon more comming)
            bucket: Destination bucket
            name: file name to be set in the cloud
        """
        pass


def local(infile, outfile):
    outfile.write(infile.read())

    outfile.close()
    infile.close()


def remote(client, infile, bucket, name):
    """
    Stores the dumped file into a cloud provider service (AWS S3, soon more comming)
    params:
        client: Must be an object that overrides RemoteClient class('put_file' method)
        infile: file object to be upload/put in the provided cloud storage service (AWS S3, soon more comming)
        bucket: Destination bucket
        name: file name to be set in the cloud
    """
    if not isinstance(client, RemoteClient):
        raise TypeError(
            'client must extends RemoteClient and overide put_file method')

    client.put_file(infile, bucket, name)
