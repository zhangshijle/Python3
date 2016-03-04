#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie


'''

import  sys
import  time
for i in range(10):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.3)
'''

'''
import pickle
data = [123123453454456,{"K1":""},{"K2":"K3"}]
with  open("data.txt","wb") as file1:
    pickle.dump(data,file1) #dunp是直接将文件dump到文件当中,和dumps方法不一样
    file1.write(pickle.dumps(data)) #需要用文件的写入方式将序列化以后的数据写入到文件,和dumo写入文件的方法不同


'''

'''
import   json
data = "123123453454456abcd"
with open("data.json","w") as f:
    json.dump(data,f) #使用dump方法将data写入到打开的文件
    #f.write(json.dumps(data))
    f.close()
    '''

import  shelve
d = shelve.open("shelve.txt")
class Test(object):
    def __init__(self,n):
        self.n = n

t1 = Test(123)
t2 = Test(234)

name = ["jack","tom"]

d["t1"] = t1
d["t2"] = t2
d.close()
