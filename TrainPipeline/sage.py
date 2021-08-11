import argparse

import sagemaker
import boto3

parser = argparse.ArgumentParser(
    description="Run a training job on Sagemaker."
)
parser.add_argument("--bucket", type=str)
parser.add_argument("--role", type=str)
args = parser.parse_args()

bucket = args.bucket
role = args.role

region = boto3.Session().region_name
sess = sagemaker.Session()
output_bucket = bucket
prefix = 'output'
container = sagemaker.image_uris.retrieve("xgboost", region, "latest")

s3_input_train = sagemaker.inputs.TrainingInput(
    s3_data="s3://{}/train".format(bucket), content_type="csv"
)
s3_input_validation = sagemaker.inputs.TrainingInput(
    s3_data="s3://{}/validation".format(bucket), content_type="csv"
)

sess = sagemaker.Session()

xgb = sagemaker.estimator.Estimator(
    container,
    role,
    instance_count=1,
    instance_type="ml.m4.xlarge",
    output_path="s3://{}/{}".format(bucket, prefix),
    sagemaker_session=sess,
)
xgb.set_hyperparameters(
    max_depth=5,
    eta=0.2,
    gamma=4,
    min_child_weight=6,
    subsample=0.8,
    silent=0,
    objective="binary:logistic",
    num_round=100,
)

xgb.fit({"train": s3_input_train, "validation": s3_input_validation}, wait=True)