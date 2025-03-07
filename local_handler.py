import os
import boto3
import json
from dotenv import load_dotenv 

sqs = boto3.client('sqs')

def receive_messages():
    response = sqs.receive_message(
        QueueUrl=os.getenv("SQS_QUEUE_URL"),
        MaxNumberOfMessages=5,
        WaitTimeSeconds=10
    )

    if 'Messages' in response:
        for message in response['Messages']:
            print("Received Message:")
            print(json.loads(message['Body']))

            sqs.delete_message(
                QueueUrl=os.getenv("SQS_QUEUE_URL"),
                ReceiptHandle=message['ReceiptHandle']
            )
            print("Message deleted.\n")
    else:
        print("No messages in queue.")


load_dotenv() 
#receive_messages()
s3 = boto3.client('s3')
sqs = boto3.client('sqs')
s3.upload_file(FILE_PATH, BUCKET_NAME, S3_OBJECT_NAME)
s3_path = f"s3://{bucket_name}/{file_key}"

print(s3_path)