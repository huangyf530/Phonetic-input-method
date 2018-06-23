# -*- coding:utf-8 -*-
import pickle
import json
import re

character_num = {}
character_table = {}
count = 0

with open("Frequency.pickle", 'rb') as d:
    character_num = pickle.load(d)
with open("Character.pickle", 'rb') as d:
    character_table = pickle.load(d)
for pinyin in character_table:
    character_num[pinyin] = 0
    for i in range(1, len(character_table[pinyin])):
        if character_table[pinyin][i] in character_num:
            character_num[pinyin] += character_num[character_table[pinyin][i]]
    print("%s : %d" % (pinyin, character_num[pinyin]))
with open("AllFrequency.pickle", 'wb') as d:
    pickle.dump(character_num, d, pickle.HIGHEST_PROTOCOL)