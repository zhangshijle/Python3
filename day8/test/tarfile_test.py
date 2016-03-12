#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  os
import  tarfile

tar = tarfile.open("/tmp/tartest.tar.gz","w:gz")
for root,dir,files in os.walk("/var/log/"):
    #print(root,"root")  #目录
    #print(dir,"dir")
    #print(files,"files") #每个目录的文件,不包括目录

    for file in files:
        fullpath = os.path.join(root,file) #取出每个文件的完整路径
        print(fullpath)
        tar.add(fullpath) #将每个文件添加到tar实例
tar.close() #文件循环完以后关闭实例

