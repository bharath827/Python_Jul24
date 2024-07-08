import json

import boto3

client = boto3.client('s3')
response = client.get_bucket_acl(
    Bucket='buck1.123',
)
j = json.dumps(response)
print(response)
print(j)