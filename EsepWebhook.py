import os
import json
import requests

def lambda_handler(event, context):
    
    issue_url = event['issue']['html_url']
    
    SLACK_URL = os.environ['SLACK_URL']
    payload = {
        'text': f'Issue Created:  {issue_url}'
    }
    
    response = requests.post(SLACK_URL, json=payload)
    response.raise_for_status()
    
    output = {'output': issue_url}
    return{
        'statusCode': 200,
        'body': json.dumps(output)
    }
