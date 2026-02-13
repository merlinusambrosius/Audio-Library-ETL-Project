import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

s3 = boto3.client('s3', region_name='us-west-2')
bucket = 'audio-catalog-bucket-2026'  
folder = 'Catalog'
folders = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder, item))]
print(folders)

for folder in folders:
    files = [item for item in os.listdir(os.path.join('Catalog', folder)) if os.path.isfile(os.path.join('Catalog', folder, item))]
    print(files)    
    for file in files:
        local_path = os.path.join('Catalog', folder, file)
        s3_key = os.path.join(folder, file).replace('\\', '/')
        upload_file(local_path, bucket, s3_key)

