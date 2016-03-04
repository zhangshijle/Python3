#/usr/bin/env  python
# -*- coding:utf-8 -*-

from socket import  socket,AF_INET,SOCK_STREAM
import  ssl
s = socket(AF_INET,SOCK_STREAM)
print("111111")
KEYFILE = "server_key.pem" #私有key
CERTFILE = "server_cert.pem" #公有key，传给客户端的


s_ssl = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs="server_cert.pem")
print("222222")
s_ssl.connect(("127.0.0.1",20007))
while True:
    aaa = input(">>:")
    s_ssl.sendall(bytes(aaa,"utf8")) #发送的数据,python3需要转换成utf8并使用bytes发送
    server_reply = s_ssl.recv(1024) #收到的服务器的数据,每次接收数据的大小
    print(str(server_reply,"utf8"))  #打印接收的服务器返回的数据并转换成utf8和str
    #s_ssl.recv(1024)
    #s_ssl.send(b"hello word ?")
s_ssl.close()