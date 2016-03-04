#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  shelve
d = shelve.open("shelve.txt")
class Test(object):
    def __init__(self,n):
        self.n = n

t1 = Test(123)
t2 = Test(234)

name = ["jack","tom"]

d["t1"] = t1
d["t2"] = t2
d.close()
