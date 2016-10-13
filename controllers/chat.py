from modules import *

class QuestionHandler(RequestHandler):
    '''when user scrolls down to the FAQ section an ajax request to the get method for welcoming the user
       also when te user scolls then the text welcoming the user must be dynamically deleted
    '''
    
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        #self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
    
    
    @coroutine
    @removeslash
    def get(self):
        question=self.get_argument('question')         
   
        print question
        sentence=TextBlob(question,analyzer=NaiveBayesAnalyzer())
        sentence1=TextBlob(question)
        if question=="hello" or question=="hi":
			response="Hey there! How are you?"
        elif cl.classify(question)=='neg' and sentence1.sentiment.polarity==0 and detect(str(sentence1.correct()))!="en":
			response='Language please'
        elif sentence.sentiment.p_pos<0.4:
			response='Can I help you with some thing'
        else:
			response = chatbot.get_response(question)
        #print 'response',response   Dont use print commands when the app is in production 
        '''
        Print the response based upon the training
        '''
        jsonData = {
        'status' : 200,
        'message' : "OK"
        'answer' : response
        }
        self.write(jsonData)
    def write_error(self,status_code,**kwargs):
        jsonData = {
        'status' : int(status_code),
        'message' : "Internal server error",
        'answer' : 'NULL'
        }
        self.write(jsonData)
    def options(self):
        self.set_status(204)
        self.finish()
    
