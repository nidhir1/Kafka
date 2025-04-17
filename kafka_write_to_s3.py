import boto3
from datetime import datetime



bucket = "your bucket name"



aws_access_key_id = "your access key"
aws_secret_access_key = "your secret key"
region_name = "your region name"




s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)


def write_to_s3(data):
    key = f'messages/{datetime.now().isoformat()}.txt'
    s3.put_object(Bucket=bucket, Key=key, Body=data)

