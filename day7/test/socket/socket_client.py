#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  socket  #导入模块
ip_port = ("127.0.0.1",9000) #用元组绑定要链接的服务器地址和端口
sk = socket.socket() #实例化方法
sk.connect(ip_port) #将端口传递给链接的方法

while True:
    aaa = input(">>:")
    sk.sendall(bytes(aaa,"utf8")) #发送的数据,python3需要转换成utf8并使用bytes发送
    server_reply = sk.recv(1024) #每次接收数据的大小
    print(str(server_reply,"utf8"))  #打印接收的数据并转换成utf8和bytes

sk.close()