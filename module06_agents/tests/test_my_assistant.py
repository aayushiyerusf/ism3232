from my_assistant import FAQAssistant
from my_tool import FAQTool


def make_assistant():
    answers = {"hours": "Open daily from 7 am to 5 pm."}
    return FAQAssistant("Bean", FAQTool(answers))


def test_assistant_uses_tool_answer():
    tool = FAQTool({"hours": "Special hours: 8 am to noon."})
    assistant = FAQAssistant("Bean", tool)
    assert assistant.respond("What are your HOURS?") == ("Special hours: 8 am to noon.")


def test_missing_answer_gets_helpful_reply():
    assistant = make_assistant()
    assert assistant.faq_tool.find_answer("Do you have parking?") is None
    reply = assistant.respond("Do you have parking?")
    assert "don't have an answer" in reply
    assert "Ask about" in reply


def test_payment_request_goes_to_staff_before_faq():
    assistant = make_assistant()
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
