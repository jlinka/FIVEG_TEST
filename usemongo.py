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

collection1 = db1.word_list

num = 1
splitfilename = "split_text/split" + str(num) + ".txt"
splitfreqname = "text_freq/freq_text" + str(num) + ".txt"
word_lst = []
word_dict = {}
while os.path.exists(splitfilename):
    word_lst = []
    word = ""
    with open(splitfilename, 'r+', encoding='UTF-8-sig', errors='ignore') as wf:
        word = wf.read().replace('\r', '').replace('\n', '').replace(' ', '').replace('  ', '').replace('   ', '')\
        .replace('    ', '').replace('     ', '').replace('      ', '').replace('       ', '').replace('        ', '')\
        .replace('         ', '').replace('          ', '').replace('\r\n            \r\n              \r\n    \r\n    '
                                                                    '        \r\n           \r\n    ', '')\
        .replace('\r\n                         \r\n                              \r\n                                '
                 '   ', '').replace('	', '').replace(' ', '').replace('http:', '').replace(':', '')
        print(word)
        word_lst.append(word.split(','))
        for item in word_lst:
            for item2 in item:
                if item2 not in word_dict:
                    word_dict[item2] = 1
                else:
                    word_dict[item2] += 1
        num += 1
        splitfilename = "split_text/split" + str(num) + ".txt"
        # word_dict.plot(10)
with open('test6.txt', 'w', encoding='UTF-8-sig') as wf2:
        # sorted_key_list = sorted(word_dict, key=lambda x: word_dict[x])
        # sorted_dict = map(lambda x: {x: word_dict[x]}, sorted_key_list)
    for key in word_dict:
        if key != "":
            data = {'word': key, 'freq': word_dict[key]}
            db1.word_list.insert(data)
            #print(key, sorted_dict[key])
            #wf2.write(key + ':' + str(word_dict[key]) + '\n')


