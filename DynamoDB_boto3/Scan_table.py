import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Bucket_List')

# retrieves all items in the table and returns a dictionary of those items
response = table.scan() 

items = response['Items'] # stores in a variable called items

# iterates over the items list using a 'for' loop
for item in items:
    print(item)
    
print("Table scan complete")
