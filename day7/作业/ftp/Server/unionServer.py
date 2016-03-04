#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'jly'

from dealwithFileServer import dealwithServer
from Authorization import Authorization

class unionServer(Authorization,dealwithServer):
    '''在登录成功后进行初始化对象
    为了代码的可看性，将代码的所有方法分成了userServer，Authorization，dealwithServer三个类
    所以这个方法什么也不做，只是继承了上面三个类
    userServer初始化基类，封装了给文件进行MD5加密的静态方法，
    Authorization控制上传至server端文件夹或者要下载文件的选择，可以选择用户有权限目录下的所有位置。
        控制权限，如果用户想访问权限外的目录，将被阻止。
    dealwithServer处理文件的上传、下载。支持批量上传和下载
    '''
    pass