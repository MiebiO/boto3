# Import the boto3 library, which allows interaction with AWS services.
import boto3

# Create an S3 client object using boto3.
s3 = boto3.client('s3')

# Use the S3 client to send a request to list all S3 buckets in the AWS account.
response = s3.list_buckets()

# Access the 'Buckets' key in the response dictionary to retrieve a list of S3 bucket metadata.
buckets = response['Buckets']

# Print a header indicating the start of the list of existing buckets.
print('The existing buckets are:')

# Iterate through the list of buckets and print each bucket's name and creation date.
for bucket in buckets:
    print(bucket['Name'], ', Creation Date:', bucket['CreationDate'])

#Response is a dictionary
#buckets is a list which has dictionaries inside it
#bucket in buckets refers to each dictionary inside the list
#bucket['Name'] gets the value assigned to the key, Name in each dictionary