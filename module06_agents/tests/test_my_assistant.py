from mock_model import MockModel
from my_assistant import FAQAssistant
from my_tool import FAQTool


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_assistant():
    answers = {"hours": "Open daily from 7 am to 5 pm."}
    return FAQAssistant("Bean", "Be friendly.", FAQTool(answers), MockModel())


def make_assistant_with_silent_model():
    answers = {"hours": "Open daily from 7 am to 5 pm."}
    return FAQAssistant("Bean", "Be friendly.", FAQTool(answers), SilentModel())


def test_assistant_uses_tool_answer():
    tool = FAQTool({"hours": "Special hours: 8 am to noon."})
    assistant = FAQAssistant("Bean", "Be friendly.", tool, SilentModel())
    assert assistant.respond("What are your HOURS?") == "Special hours: 8 am to noon."


def test_unknown_question_goes_to_the_model():
    assistant = make_assistant()
    reply = assistant.respond("Do you have parking?")
    assert "not sure" in reply


def test_safe_reply_when_the_model_has_no_answer():
    assistant = make_assistant_with_silent_model()
    reply = assistant.respond("Do you have parking?")
    assert "can't answer" in reply
    assert "Ask about" in reply


def test_payment_request_goes_to_staff_before_faq():
    assistant = make_assistant_with_silent_model()
    reply = assistant.respond("During what hours can I get a refund?")
    assert "staff member" in reply
    assert "counter" in reply


def test_history_records_both_messages():
    assistant = make_assistant()
    reply = assistant.respond("hello")
    assert assistant.history == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": reply},
    ]
