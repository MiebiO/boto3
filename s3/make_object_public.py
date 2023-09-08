import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define the S3 bucket and object key
bucket = 'boto3-bucket-06sep2023'
key = 'test_string.txt'

# Set public access block configuration for the bucket
response = s3.put_public_access_block(
    Bucket=bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,        # Block public ACLs
        'IgnorePublicAcls': False,       # Do not ignore public ACLs
        'BlockPublicPolicy': False,      # Block public bucket policies
        'RestrictPublicBuckets': False   # Do not restrict public buckets
    }
)

# Set bucket ownership controls
response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)

# Set the bucket ACL to private
response = s3.put_bucket_acl(
    ACL='private',    # Set the bucket ACL to private
    Bucket=bucket,
)

# Set the object ACL to public-read
response = s3.put_object_acl(
    ACL='public-read',  # Set the object ACL to public-read
    Bucket=bucket,
    Key=key
)

# Print the final response
print(response)
