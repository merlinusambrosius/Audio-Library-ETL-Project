import boto3
from botocore.exceptions import ClientError

#Inquire if a specific bucket exists, and create it if it does not exist. If the bucket exists, print a message to the user.


def bucket_exists(bucket_name):
    """Check if an S3 bucket exists

    :param bucket_name: Name of the bucket to check
    :return: True if bucket exists, else False
    """
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            return False
        else:
            raise e


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        s3_client = boto3.client('s3')

        create_params = {'Bucket': bucket_name}

        if region and region != 'us-west-2':
            create_params['CreateBucketConfiguration'] = {
                'LocationConstraint': region
            }

        #Create the bucket
        s3_client.create_bucket(**create_params)
        print(f"Bucket '{bucket_name}' created successfully.")
        return True
    except ClientError as e:
        print(f"Error creating bucket: {e}")
        return False

bucket_name = 'audio-catalog-bucket-2026'  # Change to your desired bucket name
region = 'us-east-2'


if bucket_exists(bucket_name):#check if bucket exists before creating it
    print(f"Bucket '{bucket_name}' already exists.")#print message if bucket exists
else:#otherwise, create the bucket
    create_bucket(bucket_name, region)
