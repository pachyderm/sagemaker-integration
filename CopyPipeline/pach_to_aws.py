import argparse

import boto3
from botocore.client import Config

parser = argparse.ArgumentParser(
    description="Copy data from Pachyderm to AWS S3."
)
parser.add_argument("--target_bucket", type=str)
args = parser.parse_args()

target_bucket = args.target_bucket

print("Passing data on to AWS S3")
aws_s3_client = boto3.client('s3')
aws_s3_client.upload_file('/pfs/churn_dataset/train.csv', target_bucket, 'train.csv')
aws_s3_client.upload_file('/pfs/churn_dataset/validation.csv', target_bucket, 'validation.csv')

print("AWS S3 bucket '{}' content:".format(target_bucket))
for key in aws_s3_client.list_objects(Bucket=target_bucket)['Contents']:
    print(key['Key'])