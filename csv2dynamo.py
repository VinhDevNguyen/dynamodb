import boto3

dynamodb = boto3.resource('dynamodb', 
                           endpoint_url="http://localhost:4566/",
                           region_name='dummy',
                           aws_access_key_id='dummy',
                           aws_secret_access_key='dummy')

table = dynamodb.Table('count')

def lambda_handler(event, context):
    with open('./tmp/count.csv', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                table.put_item(Item={"id": line, "count": 1})
    return 'OK'