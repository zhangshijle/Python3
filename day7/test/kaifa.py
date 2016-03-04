#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  sys
class WebServer(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def start(self):
        print("server is starting")

    def stop(self):
        print("server is stoping")

    def restart(self):
        self.stop()
        self.start()

def test_run(self,name):
    print("running...",name,self.host)


if __name__ == "__main__":
    server = WebServer("lcoalhost",1234)
    server2 = WebServer("localhost",1234)
    #print(sys.argv[1],"-->")

    if hasattr(server,sys.argv[1]):
        func = getattr(server,sys.argv[1])
        func()
    #setattr(server,"run",test_run)
    #server.run(server,"jack")

    delattr(WebServer,'start') #无法通过server删除,因为start是累的方法,只能通过类删除其内部的方法
    #print(server.restart())
    #server2.run(server,"tom")