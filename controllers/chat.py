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
        if cl.classify(question)=='neg' and sentence1.sentiment.polarity==0 and detect(question)!="en":
			response='You are what you think of and use decent English please'
        elif sentence.sentiment.p_pos<0.4:
			response='Can I help you with some thing'
        else:
			response = chatbot.get_response(question)
        print 'response',response   
        '''
        Print the response based upon the training
        '''
        self.write('{"status":"200","message":%s,"answer":%s}'%(self._reason,response))
    def write_error(self,status_code,**kwargs):
        self.write('{"status":%s,"message":%s,"answer":"null"}'%(status_code,self._reason))
    def options(self):
        self.set_status(204)
        self.finish()
    
