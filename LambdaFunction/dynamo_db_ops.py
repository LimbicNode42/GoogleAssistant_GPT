import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GPTConversations')

def create_conversation(conversation_id, conversation):
    table.put_item(
        Item={
            'gptc_pk': conversation_id,
            'conversation': conversation
        }
    )
    
def update_conversation(conversation_id, conversation):
    table.update_item(
        Key={'gptc_pk': conversation_id},
        UpdateExpression="SET conversation = list_append(conversation, :new_message)",
        ExpressionAttributeValues={
            ':new_message': [conversation],
        },
    )
    
def get_conversation(conversation_id):
    response = table.get_item(
        Key={'gptc_pk': conversation_id}
    )
    if 'Item' in response:
        item = response['Item']
        return item
    else:
        return None