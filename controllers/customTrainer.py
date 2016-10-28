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

chatterbot.train([
    "What is a hackathon?",
    "A hackathon is an intense session that brings together computer programmers, designers, and specialists to build a product within a stipulated period of time.",
])

chatterbot.train([
    "Who should attend?",
    "Anybody who has a knack for solving problems, likes to code, design and develop unique ideas and models are welcome to participate at the hackathon.",
])
chatterbot.train([
    "What is the maximum team size?",
    "A maximum of 3 members per team will be taken on a first come first serve basis. A total of 60 teams will be admitted to the hackathon.",
])
chatterbot.train([
    "What is the judging criteria?",
    "The complete end product that has been developed over the period of the hackathon is judged to see whether any new innovative idea has been brought to the table. The design and implementation of the code are also taken into account. The presentation of the product is also an important factor.",
])
chatterbot.train([
    "What should I bring?",
    "All the participants are required to bring their laptops and any material that the team requires to use during the hackathon. No material for the hack will be provided.",
])
chatterbot.train([
    "How do I form a team?",
    "If you do not already have a team you can come to the event and we will assign you to a team to participate for the hackathon.",
])

chatterbot.train([
    "Will there be provision for food?",
    "Yes, dinner that includes pizzas from dominos will be provided free of cost. The breakfast and lunch on 16th will not be provided till further notice.",
])

chatterbot.train([
    "What went down in 2015?",
    "NodeJS Workshop, Devfest'15, IWD'16, Android Study Jam",
])

chatterbot.train([
    "Who is sponsoring this event?",
    "Cardea Labs, miBeat, Chalk Street, VentureSity and ofcourse Google.",
])
chatterbot.train([
    "Who are the Speakers?",
    "Manoranjan Padhy ,Social Media & Community Manager,Google and Ashish Rajput who is Co - Founder of Roder.in. Also Abhinav Cardea who is CEO of Cardea Labs",
])

chatterbot.train([
    "When will the hackathon start?",
    "Hackathon will start on 15 October,2016 and end on 16 October, 2016.",
])

chatterbot.train([
    "Where are we right now?",
    "Homi Bhabha Gallery, SJT 412, VIT University",
])

chatterbot.train([	
    "Which language are you written in?",
    "Python Ofcourse!! It's the best language.",
])

chatterbot.train([	
    "Who made you?",
    "Necessity! Just kidding developers at Google Developers Group - VIT Vellore made me, so that they could feel really cool.",
])

chatterbot.train([	
    "Why was I selected?",
    "You are special.",
])

chatterbot.train([	
    "What should I make in Hackathon?",
    "Start making whatever you dreamt of making but didn't start.",
])

chatterbot.train([	
    "Tell me a joke.",
    "Algorithm is a word used by programers when they don't want to explain what they did. Nerdy right :)",
])
chatterbot.train([	
    "Will I win this Hackathon?",
    "Yes why not but try a little harder, everyone's here for winning.",
])
#Train if user says Bye! :/

chatterbot.train([
	'Bye',"Bye! I'll miss you!"])
chatterbot.train(['what is the best chapter','GDG-VIT VELLORE'])
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
