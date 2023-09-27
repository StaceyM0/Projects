


import boto3 # Import boto3 library to interact with AWS services
import json # Import the json module to work with JSON data
import datetime # Import datetime module to get current timestamp

sqs = boto3.client('sqs') # Create an SQS client
queue_url = 'YOUR_QUEUE_URL' # Replace with your own queue URL

def lambda_handler(event, context):
    timestamp = str(datetime.datetime.now()) # Get the current timestamp and convert to string
    response = sqs.send_message( # Send a message to the SQS queue
        QueueUrl=queue_url, # Specify the queue URL
        MessageBody=timestamp # Set the message body to the timestamp
    )
    
    return {
        'statusCode': 200, # Return a 200 status code to indicate success
        'body': json.dumps('Message sent to SQS queue at ' + timestamp) # Return a message indicating success
    }

