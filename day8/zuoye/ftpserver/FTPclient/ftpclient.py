#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import socket
import sys,os


class Client(object):

    def __init__(self,ip_addr):  #初始化
        self.sock = socket.socket()
        self.sock.connect(ip_addr)
        self.auth_user = self.auth()
        self.local_path = self.auth_user[1]
        self.ser_path = self.auth_user[2]
        if self.auth_user[0] == "0":
            self.interactive()

    def auth(self):  #用户登录认证和锁定家目录
        username = input("login#>>")
        password = input("passw#>>")
        user = "%s|%s" % (username,password)
        self.sock.send(bytes(user,"utf8"))
        auth_user = self.sock.recv(1024)
        auth_user = str(auth_user,"utf8").split("|")
        local_path = auth_user[1]
        ser_path = auth_user[2]
        if auth_user[0] == "0":
            print("恭喜您登陆成功！\n您的本地家目录为：%s\n您的FTP目录为：ftp:\\\%s" % (local_path,ser_path))
            return auth_user
        else:
            exit()

    def interactive(self):   #选择操作：下载或者上传
            try:
                while True:
                    cmd = input("#>>")
                    if len(cmd) == 0:continue
                    cmd_new = cmd.split()
                    cmd_type = cmd_new[0]
                    if cmd_type == "get":
                        func = getattr(self,cmd_type)
                        func(cmd_new)
                    elif cmd_type == "put":
                        func = getattr(self,cmd_type)
                        func(cmd_new)
                    else:
                        print("你输入的命令有误,请输入get命令!")
            except KeyboardInterrupt:
                self.exit('exit')
            except EOFError:
                self.exit('exit')

    def get(self,cmd):    #下载
        if len(cmd) == 2:
            print(cmd[1])
            file_msg = "get|%s" % cmd[1]
            self.sock.send(bytes(file_msg,"utf8"))
            ready = self.sock.recv(1024)
            ready = str(ready,"utf8")
            if ready.startswith('get_file-->ready'):
                file_size = int(ready.split("-->")[-1])
                cur_path = self.local_path
                os.path.exists(cur_path) or os.mkdir(cur_path)
                filename = os.path.basename(file_msg.split("|")[-1])
                filename = "%s/%s" % (cur_path,filename)
                f = open(filename,'wb')
                self.sock.send(bytes('get_file-->recv',"utf8"))
                size_recv = 0
                progress_percent = 0
                while not size_recv == file_size:
                    data = self.sock.recv(file_size-size_recv)
                    size_recv += len(data)
                    f.write(data )
                    cur_percent = int(float(size_recv) / file_size * 100)
                    if cur_percent > progress_percent:
                        progress_percent = cur_percent
                else:
                    print("文件传输完成!")

            else:
                print('接收到的服务器信息为:%s' % ready)

    def put(self,cmd):   #上传
        if len(cmd) == 2:
            cur_path = self.local_path
            os.path.exists(cur_path) or os.mkdir(cur_path)
            filename = '%s/%s' %(cur_path,cmd[1])
            if os.path.isfile(filename):
                file_msg = "put|%s" % cmd[1]
                self.sock.send(bytes(file_msg,"utf8"))
                file_size = os.path.getsize(filename)
                ready_msg = "put_file-->ready-->%s" % file_size
                self.sock.send(bytes(ready_msg,"utf8"))
                recv_msg = self.sock.recv(1024)
                recv_msg = str(recv_msg,"utf8")
                if recv_msg.startswith("put_file-->recv"):
                    f = open(filename,'rb')
                    size_left = file_size
                    while size_left >0:
                        if size_left < 1024:
                            self.sock.send(f.read(size_left))
                            size_left = 0
                        else:
                            self.sock.send(f.read(1024))
                            size_left -= 1024
                    else:
                        print("文件传输完成!")
            else:#file doesn't exist
                err_msg = "%s:没有那个文件或目录!" % filename
                self.sock.send(bytes(err_msg,"utf8"))




if __name__ == "__main__":
    ip_addr = ('127.0.0.1', 9003)
    s = Client(ip_addr)

