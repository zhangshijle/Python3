#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
class WebServer(object):
    def __init__(self,host,port):    # Constructor of the class
        self.host = host
        self.port = port
    def start(self):
        print("Server is starting...")
    def stop(self):
        print("Server is stopping...")
    def restart(self):
       self.stop()
       self.start()
def test_run(self,name):
    print("running...",name,self.host)
if __name__ == "__main__":
    server = WebServer('localhost',333)
    server2 = WebServer('localhost',333)
    #print(sys.argv[1])
    if hasattr(server,sys.argv[1]):
        func = getattr(server,sys.argv[1]) #获取server.start 内存地址
        func() #server.start()

    #setattr(server,'run',test_run)
    #server.run(server,'alex')
    delattr(WebServer,'start')
    print(server.restart())
    #server2.run(server,'alex')

    '''cmd_dic = {
        'start':server.start,
        'stop':server.stop,
    }'''
    #if sys.argv[1] == 'start':
    #if sys.argv[1] in cmd_dic:
    #    cmd_dic[sys.argv[1]]()