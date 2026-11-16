# my_tool.py
# Author: Aayush Iyer


class FAQTool:
    """A tool that knows the coffee shop's answers. It knows nothing about chatting."""

    def __init__(self, answers):
        """Store a dictionary of topics and answers."""
        self.answers = answers

    def find_answer(self, text):
        """Return the answer for the first known topic in text, or None."""
        text = text.lower()
        for topic in self.answers:
            if topic.lower() in text:
                return self.answers[topic]
        return None

    def look_up_faq(self, topic):
        """Look up the coffee shop's answer about hours, location, or menu.

        Args:
            topic: The topic to look up, like hours, location, or menu.
        """
        answer = self.find_answer(topic)
        if answer is None:
            return "There is no answer for that topic. Topics are hours, location, and menu."
        return answer
