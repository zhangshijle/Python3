#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  logging
import   configparser
config = configparser.ConfigParser()
config['DEFAULTS'] = {}

config['jack.com'] = {}
config['jack.com']['Ipaddress'] = '10.211.55.205'
config['jack.com']['Port'] = '22'
config['jack.com']['User'] = 'root'
config['jack.com']['Password'] = '123456'

config['tom.com'] = {}
topsecret = config['tom.com'] #实例化config对象,和上面的功能是一样的
topsecret['Ipaddress'] = '10.211.55.206'
topsecret['Port'] = '22'
topsecret['User'] = 'root'
topsecret['Password'] = '123456'


with open('example.ini', 'w') as configfile:
   config.write(configfile)