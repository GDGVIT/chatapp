from modules import *

class QuestionHandler(RequestHandler):
	'''when user scrolls down to the FAQ section an ajax request to the get method for welcoming the user
	   also when te user scolls then the text welcoming the user must be dynamically deleted
	'''
	@coroutine
	@removeslash
	def get(self):
		status_code=True
		emailId=self.get_argument('email')
		result=yield db.users.find_one({'emailId':emailId})
		if result:			
			self.write('{status:%s,name:%s}'%(status_code,result['name']))
		else:
			self.write('{status:%s}'%(status_code))	
	@coroutine
	@removeslash
	def post(self):
		#self.write("<p>What is your name:</p>")
		question=self.get_argument('question');			
		response = chatbot.get_response(question)
		print 'response',response	
		'''
		Print the response based upon the training
		'''
		self.write('{response:%s}'%response)
