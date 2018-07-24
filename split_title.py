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
myquery = {"isLimitSource": 1}
for item in collection.find(myquery):
    c.append(item['title'])
    #c.append("。")
    #c.append(item['content'])
    print("\n")
    #data = client.lexer(c)
num = 1
#print(c)
splitfilename = "split_title/split"+str(num) + ".txt"
for i in c:
    input = open(splitfilename, 'a', encoding='utf-8', errors='ignore')
    print("第几个文件" + str(num))
    print(i+",")
    a = "".join(i).replace('\r', '').replace('\n', '').replace(' ', '').replace('  ', '').replace('   ', '')\
        .replace('    ', '').replace('     ', '').replace('      ', '').replace('       ', '').replace('        ', '')\
        .replace('         ', '').replace('          ', '').replace('\r\n            \r\n              \r\n    \r\n    '
                                                                    '        \r\n           \r\n    ', '')\
        .replace('\r\n                         \r\n                              \r\n                                '
                 '   ', '').replace('	', '').replace('　　', '').replace('', '').replace('　　 ', '')
    #a = json.dumps(a)
    #print(a)

    time.sleep(1)
    data = client_AipNlp.lexerCustom(a)
    stopwords = stopwordslist('stop_words.txt')  # 这里加载停用词的路径
    print(data)
    if 'items' in data:
        list = data['items']
        for item in list:
            # print(item)
            if(item['item']) not in stopwords:
                input.write(item['item'] + ',')
                print(item['item'], item['pos'])
    num += 1
    splitfilename = "split_title/split" + str(num) + ".txt"
    input.close()
endtime = datetime.datetime.now()
print(endtime - starttime)