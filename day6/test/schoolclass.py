#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

class SchoolMem(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def enroll(self):
        print("member %s is enrolled!" % self.name)

