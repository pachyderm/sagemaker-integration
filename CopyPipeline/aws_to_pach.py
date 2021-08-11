import argparse
import os

import boto3
from botocore.client import Config

parser = argparse.ArgumentParser(
    description="Copy data from AWS S3 to Pachyderm."
)
parser.add_argument("--src_bucket", type=str)
args = parser.parse_args()

src_bucket = args.src_bucket

base_path = "/pfs/out/"

s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(src_bucket) 
for obj in bucket.objects.filter(Prefix = 'output/'):
    if not os.path.exists(os.path.dirname(base_path + obj.key)):
        os.makedirs(os.path.dirname(base_path +  obj.key))
    print("Downloading {}".format(obj.key))
    bucket.download_file(obj.key, base_path + obj.key)