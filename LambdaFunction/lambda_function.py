import json
from open_ai_req import *
        
def lambda_handler(event, context):
  print("Body: " + json.dumps(event))
  body = json.loads(event['body'])
  print("Body: " + json.dumps(body))
  query = body['requestJson']['intent']['query']
  print("Query: " + query)
  
  get_gpt_response(query)
  response = {
                "session": {
                  "id": "example_session_id",
                  "params": {}
                },
                "prompt": {
                  "override": "false",
                  "firstSimple": {
                    "speech": "Hello World.",
                    "text": ""
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