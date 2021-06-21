import json
import boto3


table = "OrganizationTags"

def lambda_handler(event, context):
    # TODO implement
    print(event)
    account_id = event['detail']['serviceEventDetails']['createManagedAccountStatus']['account']['accountId']
    customer_name=event['detail']['serviceEventDetails']['createManagedAccountStatus']['account']['accountName']
    tag_dic= get_tags(customer_name)
    put=put_tags(account_id,tag_dic)
    print (put)
    return {
        'statusCode': 200,
        'body': json.dumps('Successful Execution')
    }

def get_tags (account_name):
    client = boto3.client('dynamodb')
    response = client.get_item(
        TableName=table,
        Key={
            'AccountName':{
                'S': account_name,
            }
        }        
        )
    return response["Item"]

def put_tags (account_number,tags):
    client = boto3.client('organizations')
    response = client.tag_resource(
        ResourceId=account_number,
        Tags=[
            {
                'Key':'CustomerName',
                'Value':tags['Tag1']['S']
            },
            {
                'Key':'TaxID',
                'Value':tags['Tag2']['N'] 
            },
            {
                'Key':'CustomerCode',
                'Value':tags['Tag3']['N'] 
            },
            {
                'Key':'ServiceID',
                'Value':tags['Tag4']['S'] 
            }
            ]
        )
    return ('true')
