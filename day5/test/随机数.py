#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  pickle,json

info = {
    "jack":"IT",
    "tom":"ChuShi",
}

f = open("user_acc.txt","wb")

f.write(pickle.dumps(info))
f.close()

