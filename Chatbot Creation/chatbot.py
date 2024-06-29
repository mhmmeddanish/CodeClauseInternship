import nltk
from nltk.chat.util import Chat, reflections
import spacy

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return f"Hello {ent.text}, how can I help you?"
    return "I am sorry, I do not understand."

def chatbot():
    pairs = [
        [
            r"my name is (.*)",
            ["Hello %1, How are you today?",]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey there",]
        ],
        [
            r"what is your name?",
            ["I am a chatbot created by you.",]
        ],
        [
            r"how are you?",
            ["I'm doing good\nHow about You?",]
        ],
        [
            r"sorry (.*)",
            ["It's alright", "It's OK, never mind",]
        ],
        [
            r"I am fine",
            ["Great to hear that, How can I help you?",]
        ],
        [
            r"quit",
            ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
        ],
    ]
    
    print("Hi, I'm a chatbot created by you. Type 'quit' to exit.") 
    chat = Chat(pairs, reflections)
    chat.converse()

def main():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bye, take care. See you soon :)")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Call the basic chatbot
    chatbot()
    
    # You can switch to the spaCy based chatbot by commenting the line above and uncommenting the line below
    # main()
