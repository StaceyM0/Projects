import boto3

# this allows to use Key to define the key condition expression for the query
from boto3.dynamodb.conditions import Key

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Bucket_List')

## Query the table for items where the 'Country' attribute is 'Mexico'
response = table.query(
    KeyConditionExpression=Key('Country').eq('Mexico')
)

print(response['Items']) # prints the query results
