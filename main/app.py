# from __future__ import print_function

import boto3
import json


def test_lambda(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='viewcount',
        KeySchema=[
            {
                'AttributeName': 'WebPageViews',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'WebPageViews',
                'AttributeType': 'N'
            }
        ]
    )

    # Wait until the table exists.
    table.wait_until_exists()

    # Print out some data about the table.
    print(table.item_count)
