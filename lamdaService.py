import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

# Custom JSON encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Convert Decimal to float or int
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    http_method = event.get('httpMethod', None)

    if http_method == 'POST':
        # Create a new student record
        student = json.loads(event['body'])
        table.put_item(Item=student)
        return {
            'statusCode': 200,
            'body': json.dumps('Student record added successfully')
        }

    elif http_method == 'GET':
        # Fetch student record by student_id
        student_id = event['queryStringParameters'].get('student_id')
        response = table.get_item(Key={'student_id': student_id})
        item = response.get('Item', 'Student not found')

        # Use custom JSON encoder for Decimal conversion
        return {
            'statusCode': 200,
            'body': json.dumps(item, cls=DecimalEncoder)
        }
        
    elif http_method == 'PUT':
        # Update an existing student record
        student = json.loads(event['body'])
        student_id = student.get('student_id')
    
        if not student_id:
            return {
                'statusCode': 400,
                'body': json.dumps('student_id is required for updating records')
            }
    
        # Update the record in DynamoDB
        response = table.update_item(
            Key={'student_id': student_id},  
            UpdateExpression="set #name=:n, age=:a",  
            ExpressionAttributeNames={
                '#name': 'name'  
            },
            ExpressionAttributeValues={
                ':n': student['name'], 
                ':a': Decimal(student['age'])  
            },
            ReturnValues="UPDATED_NEW"  
        )
    
        return {
            'statusCode': 200,
            'body': json.dumps('Student record updated successfully')
        }
        
    elif http_method == 'DELETE':
        # Delete a student record by student_id
        student_id = event['queryStringParameters'].get('student_id')
    
        if not student_id:
            return {
                'statusCode': 400,
                'body': json.dumps('student_id is required for deleting records')
            }
    
        response = table.delete_item(
            Key={'student_id': student_id},
            ConditionExpression="attribute_exists(student_id)" 
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f'Student record with student_id {student_id} deleted successfully')
        }

    else:
        return {
            'statusCode': 400,
            'body': json.dumps(http_method)
        }
