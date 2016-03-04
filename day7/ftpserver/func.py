#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import os
class ServerClass(object):
    def server_download(self,conn):
        file_name= conn.recv(1024)
        filename = "haproxy"
        #if os.path.exists(file_name):
        file_size = os.path.getsize(filename)
        print("file_size",file_size)
        conn.send(bytes(file_size,"utf8"))



