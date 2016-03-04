#!/usr/bin/env python
# -*- coding:utf-8 -*-


import hashlib
class userServer(object):
    '''
        server端用户的基类，继承自object，其中初始化了用户对象的用户名、角色、权限、socket连接句柄、和当前所在目录等属性
        封装了文件md5加密的静态方法。
    '''
    def __init__(self,name,role,Authdir,conn):
        self.name = name
        self.role = role
        self.Authdir = Authdir
        self.conn = conn
        self.currentDir = Authdir

    @staticmethod
    def GetFileMd5(strFile):
        '''对文件进行md5加密'''
        file = None
        strMd5 = ""
        try:
            file = open(strFile, "rb")
            md5 = hashlib.md5()
            while True:
                strRead = file.read(2048)
                if not strRead:
                    break
                md5.update(strRead)
            #read file finish
            flag = True
            strMd5 = md5.hexdigest()
        except:
            flag = False
        finally:
            if file:
                file.close()
        return {'flag':flag,'strmd5':strMd5}





