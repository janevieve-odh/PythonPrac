import boto3
region = 'us-east-1'
instances = ['i-080e6744d401c337f']
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))


# region = 'us-west-1'
# instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']
# ec2 = boto3.client('ec2', region_name=region)


# def lambda_handler(event, context):
#     ec2.start_instances(InstanceIds=instances)
#     print('started your instances: ' + str(instances))
