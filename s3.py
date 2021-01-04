import boto3

ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
     ImageId='ami-04d29b6f966df1537',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='barbie_key',
     TagSpecifications=[
        {
          'ResourceType': 'instance',
          'Tags': [
            {
              'Key': 'Name',
              'Value': 'mama'
            },
            {
              'Key': 'owner',
              'Value': 'me'
            },
          ]
        },
      ],
 )

BUCKET_NAME = 'argwack'
BUCKET_FILE_NAME = 'aws-Lambda-exercise (1).rtf'
LOCAL_FILE_NAME = 'lambda_file4.txt'


def download_s3_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)


download_s3_file()


s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'argwack',  # Source Bucket
    'Key': 'aws-Lambda-exercise (1).rtf'  # file in source bucket to copy
}
bucket = s3.Bucket('boto3demo-bucket')  # Destination Bucket

obj = bucket.Object('copyText.txt')
obj.copy(copy_source)
