#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jly'
import SocketServer,json
import loginServer,dealwithFileServer,Authorization
from unionServer import *

class MyServer(SocketServer.BaseRequestHandler):
    '''ftp多线程server入口，当有客户端请求的时候在这里建立与客户端连接。
    判断client端请求，完成登录后，可以在其权限内的文件夹及其子目录进行文件的上传和下载。'''
    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall('欢迎使用FTP服务,您已建立ftp连接！')
        Flag = True
        authorized = False
        authorizedDir = ''
        while Flag:
            jmsgClient = conn.recv(1024)
            msgClient = json.loads(jmsgClient)
            #处理登录，登录成功后初始化对象的角色，权限目录等属性
            if msgClient['request'] == 'login':
                result,role,authorizedDir = loginServer.login(msgClient['user'],msgClient['password'])
                if result == '1':
                    authorized = True
                    userServerObj = unionServer(msgClient['user'],role,authorizedDir,conn)
                userServerObj.conn.sendall(result)
            #处理退出
            elif msgClient['request'] == 'exit':
                Flag = False
            #处理上传，支持文件的批量上传
            elif authorized and msgClient['request'] == 'upload':
                userServerObj.conn.sendall('received')
                userServerObj.chooseDir()
                for file in range(msgClient['fileCount']):
                    jmsgClient = userServerObj.conn.recv(1024)
                    print '###',jmsgClient
                    msgClient = json.loads(jmsgClient)
                    userServerObj.receiveUpload(msgClient['strmd5'],msgClient['fileSize'],msgClient['fileName'])
                print 'upload finished'
            #处理下载，支持文件的批量下载
            elif authorized and msgClient['request'] == 'download':
                print msgClient['request']
                userServerObj.receiveDownlode()
        conn.close()
        print 'conn is closed'

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()

