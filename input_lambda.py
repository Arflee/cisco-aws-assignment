import json
import boto3

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

def kruskal_mst(edges, num_nodes):
    edges.sort(key=lambda x: x[2])  # Sort edges by cost
    parent = {i: i for i in range(1, num_nodes + 1)}
    rank = {i: 0 for i in range(1, num_nodes + 1)}
    
    mst = []
    total_cost = 0
    
    for node1, node2, cost in edges:
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            mst.append({"from": node1, "to": node2, "cost": cost})
            total_cost += cost
    
    return total_cost, mst

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sqs = boto3.client('sqs')
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    s3_path = f"s3://{bucket_name}/{file_key}"
    
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')
    lines = file_content.strip().split('\n')
    
    num_nodes = int(lines[0])
    edges = [tuple(map(int, line.split())) for line in lines[1:]]
    
    total_cost, mst = kruskal_mst(edges, num_nodes)
    
    output_data = {
        "total_cost": total_cost,
        "connections": mst,
        "s3_file_path": s3_path
    }
    
    sqs_queue_url = "https://sqs.YOUR_REGION.amazonaws.com/YOUR_ACCOUNT_ID/output-queue"
    sqs.send_message(QueueUrl=sqs_queue_url, MessageBody=json.dumps(output_data))
    
    return {
        'statusCode': 200,
        'body': json.dumps("Processing Complete.")
    }
