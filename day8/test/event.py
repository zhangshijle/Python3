#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  threading,time,random

def light():
    if not  event.isSet():
        event.set() #设置为绿灯
    count = 0
    while True:
        if count < 10:
            print("\033[42;1m=====绿灯=====\033[0m")
        elif count < 13:
            print("\033[43;1m======黄灯======\033[0m")
        elif count < 20:
            if event.isSet():
                event.clear()
            print("\033[44;0m=======红灯=====\033[0m")
        else:
            count = 0
            event.set()
        time.sleep(1)
        count += 1

def car(n):
    while True:
        time.sleep(random.randrange(12))
        if event.isSet(): #lvdeg
            print("car %s is runing" % n)
        else:
            print("car %s is wating for the red light" % n)





if __name__ == "__main__":
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=[i,])
        t.start()