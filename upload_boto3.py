import boto3
from botocore.exceptions import NoCredentialsError, ClientError

try:
    # Boto3 code that may raise exceptions
    s3 = boto3.client('s3')
    s3.upload_file('/Users/stesh/Downloads/puppy-picture.jpg', 'my-first-boto3-test-bucket-ste', 'pictures/puppy-picture.jpg')   

except NoCredentialsError:
    print("AWS credentials not found. Please configure your credentials.")

except ClientError as e:
    if e.response['Error']['Code'] == 'NoSuchBucket':
        print("The specified bucket does not exist.")
    else:
        print("An error occurred:", e)