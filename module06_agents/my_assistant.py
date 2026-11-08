# my_assistant.py
# Author: Aayush Iyer


class FAQAssistant:  # A coffee shop assistant: rules first, then a model.
    def __init__(
        self, name, instructions, faq_tool, model
    ):  # Receive everything it needs.
        self.name = name  # Store the assistant's name.
        self.instructions = instructions  # Store the instructions sent to the model.
        self.faq_tool = faq_tool  # Store the tool; this is composition.
        self.model = model  # Store the model; also composition, so tests can swap it.
        self.history = []  # Give this assistant its own message history.

    def respond(self, message):  # Record a turn and return the reply.
        self.history.append(
            {"role": "user", "content": message}
        )  # Save the user message.
        reply = self.choose_reply(message)  # Select a reply.
        self.history.append({"role": "assistant", "content": reply})  # Save the reply.
        return reply  # Give the reply to the calling code.

    def choose_reply(self, message):  # Rules run first; the model handles the rest.
        text = message.lower()  # Make keyword checks case insensitive.
        if "refund" in text or "payment" in text:  # Money must go to a person, in code.
            return "A staff member must handle refunds and payments. Please ask at the counter."  # The handoff.
        answer = self.faq_tool.find_answer(
            message
        )  # Ask the tool first, since its facts are exact.
        if answer is not None:  # The tool found an answer.
            return answer  # Use the tool's exact answer, never the model's version.
        return (
            self.model_reply()
        )  # Nothing in the rules or tool covers it, so ask the model.

    def model_reply(self):  # Ask the model, with a safety net.
        reply = self.model.reply(
            self.instructions, self.history
        )  # Send instructions plus history.
        if reply is None:  # The model had no answer, e.g. Ollama is off.
            return "Sorry, I can't answer that right now. Ask about hours, location, or menu."  # Safe reply.
        return reply  # Return the model's reply.
