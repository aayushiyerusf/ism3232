# fallback_model.py
# Author: Aayush Iyer


class FallbackModel:
    """A model that asks a first model, and a second one if the first has no answer."""

    def __init__(self, first, second):
        """Store the two models, in the order they are asked."""
        self.first = first
        self.second = second

    def decide(self, instructions, history, tools):
        """Ask the first model. If it returns None, ask the second model."""
        decision = self.first.decide(instructions, history, tools)
        if decision is None:
            decision = self.second.decide(instructions, history, tools)
        return decision
