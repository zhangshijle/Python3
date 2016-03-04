#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

#经典类:广度优先,python 2是深度优先
#新式类:深度优先,python 3全部是广度优先,

import  time

class A:
    n = "A"
    def f2(self):
        print("f2 from A")
class B(A):
    n = "B"
    def f1(self):
        print("from B")
    #def f2(self):
    #    print("f2 from B")

class C(A):
    n = "C"
    def f2(self):
        print("from C")
class D(B,C):
    """这是一个注释"""
    def __del__(self):
        print("删除中...")

    pass

d = D()
d.f2()
d.f2()
print(d.__doc__)
print(d.)
time.sleep(1)