#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import   configparser
config = configparser.ConfigParser()
config['DEFAULTS'] = {'ServerAliveInterval':'45',
                    'Compression':'yes',
                    'CompressionLevel':'9'}

config['jack.com'] = {}
config['jack.com']['user'] = 'Jack'
config['jack.com']['password'] = '123456'

config['tom.com'] = {}
topsecret = config['tom.com'] #实例化config对象,和上面的功能是一样的
topsecret['HostPort'] = '51200'
topsecret['ForwardX11'] = 'no'
config['DEFAULTS']['ForwardX11'] = 'yes'


with open('example.ini', 'w') as configfile:
   config.write(configfile)