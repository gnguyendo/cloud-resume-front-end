import boto3
import json
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
        ExpressionAttributeValues={":view": {"N": "1"}},
        ReturnValues="ALL_NEW"
    )
    d = {1: 'a', 2: 'b', 3: 'c'}
    json_object = json.dumps(response, indent=2)

    book_json = \
        {
           "book": [

              {
                 "id":"01",
                 "language": "Java",
                 "edition": "third",
                 "author": "Herbert Schildt"
              },

              {
                 "id":"07",
                 "language": "C++",
                 "edition": "second",
                 "author": "E.Balagurusamy"
              }
           ]
        }

    test_json = json.dumps(book_json, indent=2)
    return test_json
