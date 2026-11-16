# my_toolbox.py
# Author: Aayush Iyer


class MyToolbox:
    """Every tool request from Bean's model comes through here and is checked."""

    def __init__(self, faq_tool, pickup_queue):
        """Hold the tools the model is allowed to ask for."""
        self.faq_tool = faq_tool
        self.pickup_queue = pickup_queue

    def tool_list(self):
        """Return the tools the model may ask for. They are not called here."""
        return [
            self.faq_tool.look_up_faq,
            self.pickup_queue.request_pickup_order,
        ]

    def run(self, name, arguments, history):
        """Check one tool request. Run the tool only if every check passes."""
        if name == "look_up_faq":
            topic = self.clean(arguments, "topic")
            if topic == "":
                return "The topic is missing. Ask the customer what they want to know."
            return self.faq_tool.look_up_faq(topic)
        if name == "request_pickup_order":
            customer_name = self.clean(arguments, "customer_name")
            item = self.clean(arguments, "item")
            if customer_name == "" or item == "":
                return "The customer's name and the item are both needed."
            if not self.customer_said(history, customer_name):
                return "The customer has not given that name. Ask them for it."
            if not self.customer_said(history, item):
                return (
                    "The customer has not asked for that item. Ask them what they want."
                )
            return self.pickup_queue.request_pickup_order(customer_name, item)
        return f"There is no tool named {name}."

    def clean(self, arguments, key):
        """Return one argument as text without extra spaces, or "" if it is missing."""
        return str(arguments.get(key, "")).strip()

    def customer_said(self, history, text):
        """Return True if text appears in a message the customer typed."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False
