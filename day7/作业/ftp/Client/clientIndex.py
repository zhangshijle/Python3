#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import dealwithFileClient
import loginClient

def navi(sk):
    #loginRe = loginClient.loginClient(sk)
    flag = True
    #if loginRe:
    while flag:
        operate = input('请选择您要进行的操作（1.上传文件  2.下载文件 3.退出）：')
        if operate == '1':
            dealwithFileClient.uploadClient(sk)
        elif operate == '2':
            dealwithFileClient.downloadClient(sk)
        elif operate == '3':
            dealwithFileClient.exitFunc(sk)
            flag = False

def main():
    '''main方法，建立与server端的连接'''
    ip_port = ('127.0.0.1',8009)
    sk = socket.socket()
    sk.connect(ip_port)
    welcome = sk.recv(1024)
    print(welcome)
    navi(sk)
    sk.close()

if __name__ == "__main__":
    main()