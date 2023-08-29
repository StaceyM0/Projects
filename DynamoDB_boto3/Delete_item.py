

import boto3

# create a DynamoDB client
dynamodb = boto3.client('dynamodb')

table = dynamodb.Table('Bucket_List') # get a reference to the table

# specify the key of the item to delete
key = {
    'Country': 'France', 'City': 'Provence'}
    
# delete the item
response = table.delete_item(
    Key=key)

# print the response
print(response)
print("Item deleted")
