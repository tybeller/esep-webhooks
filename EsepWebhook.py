import os
import json
import boto3
import urllib.request

def lambda_handler(event, context):
    json_data = json.loads(event['body'])
    slack_url = os.environ['SLACK_URL']
    issue_url = json_data['issue']['html_url']
    message = {"text": f"Issue Created: {issue_url}"}
    data = json.dumps(message).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(slack_url, data=data, headers=headers)
    response = urllib.request.urlopen(req)
    return {
        'statusCode': 200,
        'body': response.read().decode('utf-8')
    }
