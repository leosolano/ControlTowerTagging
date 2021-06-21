# Tagging AWS account using Control Tower Life Cycle events

In the following tutorial you will learn how to use AWS Control Tower life cycle events to trigger a tagging process to your accounts, which will help you to create interesting query to billing system from Athena and allow you to identify expends in AWS services in a Multi-Account environment. The set of services using for this development are Lambda, Control Tower, dynamoDB, AWS Organization and Control Trail. Doing a clean integration between those services any organization could simplify the tagging process during the account creation from Control Tower Account Factory.

# Step 1. Create a DynamoDB Table for tagging

First than all we need to cerate a DynamoDB table with the right structure to be consume it later from a lmabda functions to get the required tags for your accounts. Juts keep in mind that the Partition Key must be a value that need to match with the account name you use during the Account factory process in Control Tower in roder to have an "index"  which could be querie from Lambda. 


