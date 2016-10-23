'''
A custom trainer to train according to the Devfest Questions.
'''

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
chatterbot = ChatBot("Training our GDG Bot with some tests.",database="database.db")
'''
some training examples Modify as needed write new ones for your orgainzation
chatterbot.train([	
    "Which chapter it is?",
    "This is Google Developers Group - VIT Vellore",
])

chatterbot.train([
    "How long will the hackathon last?",
    "This is a 24 hours hackathon.",
])

#Train if user says Bye! :/

chatterbot.train([
	'Bye',"Bye! I'll miss you!"])
chatterbot.train(['what is the best chapter','GDG-VIT VELLORE'])
'''

'''
#Initially run :
from chatterbot.trainers import ChatterBotCorpusTrainer
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train(
    "chatterbot.corpus.english"
)

'''
chatterbot.set_trainer(ListTrainer)
print("press Ctrl+C to quit:")
while True:
	question=raw_input("Enter question: ")
	answer=raw_input("Answer: ")
	chatterbot.train([question,answer])
	print 'trained to say reply ',answer,' for ',question

