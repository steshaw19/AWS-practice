import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-first-boto3-test-bucket-ste', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})