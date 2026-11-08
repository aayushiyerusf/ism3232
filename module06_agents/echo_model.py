# echo_model.py
# Author: Aayush Iyer


class EchoModel:
    """A stand-in model that repeats the last message back."""

    def reply(self, instructions, history):
        """Return 'You said:' followed by the last message in the history."""
        last_message = history[-1]["content"]  # history[-1] is the newest message
        return f"You said: {last_message}"  # echo it back with a prefix
