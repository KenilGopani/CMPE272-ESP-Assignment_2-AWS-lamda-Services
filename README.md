
# CMPE272: Enterprise Software Platforms

#### Assignment 2: Building serverless application
#### Author: Kenil G Gopani
#### SJSU ID: 017992624
#### Guidance by: Prof. Rakesh Ranjan

## Tech Stack

**Backend:** AWS lamda

**Database:** DynamoDB

## Steps

### Setting Up the DynamoDB Table
1. Go to the AWS Management Console and navigate to DynamoDB.
2. Create a new table:
   - Table Name: StudentRecords
   - Primary Key: student_id (String)
3. After the table is created, note down the table name.
![App Screenshot](images/1.png)
![App Screenshot](images/2.png)

![App Screenshot](images/3.png)
![App Screenshot](images/4.png)
![App Screenshot](images/5.png)


### Creating an AWS Lambda Function
1. Navigate to AWS Lambda in the AWS Management Console.
2. Create a new Lambda function:
   - Function Name: StudentRecordHandler
   - Runtime: Choose Python 3.x or Node.js (depending on your preferred language).
   - Permissions: Attach the appropriate role to allow Lambda to read/write to DynamoDB.
3. Inside your Lambda function, write code to handle basic CRUD operations with DynamoDB.
   - Create: Insert a new student record into the DynamoDB table.
   - Read: Fetch a student record by student_id.
   - Update: Update a student's details.
   - Delete: Remove a student record.
![App Screenshot](images/6.png)
![App Screenshot](images/7.png)


### Python Example Code (for basic CRUD operations):
![App Screenshot](images/carbon.png)

### Creating an API Gateway
1. Go to API Gateway in the AWS Management Console.
2. Create a new REST API:
   - API Name: StudentAPI
3. Set up the following resources and methods:
   - POST /students: Trigger the Lambda function to add a new student.
   - GET /students: Trigger the Lambda function to retrieve student details by student_id.
4. Deploy the API and note down the Invoke URL.

### Testing the Application
1. Use Postman or curl to test the API by sending HTTP requests to the deployed API Gateway.
   - POST Request: https://n04iwlh2ma.execute-api.us-east-amazonaws.com/dev/StudentRecordHandler/students
   
![App Screenshot](images/8.png)
![App Screenshot](images/9.png)
![App Screenshot](images/10.png)
![App Screenshot](images/11.png)
![App Screenshot](images/12.png)
![App Screenshot](images/13.png)
![App Screenshot](images/14.png)
![App Screenshot](images/15.png)
