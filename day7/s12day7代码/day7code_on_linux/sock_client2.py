#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',12345)

sk = socket.socket()
sk.connect(ip_port)

while True:
    user_input = input("cmd:").strip()
    if len(user_input) == 0:continue
    if user_input == 'q':break
 
    sk.send(bytes(user_input,'utf8'))
    #ack_msg = b"CMD_RESULT_SIZE|%s" % len(cmd_result)
    server_ack_msg = sk.recv(100)
    cmd_res_msg = str(server_ack_msg.decode()).split("|")  
    print("server response:",cmd_res_msg)
    if cmd_res_msg[0] =="CMD_RESULT_SIZE":
      cmd_res_size = int(cmd_res_msg[1])
      sk.send(b"CLIENT_READY_TO_RECV")
    res = '' 
    received_size = 0
    while received_size < cmd_res_size:
      data = sk.recv(500)
      received_size += len(data)
      res += str(data.decode())
    else:
      print(str(res))
      print('-------recv done----')
sk.close()

