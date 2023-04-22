import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Bucket_List')

# Write multiple items to the table in a batch
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'Country': 'U.S. Virgin Islands',
            'City': 'St. John'
            }
        )
    batch.put_item(
        Item={
            'Country': 'Spain',
            'City': 'Barcelona'
            }
        )
    batch.put_item(
        Item={
            'Country': 'Canada',
            'City': 'Banff National Park'
            }
        )
    batch.put_item(
        Item={
            'Country': 'Mexico',
            'City': 'Las Coloradas'
            }
        )
    batch.put_item(
        Item={
            'Country': 'Italy',
            'City': 'Amalfi Coast'
            }
        )
    batch.put_item(
        Item={
            'Country': 'Ecuador',
            'City': 'Pailón Del Diable'
            }
        )
    batch.put_item(
        Item={
            'Country': 'France',
            'City': 'Provence'
            }
        )
    batch.put_item(
        Item={
            'Country': 'Turkey',
            'City': 'Cappadocia'
            }
        )
    batch.put_item(
        Item={
            'Country': 'South Africa',
            'City': 'Cape Town'
            }
        )
       
    print("Items added") # this will be returned once the code is successful
    
    heck yes
