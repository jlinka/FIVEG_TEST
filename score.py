# -*-coding:utf-8-*-
from pymongo import MongoClient
from aip import AipNlp
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

collection1 = db1.xinChuang_topic

starttime = datetime.datetime.now()

num = 21
tf_all = 0
tf = 0

splitfilename = "split_Freq_Final/split_Final"+str(num) + ".txt"
while os.path.exists(splitfilename):
    word_keys = []
    word_dict = {}
    word = ""
    impwords = impwordslist('5G_imp.txt')  # 这里加载关键词词的路径
    myquery = {"isLimitSource": 1}
    for item in collection1.find(myquery):
        with open(splitfilename, 'r+', encoding='UTF-8-sig', errors='ignore') as wf:
            for word in wf:
                v = word.strip().split(':')
                word = word.split(":")
                tf_all += int(word[1])
                word_dict[v[0]] = v[1]
                word_keys.append(v[0])
                if word[0] in impwords:
                    tf += int(word[1])
            score = tf/tf_all
            print(score)






endtime = datetime.datetime.now()
print(endtime - starttime)
