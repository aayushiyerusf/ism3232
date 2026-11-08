# my_main.py
# Author: Aayush Iyer

from my_assistant import FAQAssistant
from my_tool import FAQTool
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Bean, a friendly assistant for a small coffee shop.
Answer in one short sentence.
Wi-Fi is free for customers.
We offer oat milk and almond milk at no extra cost.
Only state facts that appear in these instructions.
If you do not know, say you do not know and suggest asking a staff member at the counter."""

ANSWERS = {
    "hours": "We are open daily from 7 am to 5 pm.",
    "location": "We are at 123 Bay Street. This is a fictional address.",
    "menu": "We serve coffee, tea, muffins, and sandwiches.",
}

tool = FAQTool(ANSWERS)
model = OllamaModel(MODEL_NAME)
assistant = FAQAssistant("Bean", INSTRUCTIONS, tool, model)

print("Type a message, or type quit to stop.")
message = input("You: ")

while message.lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(message)}")
    message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
