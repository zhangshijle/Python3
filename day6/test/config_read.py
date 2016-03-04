#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie


import  configparser
config = configparser.ConfigParser()
for i in config:
    print(i,"--->")
print('jack.com' in config) #判断一个主机区域是否在配置文件内部

print(config.sections()) #列表的内容
print(config.read('example.ini'))  #读取到文件名
print(config.sections()) #文件中的主机块内容
print(config['jack.com']['user'])  #读取指定数据

