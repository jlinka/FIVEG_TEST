# -*-coding:utf-8-*-
from pymongo import MongoClient
from aip import AipNlp
from decimal import Decimal
import json
import time
import datetime
import os
""" 你的 APPID AK SK """
APP_ID = '11508916'
API_KEY = 'FegRIyeMcFxmrbp0435XjPGW'
SECRET_KEY = 'm9hO7Nu9qgf3SvrAsfvZrv9ETZMlHkGO'

client_AipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def impwordslist(filepath):
    impwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return impwords


client = MongoClient('localhost', 27017)


db1 = client.FiveG_news

collection1 = db1.tfidf
num = 1
tfidffilename = "tfidf2/tfidf" + str(num) + ".txt"
tfidffilename1 = "tfidf3/tfidf" + str(num) + ".txt"


while os.path.exists(tfidffilename):
    db1.tfidf.remove({})
    dicFile = open(tfidffilename, 'r+', encoding='UTF-8-sig', errors='ignore')#打开数据
    txtDict = {}#建立字典
    while True:
        line = dicFile.readline()
        if line == '':
            break
        index = line.find(':')
        key = line[:index]
        value = line[index:]
        txtDict[key] = value.lstrip(":").rstrip()#加入字典

    dicFile.close()

    for key in txtDict.keys():
        # print(value)
        print(key)
        data = {'word': key, 'freq': float(txtDict[key])}
        db1.tfidf.insert(data)
    with open(tfidffilename1, 'w', encoding='UTF-8-sig') as wf2:
        for item in collection1.find().sort([("freq", -1)]):
            wf2.write(str(item['word']) + ':' + str(item['freq']) + '\n')
    num += 1
    tfidffilename = "tfidf2/tfidf" + str(num) + ".txt"
    tfidffilename1 = "tfidf3/tfidf" + str(num) + ".txt"



