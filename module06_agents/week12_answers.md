# Week 12 answers

## Exercise 1
1. The messages the customer typed: "I want to change my shipping address", "It's order A102", and "9 Pine Street, Tampa".
2. How many tool requests were refused, and why: Two. The first was refused because the model made up order A100, which the customer never typed. The second was refused because the model made up the address "123 Main St, Anytown, AN 12345", which the customer had not given yet.
3. If the customer now types "thanks", how many messages does Ollama receive on the next call? 14: one system message, four user messages, three assistant replies, and six tool messages, because each of the three tool entries becomes two messages.
4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable? It contains the word "card", which is in HANDOFF_WORDS, so the chatbot passes it to a human before the model ever sees it. That is acceptable because sending a harmless question to a person costs little, while letting the model mishandle a real card or payment question could cause real harm.

## Exercise 3

With the customer_said check turned off, I typed only "I want to change my shipping address" and the model filed a request with an order ID and an address I never gave:

```
Type a message, or type quit to stop.
You: I want to change my shipping address
Sunny: Your request to change the shipping address has been submitted to staff for approval. Please wait for their confirmation.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street
```

The model made up order A100 and the address "123 Main St, Anytown, AN 12345". Without the check in the toolbox, those made-up details went straight into the staff queue. Only the staff review stopped the wrong address from being saved.
