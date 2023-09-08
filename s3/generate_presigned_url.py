import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'boto3-bucket-06sep2023','Key': 'test_string.txt'}, ExpiresIn= 300)

print(response)