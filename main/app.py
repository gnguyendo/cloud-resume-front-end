import boto3
import json
import os
from datetime import date

client = boto3.client("dynamodb")
web_page_counter = os.environ.get('DataBaseName')
curr_date = date.today().strftime("%m/%d/%y")


def test_lambda(event, context):
    response_body = client.update_item(
        TableName=web_page_counter,
        Key={"Date": {"S": curr_date}},
        UpdateExpression="ADD total_views :view",
        ExpressionAttributeValues={":view": {"N": "1"}},
        ReturnValues="ALL_NEW"
    )
    d = {1: 'a', 2: 'b', 3: 'c'}
    # json_object = json.dumps(response, indent=2)

    response = \
        {
            "isBase64Encoded": True,
            "statusCode": 200,
            # "headers": {"headerName": "headerValue"},
            # "multiValueHeaders": {},
            "body": json.dumps(response_body, indent=2)
        }

    return response
