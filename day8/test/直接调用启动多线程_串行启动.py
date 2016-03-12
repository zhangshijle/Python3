#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  threading
import  time

def sayhi(num):
    print("running on number: %s"% num)
    time.sleep(3)

if __name__ == "__main__":
    t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例,不写逗号会被打当成一个独立的元组
    t2 = threading.Thread(target=sayhi,args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join() #等待线程运行之后再继续执行
    print("_____>")