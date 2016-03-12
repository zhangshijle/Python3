#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.211.55.205', 22, 'root', '123456')
stdin, stdout, stderr = ssh.exec_command('ifconfig')
a = stdout.read()
b = stderr.read()
print(a,"a")
print(b,"b")
ssh.close()
