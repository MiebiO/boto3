import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='boto3-bucket-DDMMYYYY'
    )

#Enter in a unique bucket name
print(response)
