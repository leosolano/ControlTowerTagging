# Tagging AWS account using Control Tower Life Cycle events

In the following tutorial you will learn how to use AWS Control Tower life cycle events to trigger a tagging process to your accounts, which will help you to create interesting query to billing system from Athena and allow you to identify expends in AWS services in a Multi-Account environment. The set of services using for this development are Lambda, Control Tower, dynamoDB, AWS Organization and Control Trail. Doing a clean integration between those services any organization could simplify the tagging process during the account creation from Control Tower Account Factory.

## Step 1. Create a DynamoDB Table for tagging

First than all we need to cerate a DynamoDB table with the right structure to be consume it later from a lmabda functions to get the required tags for your accounts. Juts keep in mind that the Partition Key must be a value that need to match with the account name you use during the Account factory process in Control Tower in roder to have an "index"  which could be querie from Lambda. In our example we used AccountName as Partition key.

![DynamoDB1](https://github.com/leosolano/ControlTowerTagging/blob/main/images/CreateTable.png)

![DynamoDB2](https://github.com/leosolano/ControlTowerTagging/blob/main/images/CreateItem.png)

## Step 2. Create the Lambda function

Second step is the creation of the lambda function which will be usen then by event bridge to trigger the tagging process. As you can see in the code folder this is a simple python code using boto3 library to use the DynamoDB and AWS Organizations SDK in order to get tags from DynamoDB Table and putt tags to AWs Acconts created in AWS Organizations. The Partition key to get tags is the Account Name that is captiurable from the event in the field ['detail']['serviceEventDetails']['createManagedAccountStatus']['account']['accountName'].- In the other hand the account id is required to send tags toward the right account, this is why the lambda function is capturing this field from the event ['detail']['serviceEventDetails']['createManagedAccountStatus']['account']['accountId']



