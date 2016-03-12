#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import paramiko
import  configparser
import  subprocess
from  host_log import  log_models
import  datetime

class Config_class(object):


    def __init__(self,filename):
        '''
        初始化基本信息
        '''
        config = configparser.ConfigParser()
        config.read(filename)
        self.host_ipaddress = config['jack.com']['ipaddress']
        self.host_port = config['jack.com']['port']
        self.host_user = config['jack.com']['user']
        self.host_pass = config['jack.com']['password']
        self.user_logout_now = datetime.datetime.now()
        self.date1 = self.user_logout_now.strftime("%Y:%m:%d %H:%M:%S")

    def ssh_connetc(self):
        '''
        链接到主机并批量执行命令,文件上传和下载
        '''

        ssh = paramiko.Transport(self.host_ipaddress, int(self.host_port)) #实例化
        #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #首次链接的机器自动回答yes
        ssh.connect(username=self.host_user, password=self.host_pass) #连接到远程主机
        obj = subprocess.Popen(("df  -h"),shell=True, stdout=subprocess.PIPE) #批量执行命令
        self.conn = ssh
        print(obj.stdout.read()) #输出命令执行结果
        ssh.close()

        while True:
            select = input("请选择要进行的操作,1.退出, 2.上传文件 3.下载文件: ")
            if select == "1":
                print("您已经成功退出")
                ssh.close() #关闭会话
                exit(9)
            elif select == "2":
                up_filename = input("请输入要上传的文件名称:")
                ssh = paramiko.Transport(self.host_ipaddress, int(self.host_port))
                #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(username=self.host_user, password=self.host_pass)
                sftp = paramiko.SFTPClient.from_transport(ssh)
                sftp.put("readme",'home/')
                log_models("%s在服务器%s上传了%s文件" %(self.date1,self.host_ipaddress,up_filename))
                ssh.close()
            elif select == "3":
                down_filename = input("请输入要上传的文件名称:")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(self.host_ipaddress, int(self.host_port), self.host_user, self.host_pass)
                sftp = paramiko.SFTPClient.from_transport(self.conn)
                sftp.put(down_filename, 'home/download')
                log_models("%s在服务器%s下载了%s文件" %(self.date1,self.host_ipaddress,down_filename))
                ssh.close()
            else:
                print("输入错误,请重新输入要进行的操作!")
                continue

if __name__ == "__main__":
    conn = Config_class("example.ini")
    conn.ssh_connetc()
