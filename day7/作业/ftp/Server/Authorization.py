#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jly'
import os
import json
from userClass import *
class Authorization(userServer):
    '''Authorization控制上传至server端文件夹或者要下载文件的选择，可以选择用户有权限目录下的所有位置。
        控制权限，如果用户想访问权限外的目录，将被阻止。'''
    def getdir(self):
        '''查看当前目录下的所有文件和文件目录，分别放入字典并返回'''
        if os.walk(self.currentDir).next():
            dirDic = {}
            print os.walk(self.currentDir).next()
            dirResult = os.walk(self.currentDir).next()
            dirDic['dir'] = dirResult[1]
            dirDic['file'] = dirResult[2]
            return dirDic
        else:
            return False

    def chooseDir(self):
        '''与客户端进行交互最终实现客户端自由选择有权限的文件夹，上传至该位置'''
        while True:
            dirDic = self.getdir()
            jdirDic = json.dumps(dirDic)
            self.conn.sendall(jdirDic)
            while True:
                print '***'
                jnextoperate = self.conn.recv(1024)
                print 'jnextoperate:',jnextoperate
                nextoperate = json.loads(jnextoperate)
                if nextoperate[0] == 3:
                    if dir != self.Authdir:
                        dirlst = nextoperate[1].split('\\')
                        dirlst.pop()
                        print '\\'.join(dirlst)
                        self.currentDir = '\\'.join(dirlst)
                    else:
                        self.conn.sendall('权限不足，您不能返回上一级菜单')
                        continue
                elif nextoperate[0] == 0:
                    print 'self.currentDir:',self.currentDir
                    return
                else:
                    self.currentDir = '%s\\%s'%(self.currentDir,nextoperate[1])
                    if nextoperate[0] == 1:
                        return
                    if nextoperate[0] == 2:
                        break

    def chooseDirD(self):
        '''与客户端进行交互最终实现客户端自由选择有权限的文件夹，选择该位置下的文件夹进行下载'''
        while True:
            dirDic = self.getdir()
            jdirDic = json.dumps(dirDic)
            self.conn.sendall(jdirDic)
            while True:
                jnextoperate = self.conn.recv(1024)
                nextoperate = json.loads(jnextoperate)
                if nextoperate[0] == 3:
                    if self.currentDir != self.Authdir:
                        dirlst = nextoperate[1].split('\\')
                        dirlst.pop()
                        print '\\'.join(dirlst)
                        self.currentDir = '\\'.join(dirlst)
                    else:
                        self.conn.sendall('权限不足，您不能返回上一级菜单')
                        continue
                else:
                    print 'nextoperate[0]:',nextoperate[0]
                    print 'nextoperate[1]:',nextoperate[1]
                    if nextoperate[0] == 1:
                        dirlist = map(lambda filename:'%s\\%s'%(self.currentDir,filename),nextoperate[1])
                        print 'authdirlist:',dirlist
                        return dirlist
                    if nextoperate[0] == 2:
                        self.currentDir = '%s\\%s'%(self.currentDir,nextoperate[1])
                        break

