#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#defining name for chatbot and defining trainer
bot=ChatBot("VIRAT KOHLI")
bot.set_trainer(ListTrainer)

#accessing chatterbot corpus
for files in os.listdir('C:/Users/Jahnavi/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english'):
    data=open('C:/Users/Jahnavi/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)
while True:
        message=input('You:')
        if message.strip!='Bye' or message.strip!='bye':
                reply=bot.get_response(message)
                print('Chatbot:',reply)
        if message.strip=='Bye' or message.strip=='bye':
                print('Chatbot:It was nice talking to you')
                break

