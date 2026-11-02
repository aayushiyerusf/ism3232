# two_bots.py
# Author: Aayush Iyer

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

# Create tools that both chatbots will share.
order_tool = OrderLookup({"A100": "shipped"})
stock_tool = StockLookup({"rain jacket": 12})

# Each chatbot gets its own name, instructions, and history.
sunny = SupportChatbot(
    "Sunny",
    "You are cheerful and brief.",
    order_tool,
    stock_tool,
)

river = SupportChatbot(
    "River",
    "You are formal and detailed.",
    order_tool,
    stock_tool,
)

sunny.respond("hello")
sunny.respond("Where is order A100?")
river.respond("hello")

print(sunny.name, len(sunny.history))
print(river.name, len(river.history))
print(sunny.history[1]["content"])
print(river.history[1]["content"])
print(sunny.instructions)
print(river.instructions)
