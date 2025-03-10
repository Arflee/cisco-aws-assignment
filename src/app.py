import os
import json
import boto3
import logging
from network_analyzer import kruskal_mst

logger = logging.getLogger()

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    s3_path = f"s3://{bucket_name}/{file_key}"
    
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')
    lines = file_content.strip().split('\n')
    num_nodes = int(lines[0])

    if num_nodes != len(lines) - 1:
        logger.setLevel(logging.ERROR)
        logger.error("Node amount is not the same as the actual number of nodes. Expected " + str(num_nodes) + " but got " + str(len(lines) - 1))
        return {"s3_file_path": s3_path}
    
    for line in lines[1:]:
        if len(line.split()) != 3:
            logger.setLevel(logging.ERROR)
            logger.error("Node syntax is different. The syntax have to be {node1} {node2} {cost}. But got " + line)
            return {"s3_file_path": s3_path}

    edges = [tuple(map(int, line.split())) for line in lines[1:]]

    total_cost, mst = kruskal_mst(edges, num_nodes)
    output_data = {
        "total_cost": total_cost,
        "connections": mst,
        "s3_file_path": s3_path
    }
    
    sqs = boto3.client('sqs')
    sqs_queue_url = os.getenv("SQSURL")
    sqs.send_message(QueueUrl=sqs_queue_url, MessageBody=json.dumps(output_data))

    return output_data
