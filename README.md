# GoogleAssistant_GPT
Integrating ChatGPT with Google Assistant

Implemented by making a call to an AWS Lambda function from Google Actions.
Lambda Function then makes a call to the gpt-3.5-turbo API and returns the reply to Google Actions in this format
{
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

Conversation history is recorded in an AWS DynamoDB which allows the user to refer to previous messages.
Each conversation that can be referred back to is per Google Assistant sessions as that session id is the PK.


IMPROVEMENTS TODO:
Send conversation to Discord
Maintain conversations across Google Assistant sessions
Implement for Alexa
