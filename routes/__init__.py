from controllers import *

route=[
	(
		r"/faq",
		chat.QuestionHandler
	
	),
	(
		r"/register",
		Register.RegisterHandler
	
	),
	(
		r"/welcome",
		Welcome.WelcomeHandler
	
	)
]
