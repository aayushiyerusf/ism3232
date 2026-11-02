# my_main.py
# Author: Aayush Iyer

from my_assistant import FAQAssistant
from my_tool import FAQTool

ANSWERS = {
    "hours": "We are open daily from 7 am to 5 pm.",
    "location": "We are at 123 Bay Street. This is a fictional address.",
    "menu": "We serve coffee, tea, muffins, and sandwiches.",
}

tool = FAQTool(ANSWERS)
assistant = FAQAssistant("Bean", tool)

print("Type a message, or type quit to stop.")
message = input("You: ")

while message.lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(message)}")
    message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
