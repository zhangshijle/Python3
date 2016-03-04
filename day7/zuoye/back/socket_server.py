#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  socket
import  ssl
KEYFILE = "server_key.pem" #私有key
CERTFILE = "server_cert.pem" #公有key，传给客户端的


def socktdun(s):

    ip_port = ("127.0.0.1",5557) #绑定主机端口

    sk = socket.socket() #实例化方法
    sk.bind(ip_port) #监听绑定的本机端口
    sk.listen(5)  #


    while True:
        conn = ssl.wrap_socket(s,
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            server_side=True
                            )
        print("server is waiting.....")
        conn1,addr = conn.accept() #将监听到的客户机地址和IP保存到conn和addr
        client_data = conn.recv(1024) #接收到的用户请求的数据
        print(str(client_data,"utf8")) #打印用户发送的数据
        conn.send(client_data)  #发送给用户的数据
        while True:
            client_data = conn.recv(1024)
            print("recv:",str(client_data,"utf8"))
            if not client_data:break
            conn.send(client_data)
        conn.close()
