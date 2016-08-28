#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  os
import  sys
sdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sdir)




def test2():
    print("test2")

from s1 import  test
test()

