#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
from  module import  C
obj = C() #自动执行类中的__init__方法
print(obj.__module__) #显示当前正在操作的模块名称
print(obj.__class__) #显示当前操作的对象的类是什么
print(obj.__doc__) #显示帮助文档
obj.__del__()
print(obj.__dict__,"类成员")