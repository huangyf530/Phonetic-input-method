# -*- coding:utf-8 -*-
import pickle
import json
import re

total_character_num = {}
now_character_num = {}
count = 0

def dealMaterial(str):
    global count
    regex_str = "[\u4e00-\u9fa5]"
    sentences = re.split(r'[a-zA-Z0-9，。/《》？；’‘：“”【】{}、—（）&*…%￥#@！~·.,?:;"\'\\|\[\]+_\-\s ()$!^`]*', str)
    for sentence in sentences:
        if sentence == '' :
            continue
        count = count + 1
        print("the %d sentence : %s" % (count, sentence))
        for i in range(len(sentence)):
            if sentence[i] not in now_character_num:
                now_character_num[sentence[i]] = 1
            now_character_num[sentence[i]] = now_character_num[sentence[i]] + 1
            if i != (len(sentence) - 1):
                if sentence[i] + sentence[i + 1] not in now_character_num:
                    now_character_num[sentence[i] + sentence[i + 1]] = 1
                now_character_num[sentence[i] + sentence[i + 1]] = now_character_num[sentence[i] + sentence[i + 1]] + 1


def dealContent(content):
    data = json.loads(content)
    dealMaterial(data['html'])
    dealMaterial(data['title'])


def Initial_Probability():
    global character_num
    str1 = '拼音输入法作业/sina_news/2016-'
    str2 = '.txt'
    for i in range(1, 12):
        if i < 10:
            string = str1 + str(0) + str(i) + str2
        else:
            string = str1 + str(i) + str2
        print(string)
        with open(string, 'r', encoding='utf-8') as f:
            for (linenum, content) in enumerate(f):
                dealContent(content)


Initial_Probability()
with open('Frequency.pickle', 'wb') as d:
    pickle.dump(now_character_num, d, pickle.HIGHEST_PROTOCOL)
print("Initial 2016-01.txt OK!")
#the 69136693 sentence