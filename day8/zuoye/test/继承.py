#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

class Old_class:
    def __init__(self,name):
        self.name = name
    def func1(self):
        print("%s from  Old_class" % self.name)
test = Old_class("jack")
test.func1()


class New_class(object):
    def __init__(self,name):
        self.name = name
    def func1(self):
        print("%s from  New_class" % self.name)
test2 = New_class("tom")
test2.func1()
