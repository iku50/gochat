# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:09:04 2023

@author: 13015
"""
from snownlp.__init__ import SnowNLP
def last_line(file_path):
    with open(file_path, 'rb') as f:
        f.seek(-2, 2)
        while f.read(1) != b'\n':
            f.seek(-2, 1)
        last_line = f.readline().decode()
    return last_line

f=open('favor.txt','r+',encoding='utf-8')
fav=float(f.readline())
#print(fav)
ll=last_line('test.txt')
s=SnowNLP(ll)
fav=str((fav+s.sentiments)/2)
f.seek(0)
f.write(fav)
#print(type(ll))
f.close()