#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
'''
import  pickle

f = open("data.txt","rb")
a = pickle.loads(f.readline())

print(a)
f.close()
'''
import  json
readjson = json.load(open("data.json"))
print(readjson)