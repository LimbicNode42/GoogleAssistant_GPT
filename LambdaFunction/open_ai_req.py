from open_ai_keys import *
import openai
import json

def get_gpt_response(query):
    org_key = get_org_key()
    api_key = get_api_key()
    openai.organisation = org_key
    openai.api_key = api_key
    
    # data = openai.Model.list()
    # print(json.dumps(data))
    
    print("Initiating GPT-3.5 Turbo")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Hal, an advanced AI system capable of understanding human behaviour. You answer questions as concisely as possible. However your knowledge cutoff is September 2021"},
            {"role": "user", "content": query},
        ]
    )
    print(json.dumps(completion))
    
    return "Hello World"