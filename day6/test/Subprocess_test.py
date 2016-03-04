#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  subprocess
#print(subprocess.run(["ls"]))
print(subprocess.run(['ls','-lA',"/tmp/"]))
print(subprocess.run("ls -lA",shell=True))  #带参数的语句,声明使用shell

p = subprocess.Popen("find /tmp/ -size +1000000 -exec ls -shl {} \;",shell=True,stdout=subprocess.PIPE)
print(p.stdout.read(),"--->")