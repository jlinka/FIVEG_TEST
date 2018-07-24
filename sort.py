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
dicFile = open('tfidf4.txt', 'r+', encoding='UTF-8-sig', errors='ignore')#打开数据
txtDict = {}#建立字典
while True:
    line = dicFile.readline()
    if line == '':
        break
    index = line.find(':')
    key = line[:index]
    #line[index:] = str(line[index:]).lstrip('\n').rstrip(':')
    #value = float(line[index:])
    value = line[index:]
    txtDict[key] = value.lstrip(":").rstrip()#加入字典

dicFile.close()
# print(txtDict)


        # print(txtDict.get())
        # print(txtDict[key])
for key in txtDict.keys():
    # print(value)
    print(key)
    data = {'word': key, 'freq': float(txtDict[key])}
    db1.tfidf.insert(data)




