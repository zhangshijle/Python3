#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  sys
import os

sdir=os.path.dirname((os.path.abspath(__file__)))


print(sdir,"xx--")
sys.path.append(sdir)



def test():
    print("ss111")
from  modules  import  s2
s2.test2()


