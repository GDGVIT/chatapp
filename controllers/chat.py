from modules import *

class QuestionHandler(RequestHandler):
	@coroutine
	@removeslash
	def get(self):
		#self.write("<p>What is your name:</p>")
		question=self.get_argument('question');	
		
		response = chatbot.get_response(question)
		'''
		Print the response based upon the training
		'''
		self.write('{response:%s}'%response)
