import boto3

# Set the region to launch the instance in
REGION = 'us-west-2'

# Set the AMI ID of the Amazon Linux 2 AMI
AMI_ID = 'ami-0a887e401f7654935'

# Set the instance type to launch
INSTANCE_TYPE = 't2.micro'

# Set the name of the key pair to use for the instance
KEY_NAME = 'my-key-pair'

# Set the ID of the security group to use for the instance
SECURITY_GROUP_ID = 'sg-0123456789abcdefg'

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

# Launch the instance
response = ec2.run_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    SecurityGroupIds=[SECURITY_GROUP_ID],
    MinCount=1,
    MaxCount=1
)

# Print the instance ID
print(f"Instance ID: {response['Instances'][0]['InstanceId']}")
