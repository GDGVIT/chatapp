from tornado.ioloop import IOLoop,PeriodicCallback
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine
from chatterbot import ChatBot
import customTrainer
from chatterbot.trainers import ListTrainer
import os
import re
from motor import MotorClient
from  uuid import uuid4
from routes import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier
from langdetect import detect
chatbot = ChatBot(
    'GDG BOT',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
#Name of the Chat Bot
name = chatbot.name
from chatterbot.trainers import ListTrainer

chatterbot = ChatBot("Training chatbot")
chatterbot.set_trainer(ListTrainer)
db=MotorClient().chatDB
with open('hitrain.csv','r') as fp:
	cl=NaiveBayesClassifier(fp,format="csv")
