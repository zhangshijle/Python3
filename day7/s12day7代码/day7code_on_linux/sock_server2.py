#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import time
import subprocess 
ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    print('server waiting...')
    conn,addr = sk.accept()
    while True:
            client_data = conn.recv(1024)
            if not client_data:break
            print("recv cmd:",str(client_data,'utf8'))
            cmd = str(client_data,"utf8").strip()
            cmd_call = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
            cmd_result = cmd_call.stdout.read()
            if len(cmd_result) == 0:
               cmd_result = b"cmd execution has no output.."
            ack_msg = bytes("CMD_RESULT_SIZE|%s" %len(cmd_result) ,"utf8")
            conn.send(ack_msg)
            client_ack = conn.recv(50) 
            if client_ack.decode() == 'CLIENT_READY_TO_RECV':
              conn.send(cmd_result )


conn.close()

