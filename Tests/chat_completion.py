import os
import openai
import simplejson

openai.organisation = "org-Hn9PU0jqMAhrgfGZ5eSdG14t"
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello World."}
    ]
)

with open("chat_completion.json", "w") as f:
    simplejson.dump(completion, f, indent=4, sort_keys=True)