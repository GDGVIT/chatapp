import csv
#name=raw_input("name:")
#email=raw_input("email:")
#feedback=raw_input("feedback:")
'''with open("feddback1.csv","r") as csvfile:
    readCSV=csv.reader(csvfile)
    for row in readCSV:
        print row
csvfile.close()
'''
#with open("feddback1.csv",'rw') as csvfile:
#   text=csvfile.readlines()
#   writeCSV=csv.writer(csvfile)
    

'''with open("hi.csv","rw+") as csvfile:
    text=csvfile.readlines()    
    with open("hitrain.csv","rw+") as cpyfile:
        writeCSV=csv.writer(cpyfile)
    
        for line in text:
            writeCSV.writerow([line,'neg'])
    cpyfile.close()
csvfile.close()
'''
from textblob.classifiers import NaiveBayesClassifier
with open('hitrain.csv','r') as fp:
	cl=NaiveBayesClassifier(fp,format="csv")
print(cl.classify("tu kutta"))
