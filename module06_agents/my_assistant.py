# my_assistant.py
# Author: Aayush Iyer


class FAQAssistant:  # Define a mock coffee shop assistant.
    def __init__(self, name, faq_tool):  # Receive a name and a separate tool.
        self.name = name  # Store the assistant's name.
        self.faq_tool = faq_tool  # Store the tool; this is composition.
        self.history = []  # Give this assistant its own message history.

    def respond(self, message):  # Record a turn and return the reply.
        self.history.append(
            {"role": "user", "content": message}
        )  # Save the user message.
        reply = self.choose_reply(message)  # Select a reply using rules.
        self.history.append({"role": "assistant", "content": reply})  # Save the reply.
        return reply  # Give the reply to the calling code.

    def choose_reply(self, message):  # Choose a reply without an AI model.
        text = message.lower()  # Make keyword checks case insensitive.
        if "refund" in text or "payment" in text:  # Identify requests needing staff.
            return "A staff member must handle refunds and payments. Please ask at the counter."  # Explain the handoff.
        if "hello" in text:  # Recognize a greeting.
            return f"Hello! I'm {self.name}. Ask about hours, location, or menu."  # Introduce the assistant.
        answer = self.faq_tool.find_answer(message)  # Ask the tool for an answer.
        if answer is None:  # Handle a lookup that finds nothing.
            return "I don't have an answer for that. Ask about hours, location, or menu."  # Give a safe, helpful reply.
        return answer  # Return the answer supplied by the tool.
