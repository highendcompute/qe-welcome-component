"""
This function saves a welcome message.
"""

import json

def welcome():
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        # Write message to file as this will serve as output artifact
        f.write(json.dumps(message_dict, indent=2)) 
