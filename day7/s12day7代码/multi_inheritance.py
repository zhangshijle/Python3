#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
class A(object):
    n = 'A'
    def f2(self):
        print("f2 from A")
class B(A):
    n = 'B'
    def f1(self):
        print("from B")
    #def f2(self):
    #    print("f2 from B")
class C(A):
    n = 'C'
    def f2(self):
        print("from C")
class D(B,C):
    '''Test class'''

    def __del__(self):
        print("deleteing the ...")

d = D()
d.f1()
d.f2()
d.__del__()
time.sleep(2)
print(d.n)
print('hahah')
#print(d.__module__)