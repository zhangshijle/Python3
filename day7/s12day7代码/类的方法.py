#!/usr/bin/env python
# -*- coding:utf-8 -*-
#class Animal:
class Animal(object):
    count = 10
    def __init__(self, name):    # Constructor of the class
        self.name = name
        self.__num = None
    hobbie = 'meat'
    @classmethod #类方法，不能访问实例变量
    def talk(self):
        print("%s is talking..." % self.hobbie )
    @staticmethod #静态方法，不能访问类变量及实例变量
    def walk():
        print(" is walking..." )
    @property  #把方法变成属性
    def habit(self):
        print("%s habit is xxoo" %self.name)
    @property
    def total_players(self):
        return self.__num

    @total_players.setter
    def total_players(self,num):
        self.__num = num
        print("total players:",self.__num)
    @total_players.deleter
    def total_players(self):
        print("total player got deleted.")
        del self.__num

d = Animal("Sanjiang")
print(d.total_players)
d.total_players = 3
d.__num = 9
print("OUT:",d._Animal__num) #特例访问私有变量
#del d.total_players
print(d.total_players)
