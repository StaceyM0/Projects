

import boto3

sqs = boto3.client('sqs')

queue = sqs.create_queue(
    QueueName='SQS_lambda_project'
)

print('Queue created')
print(queue)
