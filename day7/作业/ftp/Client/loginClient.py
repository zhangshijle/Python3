#!/usr/bin/env python
# -*- coding:utf-8 -*-


import getpass,json,sys,hashlib

def loginClient(sk):
    '''
    登录，验证密码三次错误，锁定账号。输入用户名，密码。socket请求server端验证，输入三次错误，用户锁定。
    用户为eva，密码是 123456，已加密
    '''
    while True:

        user = input('请输入用户名以登录：')
        #password = getpass.getpass('请输入密码或输入"0"退出：')
        password =  input('请输入密码或输入"0"退出：')
        if password and user:
            #hash = hashlib.md5(password)
            #hash.update('admin')
            #pwdMd5 = hash.hexdigest()
            loginInfo = {'request':'login','user':user,'password':pwdMd5}

            jloginInfo = json.dumps(loginInfo)
            sk.sendall(jloginInfo)
            loginRe = sk.recv(1024)
            print(loginRe)

            if loginRe == '1':
                print('登录成功，欢迎您使用ftp服务')
                return 1
            elif loginRe == '2':
                print('对不起，您输入的密码有误，用户名将在输入三次错误后被锁定')
            else:
                print('对不起，您输入的用户不可用（不存在或已被锁定）')
        else:
            return 0

