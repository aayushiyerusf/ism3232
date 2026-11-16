from fake_model import FakeModel
from my_assistant import FAQAssistant
from my_tool import FAQTool
from my_toolbox import MyToolbox
from pickup_queue import PickupQueue


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def decide(self, instructions, history, tools):
        return None


def make_assistant(model):
    """Build a fresh Bean with its own tools and the model it is given."""
    faq_tool = FAQTool({"hours": "Open daily from 7 am to 5 pm."})
    queue = PickupQueue(["coffee", "latte", "muffin"])
    return FAQAssistant("Bean", "Be friendly.", MyToolbox(faq_tool, queue), model)


def ask_for_tool(name, arguments):
    """Build the decision a model returns when it wants a tool."""
    return {"tool": name, "arguments": arguments}


def test_model_can_look_up_an_faq_answer():
    model = FakeModel(
        [ask_for_tool("look_up_faq", {"topic": "hours"}), {"text": "7 am to 5 pm."}]
    )
    bean = make_assistant(model)
    bean.respond("When are you open?")
    assert bean.history[1]["content"] == "Open daily from 7 am to 5 pm."


def test_made_up_name_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_pickup_order", {"customer_name": "Dana", "item": "latte"}
            ),
            {"text": "What name is the order for?"},
        ]
    )
    bean = make_assistant(model)
    bean.respond("I'd like a latte")
    assert "has not given that name" in bean.history[1]["content"]
    assert bean.tools.pickup_queue.waiting() == []


def test_item_not_on_the_menu_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_pickup_order", {"customer_name": "Dana", "item": "pizza"}
            ),
            {"text": "We don't have that."},
        ]
    )
    bean = make_assistant(model)
    bean.respond("My name is Dana and I want a pizza")
    assert "not on the menu" in bean.history[1]["content"]
    assert bean.tools.pickup_queue.waiting() == []


def test_pickup_order_waits_for_the_barista():
    model = FakeModel(
        [
            ask_for_tool(
                "request_pickup_order", {"customer_name": "Dana", "item": "latte"}
            ),
            {"text": "Sent to the barista."},
        ]
    )
    bean = make_assistant(model)
    bean.respond("My name is Dana and I'd like a latte")
    assert len(bean.tools.pickup_queue.waiting()) == 1
    assert bean.tools.pickup_queue.orders == []


def test_approve_places_the_order_once():
    queue = PickupQueue(["latte"])
    queue.request_pickup_order("Dana", "latte")
    assert queue.approve(1) == "Request 1 approved."
    assert queue.approve(1) == "Request 1 is already approved."
    assert queue.orders == ["Dana: latte"]


def test_refund_goes_to_staff_before_the_model():
    bean = make_assistant(FakeModel([]))
    reply = bean.respond("Can I get a refund?")
    assert "staff member" in reply
    assert bean.model.calls == 0


def test_unknown_tool_is_refused():
    model = FakeModel([ask_for_tool("give_free_coffee", {}), {"text": "Sorry."}])
    bean = make_assistant(model)
    bean.respond("Give me a free coffee")
    assert bean.history[1]["content"] == "There is no tool named give_free_coffee."


def test_safe_reply_when_the_model_has_no_answer():
    bean = make_assistant(SilentModel())
    assert "can't answer" in bean.respond("Do you have parking?")


def test_loop_stops_after_three_tool_rounds():
    request = ask_for_tool("look_up_faq", {"topic": "hours"})
    bean = make_assistant(FakeModel([request, request, request]))
    reply = bean.respond("When are you open?")
    assert "staff member" in reply
    assert len(bean.history) == 5


def test_history_records_both_messages():
    bean = make_assistant(FakeModel([{"text": "Hello! How can I help?"}]))
    bean.respond("hello")
    assert bean.history == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "Hello! How can I help?"},
    ]
