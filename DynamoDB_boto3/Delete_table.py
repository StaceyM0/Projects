import boto3 # imports the boto3 library

# create a DynamoDB resource object which will interact with the DynamoDB service
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table_name = 'Bucket_List' # Adding a variable to table_name

table = dynamodb.Table('Bucket_List') # Makes a reference to the DynamoDB table

table.delete() # deletes the table

print('Table deleted:', 'Bucket_List') # The name of the deleted table will show

