import re

def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower().strip())

def match_intent(user_input, intents):
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if re.search(rf"\b{pattern}\b", user_input):
                return intent
    return "default"

def chatbot():
    intents = {
        "greeting": {
            "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
            "responses": ["Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?"]
        },
        "goodbye": {
            "patterns": ["bye", "goodbye", "see you", "later"],
            "responses": ["Goodbye! Have a great day!", "See you soon!", "Bye! Take care!"]
        },
        "thanks": {
            "patterns": ["thank you", "thanks", "thx"],
            "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
        },
        "how_are_you": {
            "patterns": ["how are you", "how is it going", "how are things"],
            "responses": ["I'm a bot, so I don't have feelings, but I'm here to help!", "Doing great! Ready to assist!"]
        },
        "name": {
            "patterns": ["what is your name", "who are you", "your name"],
            "responses": ["I’m a simple chatbot created in Python.", "You can call me ChatPy."]
        },
        "default": {
            "patterns": [],
            "responses": ["I'm not sure I understand that. Could you rephrase?", "Sorry, I don't know how to respond to that."]
        }
    }

    print("Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye!")
            break

        normalized_input = normalize(user_input)
        intent = match_intent(normalized_input, intents)
        response_list = intents[intent]["responses"]
        print("Chatbot:", response_list[0])

chatbot()
