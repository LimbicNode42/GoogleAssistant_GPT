from open_ai_keys import *
from dynamo_db_ops import *
import openai
import json

def get_gpt_response(query, session):
    org_key = get_org_key()
    api_key = get_api_key()
    openai.organisation = org_key
    openai.api_key = api_key

    # Initialise session if it doesn't exist
    db_item = get_conversation(session)
    if db_item is None:
        system_message = [{"role": "system", "content": "You are Hal, an advanced AI system capable of understanding human behaviour. You answer questions as concisely as possible. However your knowledge cutoff is September 2021"}]
        create_conversation(session, system_message)
    
    # Add new user message to conversation
    user_message = {"role": "user", "content": query}
    update_conversation(session, user_message)
    
    # Get entire conversation to send to GPT API
    db_item = get_conversation(session)
    conversation = []
    for message in db_item['conversation']:
        conversation.append({"role": message['role'], "content": message['content']})
    
    # Send entire conversation to GPT API
    print("Requesting GPT: " + json.dumps(conversation))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )
    print("GPT response: " + json.dumps(completion))
    reply = completion['choices'][0]['message']['content']
    
    # Add new assistant message to conversation
    assistant_message = {"role": "assistant", "content": completion['choices'][0]['message']['content']}
    update_conversation(session, assistant_message)
    
    return reply