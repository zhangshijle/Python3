#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

#class Animal(object): #新式类,和经典类的底层实现是不一样的,比如多继承

class Animal: #经典类
    count = 10
    def __init__(self,name):
        self.name = name
        #self.num = None
        self.__num = None #私有属性,对外部隐藏不可见,内部访问加__即可

    hobbile = "xxx"

    @classmethod #类方法,不能访问实例变量
    def talk(self):
        print("%s is talking...." % self.hobbile)

    @staticmethod #静态方法,不能访问类变量和实例变量
    def walk():
        print("%s us tailking")

    @property  #把方法变成属性,调用的时候不用加括号调用
    def habit(self):
        print("%s habit is  xxoo" % self.name)

    @property #把方法变成属性,调用的时候不用加括号调用
    def total_players(self):
        return  self.name

    @total_players.setter
    def total_players(self,__num):
        self.__num = __num
        print("total num is :",self.__num)
        print("total players:",self.name)

    @total_players.deleter
    def total_players(self):
        print("total player got deleted.")
        del self.__num

d = Animal("yy")
print(d.total_players)
d.total_players = 5
#del d.total_players
#print(d.total_players)