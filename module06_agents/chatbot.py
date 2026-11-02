# chatbot.py
# Author: Aayush Iyer

HANDOFF_WORDS = ["address", "payment", "card"]


class SupportChatbot:
    """A mock support chatbot. Its replies come from simple rules, not from AI."""

    def __init__(
        self, name, instructions, order_tool, stock_tool
    ):  # Receive both tools.
        self.name = name  # Store the name.
        self.instructions = instructions  # Store the instructions.
        self.order_tool = order_tool  # Store the order tool.
        self.stock_tool = stock_tool  # Store the stock tool.
        self.history = []  # Start an empty history.

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."
        if "stock" in text:  # Detect a stock question.
            return self.stock_reply(user_message)  # Use the stock tool.
        if "order" in text:
            return self.order_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check an order status for you."
        return "I'm not sure how to help with that. I can check an order status."

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        """Use the order tool to answer a question about an order."""
        order_id = self.order_tool.find_order_id(user_message)
        if order_id is None:
            return "Which order? Please send an order ID like A100."
        status = self.order_tool.find_status(order_id)
        return f"Order {order_id} is {status}."

    def count_user_messages(self):  # Count this bot's user messages.
        count = 0  # Start the count at zero.
        for message in self.history:  # Examine each history entry.
            if message["role"] == "user":  # Select user entries.
                count += 1  # Increase the count by one.
        return count  # Return the final count.

    def stock_reply(self, user_message):  # Answer a stock question.
        product = self.stock_tool.find_product(user_message)  # Find the product.
        if product is None:  # Handle a missing product.
            return "Which product? Please name the item you want me to check."
        count = self.stock_tool.count_for(product)  # Get the stock count.
        return f"We have {count} of the {product} in stock."  # Give the answer.
