# -*- coding:utf-8 -*-
sf = open('output.txt','r',encoding="utf-8")
cf = open('ans.txt','r')
d =[]
c = []
for line in sf:
    d.append(line)
for line in cf:
    c.append(line)
g = 0
z = 0
for i in (range(len(c))):
    if c[i] == d[i]:
        g = g+1
    for k in range(len(c[i])):
        if((c[i][k]==d[i][k])&(c[i][k]!='\n')):
            z = z+1
print(z/7471)
print(g/789)