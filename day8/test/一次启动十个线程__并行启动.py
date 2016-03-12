#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  threading
import  time
'''
def sayhi(num):
    print("running on number: %s"% num)
    time.sleep(3)

if __name__ == "__main__":
    t_list = []
    for i in range(10):
        t = threading.Thread(target=sayhi,args=[i,]) #中括号里面加逗号表示是一个列表或元组
        t.start()
        t_list.append(t) #每启动一个将线程附加到列表
    for j in t_list:
        j.join() #循环列表并等待
    print("---->")
'''

import  threading,time
def hihi(num):
    print("running on number: %s" % num)
    time.sleep(3)
if __name__ == "__main__":
    list1 = []
    for i in range(10):
        t = threading.Thread(target=hihi,args=[i,])
        t.start()
        list1.append(t) #附加所有的线程到列表
    for j in list1:  #循环所有的线程等待一次
        j.join() #在没有守护线程的时候使用,如果主线程被设置为守护线程则join就无效了
        print("==>") #循环list1,
    print("--->")