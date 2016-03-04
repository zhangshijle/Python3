#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  pickle,json


f = open("user_acc.txt","rb")
a = pickle.loads(f.read())
print(a)
f.close()

