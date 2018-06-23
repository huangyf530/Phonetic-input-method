# -*- coding:utf-8 -*-
import pickle
import sys


inputfile = sys.argv[1]
outputfile = sys.argv[2]
character_num = {}
character_table = {}
file_content = []
pin_yin = []
outfile = open(outputfile, 'w', encoding='utf-8')

def GetContent():
    global pin_yin, file_content
    with open(inputfile, 'r') as f:
        file_content = f.readlines()


def GetPinyin(linenum):
    global pin_yin, file_content
    pin_yin = file_content[linenum].split()


def Smooth(rate1, rate2):
    a = 0.99999 * rate1 + 0.00001 * rate2
    return a


def getLinkValue(a, b, pinyin):
    global character_num
    rate1 = 0
    if a == "<start>":
        rate1 = character_num[b] / character_num[pinyin]
    else:
        if a + b in character_num:
            rate1 = character_num[a + b]/character_num[a]
    rate2 = character_num[b] / character_num[pinyin]
    return Smooth(rate1, rate2)


def PrintToFile(ans):
    global outfile
    outfile.write(ans + '\n')

#动态规划算法思想参照何家傲同学的讲解
def Dpsearch():
    global pin_yin, character_num, character_table
    n = len(pin_yin)
    f = []
    dict = {}
    dict['<start>'] = {'val': 1}
    f.append(dict.copy())
    dict.clear()
    for i in range(1, n + 1):
        f.append({})
        for j in character_table[pin_yin[i - 1]]:
            if j in character_num and j != pin_yin[i - 1]:
                f[i][j] = {'val': 0, 'from': 0}
                for k in f[i - 1]:
                    temp = f[i - 1][k]['val'] * getLinkValue(k, j, pin_yin[i - 1])
                    if temp > f[i][j]['val']:
                        f[i][j]['val'] = temp
                        f[i][j]['from'] = k
    answer = ''
    temp = -10000
    last_word = ''
    for word in f[n]:
        if f[n][word]['val'] > temp:
            last_word = word
            temp = f[n][word]['val']
    for count in range(n, 0, -1):
        answer = last_word + answer
        last_word = f[count][last_word]['from']
    print(answer)
    PrintToFile(answer)


with open("AllFrequency.pickle", 'rb') as d:
    character_num = pickle.load(d)
with open("Character.pickle", 'rb') as d:
    character_table = pickle.load(d)
GetContent()
for i in range(len(file_content)):
    GetPinyin(i)
    Dpsearch()
outfile.close()

#0.7601392049257127
#0.2674271229404309

