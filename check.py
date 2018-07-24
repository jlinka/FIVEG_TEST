from pymongo import MongoClient
import os
client = MongoClient('localhost', 27017)
db1 = client.FiveG_news
collection1 = db1.tfidf
with open('tfidf.txt', 'w', encoding='UTF-8-sig') as wf2:
    for item in collection1.find().sort([("freq", -1)]):
        wf2.write(str(item['word']) + ':' + str(item['freq']) + '\n')