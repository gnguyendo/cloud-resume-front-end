import boto3


def test_lambda(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='viewcount',
        KeySchema=[
            {
                'AttributeName': 'ViewerDate',
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'WebPageViews',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'ViewerDate',
                'AttributeType': 'S'
            }
        ]
    )
    # Wait until the table exists.
    table.wait_until_exists()

    # Print out some data about the table.
    print(table.item_count)

    message = "Hello Lambda World"
    return message


