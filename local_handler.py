import os
import boto3
import json
from dotenv import load_dotenv, dotenv_values 


# Create an SQS client
sqs = boto3.client('sqs')

def receive_messages():
    response = sqs.receive_message(
        QueueUrl=os.getenv("SQS_QUEUE_URL"),
        MaxNumberOfMessages=5,  # Adjust based on your needs
        WaitTimeSeconds=10  # Long polling for better efficiency
    )

    if 'Messages' in response:
        for message in response['Messages']:
            print("Received Message:")
            print(json.loads(message['Body']))

            # Delete the message after processing
            sqs.delete_message(
                QueueUrl=os.getenv("SQS_QUEUE_URL"),
                ReceiptHandle=message['ReceiptHandle']
            )
            print("Message deleted.\n")
    else:
        print("No messages in queue.")


load_dotenv() 
receive_messages()
