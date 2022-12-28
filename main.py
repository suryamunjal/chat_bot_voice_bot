from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

#creating a chatbot variable
chatbot = \
ChatBot('ChatBot')

#creating a trainer using chatbot variable
trainer = ChatterBotCorpusTrainer(chatbot)

#now we will use english language corpus to train our chatbot using our trainer

trainer.train("chatterbot.corpus.english")  #we can change language, also provide custom yml file

print("hi i am chatbot")
while True:
    query=input(">>>")
    print(chatbot.get_response(Statement(text=query,search_text=query)))

