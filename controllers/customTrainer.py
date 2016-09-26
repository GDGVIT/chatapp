'''
A custom trainer to train according to the Devfest Questions.
'''

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
chatterbot = ChatBot("Training our GDG Bot with some tests.")
chatterbot.set_trainer(ListTrainer)

"""chatterbot.train([
    "Which chapter it is?",
    "This is Google Developers Group - VIT Vellore",
])

chatterbot.train([
    "How long will the hackathon last?",
    "This is a 24 hours hackathon.",
])

#Train if user says Bye! :/

chatterbot.train([
	'Bye',"Bye! I'll miss you!"])"""
