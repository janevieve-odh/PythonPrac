
# import boto3
# import json
# s3 = boto3.resource('s3')
# def lambda_handler(event, context):
#     bucket = s3.Bucket('test-bucket-3x1')
#     dest_bucket = s3.Bucket('test-bucket-3x2')
#     print(bucket)
#     print(dest_bucket)

#     for obj in bucket.objects():
#         dest_key = obj.key
#         print(dest_key)
#         # s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})

    
s3 = boto3.resource('s3')
#get the bucket name
def lambda_handler(event, context):

#get the file/key name
Key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

try:
    #fetch the file from s3
    response = s3.get_object(Bucket=bucket, Key=key)
    #deserialize the file content
    text = response["Body"].read().decode()

    #print the content
    print(data)

    #parse and print the transcation
    transcations = data['transactions']
    for record in transcations:
    print(record['transType'])
    return 'Success!'

except Exception as e:
    print (e)
    raise e

