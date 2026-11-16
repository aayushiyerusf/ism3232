## Coffee Shop FAQ Assistant — Lab 10

My assistant, Bean, answers questions about a fictional coffee shop's hours, location, and menu.
It uses keyword rules and a dictionary of answers, so it is a mock chatbot with no AI model or internet connection.
The assistant receives a separate FAQ tool and records each user message and assistant reply in its history.
Refund and payment requests go to a staff member at the counter because the assistant cannot authorize refunds or access payment systems.
If real customer data were used, saving private information in the conversation history could expose it to someone who should not see it.

## Week 11: Adding a model

Bean now uses a local AI model (granite4.1:3b through Ollama) for any question that the rules and the FAQ tool do not cover.

The model answered "Is there wifi?" and "Do you have oat milk?" correctly, because both facts are in its instructions.
When I asked "Do you have parking?" it invented an answer about public parking lots nearby, even though parking is not in its instructions and it was told to only state facts it was given.

I kept hours, location, and menu in the FAQ tool so those answers are always exact and cannot be invented by the model.
Refunds and payments are still sent to staff in code, because the model cannot be trusted with anything that has to be right.
The tests use a mock model, so they pass even with Ollama switched off.

## Week 12: Letting Bean choose its tool

Bean's model now decides when to use a tool, every tool request goes through one checked door (MyToolbox), and a pickup order waits in a queue until the barista approves it.
The model handled "What are your hours?" well: it asked for the look_up_faq tool and answered with the exact hours from the FAQ tool instead of inventing them.
When I asked for a latte without giving my name, Bean asked for my name instead of placing the order, because the door refuses a pickup request with a name the customer never typed; my test_made_up_name_is_refused test shows a model making up the name "Dana" and the door refusing it.
After I gave my name, the order went to the barista review and was only placed when I typed yes, and approving it a second time changes nothing.
I added "If the customer only says hello, greet them and ask how you can help" to the instructions, so a greeting gets a greeting instead of a tool call.
Refunds and payments still go to a staff member in code, before the model ever sees the message.
