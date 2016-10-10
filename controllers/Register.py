from modules import *

class RegisterHandler(RequestHandler):
    
    @coroutine
    @removeslash
    def get(self):
        self.render("register.html")
    @coroutine
    @removeslash
    def post(self):
        name=self.get_argument('name')
        #appId=self.get_argument('appId')
        emailId=self.get_argument('emailId')
        if not(bool(name) and bool(re.search(r".+@\w+\.(com|co\.in)",emailId))):
            self.write('{name&emailId:empty}')
            return
           
        result=yield db.users.find_one({'name':name,'emailId':emailId})
        if(bool(result)):
            self.write('{name&emailId:alreadyRegistered}')
        else:        
            yield db.users.insert({'name':name,'emailId':emailId})
            self.write('{register:success}')
            
