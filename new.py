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

num = 1
tf_all1 = 0
tf1 = 0
tf_all2 = 0
tf2 = 0
impwords = impwordslist('5G_imp.txt')  # 这里加载关键词词的路径
myquery = {"isLimitSource": 1}

splitfilename = "split_Freq_/split_Final"+str(num) + ".txt"
text_freq = "text_freq/freq_text" + str(num) + ".txt"
title_freq = "title_freq/freq_title" + str(num) + ".txt"
for item in collection1.find(myquery):

    print(str(num)+'\n')
    word_keys = []
    word_dict = {}
    word = ""
    tf_all1 = 0
    tf1 = 0
    tf_all2 = 0
    tf2 = 0
    while os.path.exists(text_freq):
        with open(text_freq, 'r+', encoding='UTF-8-sig', errors='ignore') as wf:
            for word in wf:
                v = word.strip().split(':')
                word = word.split(":")
                tf_all1 += int(word[1])
                word_dict[v[0]] = v[1]
                word_keys.append(v[0])
                if word[0] in impwords:
                    tf1 += int(word[1])
        word_keys = []
        word_dict = {}
        while os.path.exists(title_freq):
            with open(title_freq, 'r+', encoding='UTF-8-sig', errors='ignore') as wf:
                for word in wf:
                    v = word.strip().split(':')
                    word = word.split(":")
                    tf_all2 += int(word[1])
                    word_dict[v[0]] = v[1]
                    word_keys.append(v[0])
                    if word[0] in impwords:
                        tf2 += int(word[1])
                break
        score1 = tf1/tf_all1
        score2 = (tf2/tf_all2)*5
        score = score1 + score2
        print(score)

        newvalues = {"$set": {"score_new": score}}

        db1.xinChuang_topic.update(item, newvalues)
        break
    num += 1
    text_freq = "text_freq/freq_text" + str(num) + ".txt"
    title_freq = "title_freq/freq_title" + str(num) + ".txt"


