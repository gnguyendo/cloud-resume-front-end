import boto3
import os
from datetime import date

client = boto3.client("dynamodb")
web_page_counter = os.environ.get('DataBaseName')
curr_date = date.today().strftime("%m/%d/%y")


def test_lambda(event, context):
    response = client.update_item(
        TableName=web_page_counter,
        Key={"Date": {"S": curr_date}},
        UpdateExpression="ADD total_views :view",
        ExpressionAttributeValues="{':view' : {'N': 1}",
        ReturnValues='ALL_NEW'
    )

    message = "Hello Lambda World"
    return message
