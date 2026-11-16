# my_assistant.py
# Author: Aayush Iyer

HANDOFF_WORDS = ["refund", "payment"]
MAX_TOOL_ROUNDS = 3


class FAQAssistant:
    """A coffee shop assistant. The model decides. The toolbox checks every request."""

    def __init__(self, name, instructions, tools, model):
        """Set up one assistant with its own name, instructions, tools, model, and history."""
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.model = model
        self.history = []

    def respond(self, message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": message})
        reply = self.choose_reply(message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, message):
        """Pass refunds and payments to staff. Send everything else to the model."""
        if self.needs_human(message.lower()):
            return "A staff member must handle refunds and payments. Please ask at the counter."
        return self.model_reply()

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def model_reply(self):
        """Ask the model. Run each tool it asks for, then ask again, up to a limit."""
        rounds = 0
        while rounds < MAX_TOOL_ROUNDS:
            tool_list = self.tools.tool_list()
            decision = self.model.decide(self.instructions, self.history, tool_list)
            if decision is None:
                return (
                    "Sorry, I can't answer that right now. Please ask at the counter."
                )
            if "text" in decision:
                return decision["text"]
            name = decision["tool"]
            arguments = decision["arguments"]
            result = self.tools.run(name, arguments, self.history)
            self.history.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "arguments": arguments,
                    "content": result,
                }
            )
            rounds += 1
        return (
            "Sorry, I couldn't finish that. Please ask a staff member at the counter."
        )
