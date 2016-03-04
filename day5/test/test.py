#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie


'''
data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
for j in  range(1,len(data)-2):
    for i in range(len(data)-j):
        if data[i] > data[i+1]:
            tmp = data[i+1]
            data[i+1] = data[i]
            data[i] = tmp
print(data)

'''

#
# import  time
# import  datetime
# print(time.clock())
# print(time.process_time()) #返回处理器执行程序的时间
# print(time.time()) #1970年以后的时间戳
# print(time.ctime(),"输出Sat Jan 30 18:19:15 2016,当前系统时间")
# print(time.ctime(time.time()-86400),"将时间减去一天")
# print(time.gmtime(time.time()-8400),"将时间戳转换成struct_time格式,并将时间减一天")
# print(time.localtime(time.time()-86400),"将时间戳转换成struct_time格式,但返回的是吧恩地时间")


'''
import random
print(random.random())
print(random.randint(1,20))
'''

'''
def search(data,n):
    mid = int(len(data)/2)
    if len(data) > 1:
        if data[mid] > n: #数据在另一半
            print("要查找的 %s 在左侧" % data[mid])
            search(data[:mid],n) #转换成实参
            print(mid)
        elif data[mid] < n: #数据在这一半
            print("要查找的%s 在这一伴儿" % data[mid])
            search(data[mid:],n)
            print(mid)
        else:
            print("找到了%s" % data[mid])
    else:
        print("找不到")

if __name__ == "__main__":
    data = list(range(6000000))
    search(data,1)

'''
'''
def search(data,n):
    mid = int(len(data)/2)
    if len(data) >=  1 :
        if data[mid] > n:
            print("要查找的%s 在左侧" % data[mid])
            search(data[:mid],n)
            #print(mid)
        elif data[mid] < n:
            print("要查找的 %s在右侧" % data[mid])
            search(data[mid:],n)
            #print(mid)
        else:
            print("找到了%s" % n)
    else:
        print("找不到了%s " % n)


if __name__ == "__main__":
    data = list(range(100000))
    search(data,13560)
'''
'''
def search(data,n):
    mid = int(len(data)/2)
    if len(data) >= 1:
        if data[mid] > n:
            print("要查找的%s 在左侧" % data[mid])
            search(data[:mid],n)
        elif data[mid] < n:
            print("要查找的 %s在右侧" % data[mid])
            search(data[mid:],n)
        else:
            print("找打了 %s" % n)

    else:
        print("再也找不到了~~")
if __name__ == "__main__":
    data = list(range(10000))
    search(data,1230)
'''



def  search(data,n):
    mid = int(len(data)/2)
    if data[mid] >=1 :
        if data[mid] > n:
            search(data[:mid],n)
        elif data[mid] < n:
            search(data[mid:],n)
        else:
            print("找到了%s" %n)
    else:
        print("zhaobudaol")

if __name__ == "__main__":
    data = list(range(100000))
    search(data,1235)


import  sys
print(sys.path)











