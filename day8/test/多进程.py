#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
'''
from multiprocessing import Process
from multiprocessing import Manager

import time

li = []

def foo(i):
    li.append(i)
    print('say hi',li)

for i in range(10):
    p = Process(target=foo,args=(i,))
    p.start()

print('ending',li)
'''

from  multiprocessing import Process,Pool
import time

def Foo(i):
    time.sleep(2)
    return i+100

def Bar(arg):
    print(arg)

pool = Pool(5) #创建一个进程池
#print pool.apply(Foo,(1,))#去进程池里去申请一个进程去执行Foo方法
#print pool.apply_async(func =Foo, args=(1,)).get()

for i in range(10):
    pool.apply_async(func=Foo, args=(i,),callback=Bar) #子进程的返回值会自动传给父进程中,Bar

print('end')
pool.close()
pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

#fresze_support() #在windows运行