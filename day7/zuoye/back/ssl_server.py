#/usr/bin/env  python
# -*- coding:utf-8 -*-

from socket import  socket,AF_INET,SOCK_STREAM
import  ssl
KEYFILE = 'server_key.pem' #私有key
CERTFILE ='server_cert.pem' #公有key，传给客户端的
def echo_server(address):
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    s_ssl = ssl.wrap_socket(s,
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            server_side=True,
                            )
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

echo_server(("127.0.0.1",20007))




