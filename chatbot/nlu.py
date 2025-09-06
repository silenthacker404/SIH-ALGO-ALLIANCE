import json
import re

# Load intents
with open("chatbot/intents.json") as f:
    intents = json.load(f)["intents"]

def get_intent(user_msg):
    user_msg = user_msg.lower()
    for intent in intents:
        for pattern in intent["patterns"]:
            if re.search(pattern, user_msg):
                return intent["tag"]
    return "unknown"
