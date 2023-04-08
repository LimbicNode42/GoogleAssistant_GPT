import os
import openai
import simplejson

openai.organisation = "org-Hn9PU0jqMAhrgfGZ5eSdG14t"
openai.api_key = os.getenv("OPENAI_API_KEY")

data = openai.Model.list()

with open("retrieve_models.json", "w") as f:
    simplejson.dump(data, f, indent=4, sort_keys=True)