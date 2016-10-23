from modules import *

class QuestionHandler(RequestHandler):
    
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        #self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
    
    
    @coroutine
    @removeslash
    def get(self):
        #extract response
        question=self.get_argument('question')         
        '''
        Check comments for different ways to tweak the bot
        sentence=TextBlob(question,analyzer=NaiveBayesAnalyzer())
        '''
        sentence1=TextBlob(question)
        if question=="hello" or question=="hi":
            response="Hey there! How are you?"
            '''
            You can use custom classifiers to detect bad language ex:
            elif cl.classify(question)=='neg':
                response='good words appreciated'
            '''
            '''
            for knowing that whether it is english that is being spoken
            this part is not very accurate you can use google api to configure
            and then remove this part
            '''
        elif sentence1.sentiment.polarity==0 and detect(str(sentence1.correct()))!="en":
            response='Language please'  
        
            
            '''
            You can have custom data set of responses based on the mood of the person 
            for more information check the TextBlob documentation ex:
            elif sentence.sentiment.p_pos<0.4:
                response='Can I help you with some thing'            
            '''
        else:
            response = chatbot.get_response(question)       

        '''
        Return the response based upon the training
        '''
        jsonData = {
        'status' : 200,
        'message' : "OK",
        'answer' : str(response)
        }
        jsonData=json.dumps(jsonData)
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
    
