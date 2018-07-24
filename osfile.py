# -*-coding:utf-8-*-
from pymongo import MongoClient
from aip import AipNlp
import json
import time
import datetime
""" 你的 APPID AK SK """
APP_ID = '11508916'
API_KEY = 'FegRIyeMcFxmrbp0435XjPGW'
SECRET_KEY = 'm9hO7Nu9qgf3SvrAsfvZrv9ETZMlHkGO'

client_AipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

#建立MongoDB数据库连接
client = MongoClient('localhost', 27017)

#连接所需数据库,test为数据库名
db = client.FiveG_news
#连接所用集合，也就是我们通常所说的表，test为表名
collection = db.xinChuang_topic

#接下里就可以用collection来完成对数据库表的一些操作

#查找集合中所有数据

starttime = datetime.datetime.now()
c = []
num = 1
myquery = {"isLimitSource": 1}
input = open('score6.docx', 'a', encoding='utf-8', errors='ignore')
a = collection.find(myquery).sort("score_new", -1)
for item in a:
    c.append(item['content'])
    input.write("第" + str(num) + "个" + '           ' + "相关度：" + str(item['score_new']) + '\n')
    input.write('标题:'+item['title']+'\n')
    input.write('正文内容:')
    for i in c:

        #print(i + ",")
        a = "".join(i).replace('\r', '').replace('\n', '').replace(' ', '').replace('  ', '').replace('   ', '') \
            .replace('    ', '').replace('     ', '').replace('      ', '').replace('       ', '').replace('        ',
                                                                                                           '') \
            .replace('         ', '').replace('          ', '').replace(
            '\r\n            \r\n              \r\n    \r\n    '
            '        \r\n           \r\n    ', '') \
            .replace(
            '\r\n                         \r\n                              \r\n                                '
            '   ', '').replace('	', '').replace('　　', '').replace('', '').replace('　　 ', '')

    #print(c)
    num += 1
    input.write(a + '\n\n\n\n\n\n\n\n\n\n')

input.close()