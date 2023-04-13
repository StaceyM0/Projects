import boto3 # This imports the boto3 library

dynamodb = boto3.client('dynamodb', region_name='us-east-1') # 


response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Country', # # defines a new attribute named 'Country'
            'AttributeType': 'S', # the data type of the attribute is string
        },
        {
            'AttributeName': 'City',
            'AttributeType': 'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'Country', # this will be partition key
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'City', # this will be sort key
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='Bucket_List', # sets the name of the table
)

print(response)
print("Table created")