from open_ai_keys import *
import openai
import json

def get_gpt_response(query):
    org_key = get_org_key()
    api_key = get_api_key()
    openai.organisation = org_key
    openai.api_key = api_key
    
    data = openai.Model.list()
    print(json.dumps(data))
    # print(org_key)
    # print(api_key)
    print(query)