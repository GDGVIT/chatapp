from controllers import *

route=[
	(
		r"/",
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
