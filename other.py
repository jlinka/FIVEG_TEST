# -*-coding:utf-8-*-
import codecs
import os

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
                #print(key, sorted_dict[key])
            wf2.write(key + ':' + str(word_dict[key]) + '\n')