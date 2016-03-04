#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

'''
import logging

logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %D:%H:%S',level=logging.INFO) #在其级别高的才会显示
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")

'''


import  logging
#类的实例,全局的级别,日志实例
logger =  logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

#输出在屏幕的设定的信息级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#写入在文件设定的信息级别
fh = logging.FileHandler("access.log")
fh.setLevel(logging.INFO)

#创建日志格式
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#添加格式到屏幕和文件的方法
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#将文件设置和屏幕设置添加到logger,即和将信息进行输出和写入到文件
logger.addHandler(ch)
logger.addHandler(fh)


#应用
logger.debug("debug message")
logger.info("debug message")
logger.warn("debug message")
logger.error("debug message")
logger.critical("debug message")
