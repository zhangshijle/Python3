#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  socket
ip_port = ("127.0.0.1",9003)
sk = socket.socket()
sk.connect(ip_port)

while True:
    aaa = input(">>:")
    sk.send(bytes(aaa,"utf8"))
    server_reply = sk.recv(4096)
    print(server_reply.decode())
    data = sk.recv(1024)
    print(data.decode())