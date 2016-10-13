'''
A custom trainer to train according to the Devfest Questions.
'''

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
chatterbot = ChatBot("Training our GDG Bot with some tests.")
chatterbot.set_trainer(ListTrainer)


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
'''
from chatterbot import ChatBot
import logging
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
chatterbot = ChatBot('Chitty',
    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.adapters.logic.ClosestMatchAdapter'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.adapters.input.TerminalAdapter',
    output_adapter='chatterbot.adapters.output.TerminalAdapter',
    database='chatterbot-ver1'
)
chatterbot.set_trainer(ListTrainer)
#chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english"
)
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
print('Type something to begin...')

while True:
    try:
        bot_input = chatterbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
'''
