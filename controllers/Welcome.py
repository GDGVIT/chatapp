from modules import *

class WelcomeHandler(RequestHandler):
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
			
