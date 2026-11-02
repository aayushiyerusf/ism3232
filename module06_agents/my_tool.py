# my_tool.py
# Author: Aayush Iyer


class FAQTool:  # Define a tool that looks up FAQ answers.
    def __init__(self, answers):  # Accept a dictionary of topics and answers.
        self.answers = answers  # Store the answers on this tool.

    def find_answer(self, text):  # Look for a known topic in the message.
        text = text.lower()  # Allow matching regardless of capitalization.
        for topic in self.answers:  # Check each topic in the dictionary.
            if topic.lower() in text:  # Check whether the topic was mentioned.
                return self.answers[topic]  # Return the stored answer.
        return None  # Report that no matching answer was found.
