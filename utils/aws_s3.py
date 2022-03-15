import boto3
import os
from utils.common import read_config
from from_root import from_root


class s3_bucket:

    def __init__(self):
        self.config = read_config(os.path.join(from_root(), 'config.yaml'))
        self.client = boto3.resource('s3')

    def create_bucket(self):
        pass

    def list_buckets(self):
        try:
            if self.client.Bucket(self.config['s3_bucket_params']['name_of_bucket']) in self.client.buckets.all():
                return True
            else:
                return False
        except Exception as e:
            return f"Error Occurred While Listing Buckets {e.__str__()}"

    def delete_bucket(self):
        pass
