import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='boto3-bucket-06sep2023'
    )
    
print(response)
