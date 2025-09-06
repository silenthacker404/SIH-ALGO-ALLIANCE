import json
import random

with open("chatbot/intents.json") as f:
    intents = json.load(f)["intents"]

def get_response(intent, user_msg):
    for i in intents:
        if i["tag"] == intent:
            return random.choice(i["responses"])
    return "I'm not sure about that. Please consult a nearby health professional."
