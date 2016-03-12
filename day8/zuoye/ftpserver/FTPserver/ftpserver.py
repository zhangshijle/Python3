#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie



import socketserver
import os,sys
import configparser

BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

sys.path.append(BASE_PATH)
from FTPserver import conf #找到FTPserver目录的父级即可

class FTPserver(socketserver.BaseRequestHandler):

    def handle(self):
        self.auth_user = self.auth().split("|")
        self.flag = self.auth_user[0]
        self.local_path = self.auth_user[1]
        self.ser_path = self.auth_user[2]
        while True:
            if self.flag == "0":
                data = self.request.recv(1024)
                if not data:
                    break
                data_new = str(data,"utf8").split("|")
                data_type = data_new[0]
                if hasattr(self,data_type):
                    func = getattr(self,data_type)
                    func(data_new)
                else:
                    print("datatype",data_type)
            else:
                print("客户端认证失败！")
                break

    def auth(self):   #用户登录认证和锁定家目录
        mod_file = "conf\setting"
        os.path.exists(mod_file) or sys.exit("用户配置文件不存在！")
        cf = configparser.ConfigParser()
        cf.read(mod_file,"utf8")
        name = cf.sections()
        user = self.request.recv(1024)
        user = str(user,"utf8").split("|")
        if user[0] in name:
            if user[1] == cf.get(user[0],"password"):
                flag = "0"
                home_path = cf.get(user[0],"home")
                ser_path = cf.get(user[0],"ser_home")
                auth_user = "%s|%s|%s" % (flag,home_path,ser_path)
            else:
                flag = "1"
                print("您输入的密码不正确！")
                auth_user = "%s|" % flag
        else:
            flag = "1"
            print("该用户没有注册FTP！")
            auth_user = "%s|" % flag
        self.request.send(bytes(auth_user,"utf8"))
        return auth_user

    def get(self,file_msg):   #下载
        cur_path = self.ser_path
        os.path.exists(cur_path) or os.mkdir(cur_path)
        filename = '%s/%s' %(cur_path,file_msg[1])
        if os.path.isfile(filename):
            file_size = os.path.getsize(filename)
            ready_msg = "get_file-->ready-->%s" % file_size
            self.request.send(bytes(ready_msg,"utf8"))
            recv_msg = self.request.recv(1024)
            recv_msg = str(recv_msg,"utf8")
            if recv_msg == "get_file-->recv":
                f = open(filename,'rb')
                size_left = file_size
                while size_left >0:
                    if size_left < 1024:
                        self.request.send(f.read(size_left))
                        size_left = 0
                    else:
                        self.request.send(f.read(1024))
                        size_left -= 1024

                else:
                    print("文件传输完成!")
        else:#file doesn't exist
            err_msg = "没有那个文件或目录!"
            self.request.send(bytes(err_msg,"utf8"))

    def put(self,file_msg):   #上传
        print("将要接收的文件为：",file_msg[1])
        recv_msg = self.request.recv(1024)
        recv_msg = str(recv_msg,"utf8")
        if recv_msg.startswith("put_file-->ready"):
            file_size = int(recv_msg.split("-->")[-1])
            print("文件大小为：",file_size)
            self.request.send(bytes("put_file-->recv","utf8"))
            cur_path = self.ser_path
            os.path.exists(cur_path) or os.mkdir(cur_path)
            filename = '%s/%s' %(cur_path,file_msg[1])
            f = open(filename,'wb')
            size_recv = 0
            progress_percent = 0
            while not size_recv == file_size:
                data = self.request.recv(file_size-size_recv)
                size_recv += len(data)
                f.write(data)
                cur_percent = int(float(size_recv) / file_size * 100)
                if cur_percent > progress_percent:
                    progress_percent = cur_percent
            else:
                print("文件传输完成!")



if __name__ == "__main__":
    ip_addr = ("127.0.0.1",9003)
    server = socketserver.ThreadingTCPServer(ip_addr, FTPserver)
    server.serve_forever()
