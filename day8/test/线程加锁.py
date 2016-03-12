#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  threading
import  time


def addNum():
    global num
    print("--get num:",num)
    time.sleep(1)
    lock.acquire()
    #time.sleep(1)
    num -= 1
    lock.release()

num = 100
thread_list = []
lock = threading.Lock()

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)
    print(len(thread_list),"--->")
for i in thread_list: #等待所有线程执行完毕
    i.join()
print(num)



