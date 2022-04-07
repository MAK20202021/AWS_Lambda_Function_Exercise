import json
import hello_preprocess

def lambda_handler(event,context):
    hello_preprocess.preprocess(event["s3UriKey"])
    return {
        'statusCode': 200,
        'body':json.dumps('Hello from Lambda')
    }