import boto3
import sys

def create_ec2_instance(instance_type):
    ec2 = boto3.resource('ec2', region_name='us-east-2')  # change if needed

    instance = ec2.create_instances(
        ImageId='ami-0cfde0ea8edd312d4',  # Amazon Linux 2 AMI (for us-east-1)
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName='kbalakey',  # Must already exist
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'GitHub-Actions-EC2'}]
            }
        ]
    )

    print("✅ Launched EC2 Instance ID:", instance[0].id)

if __name__ == "__main__":
    instance_type = sys.argv[1] if len(sys.argv) > 1 else "t2.micro"
    create_ec2_instance(instance_type)
