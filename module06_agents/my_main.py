# my_main.py
# Author: Aayush Iyer

from my_assistant import FAQAssistant
from my_tool import FAQTool
from my_toolbox import MyToolbox
from ollama_model import OllamaModel
from pickup_queue import PickupQueue

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Bean, a friendly assistant for a small coffee shop.
Answer in one short sentence.
Wi-Fi is free for customers.
We offer oat milk and almond milk at no extra cost.
If the customer only says hello, greet them and ask how you can help.
To place a pickup order you need the customer's name and one menu item.
Only state facts that appear in these instructions or in tool results.
If you do not know, say you do not know and suggest asking a staff member at the counter."""

ANSWERS = {
    "hours": "We are open daily from 7 am to 5 pm.",
    "location": "We are at 123 Bay Street. This is a fictional address.",
    "menu": "We serve coffee, tea, lattes, muffins, and sandwiches.",
}

MENU = ["coffee", "tea", "latte", "muffin", "sandwich"]

faq_tool = FAQTool(ANSWERS)
pickup_queue = PickupQueue(MENU)
tools = MyToolbox(faq_tool, pickup_queue)
model = OllamaModel(MODEL_NAME)
assistant = FAQAssistant("Bean", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
message = input("You: ")
while message.lower() != "quit":
    print(f"{assistant.name}: {assistant.respond(message)}")
    message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

print("Barista review")
for request in pickup_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['customer_name']}, {request['item']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(pickup_queue.approve(number))
    else:
        print(pickup_queue.reject(number))

print(f"Orders placed: {len(pickup_queue.orders)}")
for order in pickup_queue.orders:
    print(order)
