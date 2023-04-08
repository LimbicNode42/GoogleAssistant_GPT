import json
from open_ai_req import *
        
def lambda_handler(event, context):
  print("Event: " + json.dumps(event))
  body = json.loads(event['body'])
  print("Body: " + json.dumps(body))
  query = body['intent']['query']
  print("Query: " + query)
  session = body['session']['id']
  print("Session: " + session)
  
  gpt_reply = get_gpt_response(query, session)
  response = {
                "session": {
                  "id": session,
                  "params": {}
                },
                "prompt": {
                  "override": "false",
                  "firstSimple": {
                    "speech": gpt_reply,
                    "text": gpt_reply
                  }
                },
                "scene": {
                  "name": "GPTLoop",
                  "slots": {},
                  "next": {
                    "name": "GPTLoop"
                  }
                }
              }
  
  return {
      # "statusCode": 200,
      "headers": {
          "Content-Type": "application/json"
      },
      "body": json.dumps(response)
  }