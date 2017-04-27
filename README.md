# boto3-wrapper
Prototype of boto3 for AWS EC2 handler.  

# Env  
Install boto3 and awscli with pip
    $pip install boto3
    $pip install awscli


# Set credentials
For instance like this.
    $ aws configure
    AWS Access Key ID [None]: AccessKey
    AWS Secret Access Key [None]: AccessKeySecret
    Default region name [None]: region
    Default output format [None]: json


# Usage  
Example of creating new EC2 instance.
    from Ec2ClientWrapper import Ec2ClientWrapper
    
    EC2 = Ec2ClientWrapper()
    created_instance = EC2.create("Your AMI id", "Your keypair name", "Your security group id")
