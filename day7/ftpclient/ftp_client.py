#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import  json

def file(sk):
    Flae = True
    while Flae:
        select = input("请选择要进行的操作,1上传文件  2下载文件  3退出")
        if select == "1":
            sk.sendall(bytes(select,"utf8"))
            client_download(sk)
        elif select == "2":
            client_download(sk)
        elif select =="3":
            client_download(sk)

def client_download(sk):
    print(sk)
    file_name = input("输入要下载的文件名! :")
    sk.send(bytes(file_name,"utf8"))
    file_size = sk.recv(1024)
    print("下载的文件大小为:",str(file_size,"utf8"))

def socket_connet():
    ip_port = ('127.0.0.1',1115)
    sk = socket.socket()
    sk.connect(ip_port)
    data = sk.recv(1024)
    print(str(data,"utf8"))
    file(sk)
    sk.close()

if __name__ == "__main__":
    socket_connet()
