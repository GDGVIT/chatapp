from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine
from chatterbot import ChatBot
import os

#A custom trainer module to train the Bot according to the Devfest needs.
import customTrainer
chatbot = ChatBot(
    'GDG BOT',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
#Name of the Chat Bot
name = chatbot.name
from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training chatbot")
chatterbot.set_trainer(ListTrainer)

#question = ''
# Get a response to an input statement

class QuestionHandler(RequestHandler):
	#@coroutine
	#@removeslash
	def get(self):
		#self.write("<p>What is your name:</p>")
		question=self.get_argument('question');	
		
		#while(question!="Bye"):
		#Ask a question
		#question = raw_input('You: ')
		
		response = chatbot.get_response(question)
		'''
		Print the response based upon the training
		'''
		self.write('{response:%s}'%response)
		#print name + ': ' + str(response)
			
settings = dict(
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret="35an18y3-u12u-7n10-4gf1-102g23ce04n6",
        debug=True)
        
application=Application([
(r"/", QuestionHandler)
],**settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(os.environ.get("PORT", 5000))
	IOLoop.current().start()	
