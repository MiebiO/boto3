import boto3

s3 = boto3.client('s3')

with open('test_text.txt','rb') as f:
    s3.put_object(
        Bucket='boto3-bucket-06sep2023', Key='test_text.txt', ContentType ='text/plain')

