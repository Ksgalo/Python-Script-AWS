Python Script AWS
This repository contains Python scripts that perform various tasks on Amazon Web Services (AWS). The scripts use the AWS SDK for Python (Boto3) to interact with AWS services.

Prerequisites
To run the scripts in this repository, you must have the following:

Python 3.6 or higher installed on your machine
Boto3 library installed in your Python environment
AWS credentials configured on your machine with appropriate permissions to perform the tasks in the scripts
Usage
To use the scripts in this repository, follow these steps:

Clone the repository to your local machine.
Install the required dependencies by running the following command in the terminal: pip install -r requirements.txt
Set your AWS credentials by either configuring them in the ~/.aws/credentials file or by setting environment variables.
Navigate to the directory containing the script you want to run.
Run the script using the following command: python <script_name>.py
Scripts
Here's a brief overview of the scripts available in this repository:

create_ec2_instance.py: Creates a new EC2 instance in the specified region.
create_s3_bucket.py: Creates a new S3 bucket with the specified name.
delete_ec2_instance.py: Deletes an EC2 instance with the specified instance ID.
delete_s3_bucket.py: Deletes an S3 bucket with the specified name.
list_ec2_instances.py: Lists all EC2 instances in the specified region.
list_s3_buckets.py: Lists all S3 buckets in your AWS account.
Contributing
If you'd like to contribute to this repository, please fork the repository and create a pull request with your changes.

License
This repository is licensed under the MIT License. See the LICENSE file for more information.
