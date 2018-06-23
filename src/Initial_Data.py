# -*- coding:utf-8 -*-
import pickle


pinin_to_cha_map = {}
character_num = {}


def dealContent(c):
    global pinin_to_cha_map
    line = c.split()
    pinin_to_cha_map[line[0]] = line


def Initial_PinyitoCha():
    global pinin_to_cha_map
    with open('拼音输入法作业/拼音汉字表_12710172/拼音汉字表.txt', 'r', encoding='gbk') as f:
        for (linenum, cotent) in enumerate(f):
            dealContent(cotent)
    with open('Character.pickle', 'wb') as d:
        pickle.dump(pinin_to_cha_map,d, pickle.HIGHEST_PROTOCOL)
    print("Initial Character Table OK!")








with open('Character.pickle', 'rb') as f:
    pin = pickle.load(f)
print (pin['wo'])