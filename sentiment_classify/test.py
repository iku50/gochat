# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:08:53 2023

@author: 13015
"""
from snownlp import SnowNLP as hs #喜悲
from anger import SnowNLP as ag  #愤怒
from like import SnowNLP as li  #喜爱

f=open('test.txt',encoding='utf-8')
for line in f:
    
    s1=hs(line).sentiments
    s2=ag(line).sentiments
    s3=li(line).sentiments
    print(line,'\n悲喜:',s1,'\n愤怒',s2,'\n喜爱',s3,)
    s=[s1,s2,s3]
    m=max(s)
    if(m==s2):
        if(s2>0.85):
            print("怒2")
            if(s1<0.25):
                print("悲2")
            elif(s1<0.4):
                print("悲1")
            if(s3<0.25):
                print("恶2")
            elif(s3<0.4):
                print("恶1")
        elif (s2>0.65):
            print("怒1")
            if(s1<0.25):
                print("悲2")
            elif(s1<0.4):
                print("悲1")
            if(s3<0.25):
                print("恶2")
            elif(s3<0.4):
                print("恶1")
    if(m==s1):
        if(s1>0.7 ):
            print("乐2 ")
            if(s3>0.7):
                print("爱2")
            elif(s3>0.6):
                print("爱1")
        elif (s1>0.55):
            print("乐1 ")
            if(s3>0.7):
                print("爱2")
            elif(s3>0.6):
                print("爱1")
        if(s1<0.25):
            print("悲2")
            if(s2>0.85):
                print("怒2")
            elif (s2>0.7):
                print("怒1")
            if(s3<0.25):
                print("恶2")
            elif(s3<0.4):
                print("恶1")
        elif(s1<0.4):
            print("悲1")
            if(s2>0.85):
                print("怒2")
            elif (s2>0.7):
                print("怒1")
            if(s3<0.25):
                print("恶2")
            elif(s3<0.4):
                print("恶1")
    if(m==s3):
        if(s3>0.7):
            print("爱2")
            if(s1>0.7 ):
                print("乐2 ")
            elif (s1>0.55):
                print("乐1 ")
        elif(s3>0.6):
            print("爱1")
            if(s1>0.7 ):
                print("乐2 ")
            elif (s1>0.55):
                print("乐1 ")
    print()
    
    
    
''' if(s2>0.85):
        print("怒2")
        continue
    elif (s2>0.65):
        print("怒1")
        continue
    if(s3<0.25):
        print("恶2")
        continue
    elif(s3<0.4):
        print("恶1")
        continue
    if(s1>0.7 ):
        print("乐2 ")
        if(s3>0.7):
            print("爱2")
        elif(s3>0.6):
            print("爱1")
    elif (s1>0.55):
        print("乐1 ")
        if(s3>0.7):
            print("爱2")
        elif(s3>0.6):
            print("爱1")
    if(s1<0.25):
        print("悲2")
        if(s2>0.8):
            print("怒2")
        elif (s2>0.65):
            print("怒1")
    elif(s1<0.4):
        print("悲1")
        if(s2>0.8):
            print("怒2")
        elif (s2>0.65):
            print("怒1")'''
    