import boto3

s3 = boto3.client('s3')

bucket = 'boto3-bucket-06sep2023'
key = 'test_string.txt'

s3.download_file(bucket, key, key)