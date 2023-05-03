import boto3

# Set the name of the bucket to create
BUCKET_NAME = 'my-unique-bucket-name'

# Set the region to create the bucket in
REGION = 'us-west-2'

# Create an S3 client
s3 = boto3.client('s3', region_name=REGION)

# Create the bucket
response = s3.create_bucket(
    Bucket=BUCKET_NAME,
    CreateBucketConfiguration={
        'LocationConstraint': REGION
    }
)

# Print the bucket ARN
print(f"Bucket ARN: {response['Location']}")
