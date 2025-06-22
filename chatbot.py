import nltk
from nltk.chat.util import Chat, reflections


# Define chatbot pairs (patterns and responses)
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm a chatbot, I'm always good!", "Doing well, thank you!"]],
    [r"what is your name?", ["You can call me CodBot.", "I'm CodTech's NLP Chatbot."]],
    [r"who created you?", ["I was created as a part of an internship task."]],
    [r"what can you do?", ["I can answer simple questions using NLP.", "I help demonstrate basic AI concepts."]],
    [r"(.*) your internship (.*)", ["This chatbot is built for the CodTech internship project."]],
    [r"(.*) (location|city)", ["I'm just virtual, but you can find me anywhere!"]],
    [r"(.*) help (.*)", ["Sure, I'm here to help. Just ask me anything!"]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Thanks for chatting!"]],
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("🤖 CodBot: Hi! I'm your AI Chatbot. Type 'bye' to exit.")
chatbot.converse()
