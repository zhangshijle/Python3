#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jly'
import ConfigParser
import json
def login(user,password):
    '''
    登录功能。
    验证密码三次错误或用户名输入错误直接返回0
    登录成功返回1并将文件中登录次数置写0
    密码错误返回2并记录登录次数
    '''
    cf = ConfigParser.ConfigParser()
    cf.read("simulateDB.cfg")
    jusrinfo = cf.get('user','usrinfo')
    usrinfo = json.loads(jusrinfo)
    authority = 0
    role = 0
    if usrinfo['user'] == user and usrinfo['times'] < 3:
        if usrinfo['password'] == password:
            usrinfo['times'] = 0
            flag = 1
        else:
            usrinfo['times'] += 1
            flag = 2
    else:
        flag = 0
    if flag:
        jcardfloatinfo = json.dumps(usrinfo)
        cf.set('user','usrinfo',jcardfloatinfo)
        cf.write(open('simulateDB.cfg', "w"))
        if flag == 1:
            jroleinfo = cf.get('role','roleinfo')
            print jroleinfo
            roleinfo = json.loads(jroleinfo)
            for key in roleinfo:
                if user in roleinfo[key]:
                    role = key
                    print role
                    authority = cf.get('authority',role)
                    break
    return str(flag),role,authority
