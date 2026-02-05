import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CoffeeInventory')

def lambda_handler(event, context):
    method = event.get('httpMethod')

    if method == 'GET':
        response = table.scan()
        return {
            "statusCode": 200,
            "body": json.dumps(response['Items'])
        }

    if method == 'POST':
        body = json.loads(event['body'])
        item = {
            "itemId": str(uuid.uuid4()),
            "name": body['name'],
            "quantity": body['quantity']
        }
        table.put_item(Item=item)
        return {
            "statusCode": 201,
            "body": json.dumps(item)
        }

    return {
        "statusCode": 400,
        "body": "Unsupported method"
    }
