import boto3

s3 = boto3.client('s3')

s3.put_object(
    Bucket='boto3-bucket-06sep2023', Key='test_string.txt', Body='This is a string, tesing uploading a new object' ,ContentType ='text/plain')

