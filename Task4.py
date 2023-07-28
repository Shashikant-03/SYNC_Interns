import nltk
from nltk.chat.util import Chat, reflections
import time

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],
    [
        r"what is your name?|Are you human?|Are you a robot?",
        ["You can call me Chatbot.", "I'm just a simple chatbot.", "I go by the name Chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "All good! How about you?"]
    ],
    [
        r"(.*) (hungry|thirsty|tired)",
        ["I'm just a program, so I don't experience physical needs."]
    ],
    [
        r"(.*) (help|support|assist)",
        ["Sure, I'd be happy to help. How can I assist you?", "Of course! What do you need help with?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a great day!"]
    ],
    [
        r"what is current time ?",
        ["Current time is {}".format(time.strftime("%H:%M:%S",time.localtime()))]
    ],
        [
        r"what is today date ?",
        ["Today date is {}".format(time.strftime(" %d %b %Y ",time.localtime()))]
    ],
        [
        r"What day is it today?",
        ["Today day is {}".format(time.strftime("%A ",time.localtime()))]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Can you please rephrase your question?", "I'm not sure I follow. Could you try asking differently?"]
    ],
    
]

def create_chatbot():
    chatbot = Chat(pairs, reflections)
    return chatbot

if __name__ == "__main__":
    print("Chatbot: Hi there! I'm your chatbot. How can I help you today?")
    chatbot = create_chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
