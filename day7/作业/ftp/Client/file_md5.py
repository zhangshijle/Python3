#!/usr/bin/env python
#-*-coding:utf-8-*-

import hashlib

def GetFileMd5(strFile):
    '''文件的md5加密'''
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

#print(GetFileMd5('test.py'))