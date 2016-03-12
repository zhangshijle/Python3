#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie


import  socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New Conn:",self.client_address)
        while True:
            data = self.request.recv(1024)
            if not  data:
                break
            print("Client Says:",data.decode())
            self.request.send(data)
            self.request.send(bytes("本次数发送完毕","utf8"))


if __name__ == "__main__":
    Host,Port = "localhost",9003
    server = socketserver.ThreadingTCPServer((Host,Port),MyTCPHandler)
    server.serve_forever()