#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
#/usr/bin/env  python
# -*- coding:utf-8 -*-

import  socketserver
import  os,sys
from func import  ServerClass

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall(bytes("欢迎使用FTP服务,您已建立ftp连接","utf8"))

        Flag = True
        while Flag:
            data = conn.recv(1024)
            print(str(data,"utf8"),"data------>")
            if not data:
                break

            if str(data,"utf8") == "1":
                ServerClass.server_download(self,conn)
                break

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",1115),Myserver)
    server.serve_forever()




