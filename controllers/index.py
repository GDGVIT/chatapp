
from modules import *

class IndexHandler(RequestHandler):
	@coroutine
	@removeslash
	def get(self):
		#self.write("<p>What is your name:</p>")
		self.render("register.html")
		'''emailId=self.get_argument('emailId')
		response=chatbot.get_response(emailId)	
		
		response = chatbot.get_response(question)
		'''
		'''Print the response based upon the training
		'''
		'''
		self.write('{response:%s}'%response)
		'''
