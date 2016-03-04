#/usr/bin/env  python
# -*- coding:utf-8 -*-
import  os
import  user
import  socketserver
from socket import  socket,AF_INET,SOCK_STREAM
import  ssl,subprocess
KEYFILE = 'server_key.pem' #私有key
CERTFILE ='server_cert.pem' #公有key，传给客户端的

'''
def echo_client(s):
    while True:
        aa = s.recv(1024)
        if aa == b'':
            break
        print(str(aa,"utf8"))
        s.send(aa)
    s.close()
    print("连接关闭")
'''
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("sss")
        conn = self.request
        print("starting..",self.client_address)

        '''
        s_ssl = ssl.wrap_socket(s,
                                keyfile=KEYFILE,
                                certfile=CERTFILE,
                                server_side=True,
                                )
        '''
        '''
        while True:
            c,a = s_ssl.accept()
            print("conn to:",a)
            #echo_client(c)
            while True:
                aa = c.recv(1024)
                if aa == b'':
                    break
                print(str(aa,"utf8"))
                c.send(aa)
            c.close()
        print("连接关闭")
        '''
        Flag = True
        while Flag:
            data1 = conn.recv(1024)
            if not data1:
                break
            print("recv cmd:",str(data1,'utf8'))
            cmd = str(data1,"utf8").strip()
            cmd_call = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
            cmd_result = cmd_call.stdout.read()
            if len(cmd_result) == 0:
               cmd_result = b"cmd execution has no output.."

            ack_msg = bytes("CMD_RESULT_SIZE|%s" %len(cmd_result) ,"utf8")

            conn.send(ack_msg)
            client_ack = conn.recv(50)
            if client_ack.decode() == 'CLIENT_READY_TO_RECV':
                conn.send(cmd_result )

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",1234),Myserver)
    server.serve_forever()




