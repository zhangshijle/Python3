#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

class Role(object):
    ac= None  #类的熟悉,是公共的
    def __init__(self,name,role,weapon,life_value): #self是实例本身,谁调用类,self就是谁
        self.name = name  #成员变量,成员属性,是类自己的
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def buy_weapon(self,weapon):
        print("%s正在采购 %s" %(self.name,weapon))
        #self.weapon = weapon

p1 = Role("警察","poloce","B10",100) #将类实例化,这里p1就是def __init__后面的self
p1.buy_weapon("AK47") #执行函数

t1 = Role("劫匪","terrorist","B11",100)
t1.buy_weapon("BB45")