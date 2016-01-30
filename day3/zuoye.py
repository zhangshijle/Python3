#/usr/bin/env  python
# -*- coding:utf-8 -*-

import json
import os
import  sys
import  datetime

def user_login():  #登录函数
    flag=0  #定义一个标记变量
    for login_num in range(3): #此循环,用户有三次机会输入密码
        user = "root" #登录用户
        password = "123456" #登录密码
        login_user = input("请输入登录用户名:") #要求用户输入登录用户
        login_password = input("请输入登录密码:") #要求用户输入登录密码
        if login_user == user and login_password == password:  #假如用户输入的用户和密码与设定好的是一样的
            print("欢迎登录本系统") #输出欢迎登录界面
            break #跳出本循环
        else:
            print("用户名密码或密码错误,请重新登录") #如果密码不对,返回错误，继续下次循环
            continue
    else:
        print("用户名密码输入次数达到3次或以上,请稍后重新登录")  #三次密码不对，提示稍后登录
        flag=1  #标记变量赋值为1
        return flag  #返回标记变量，如果返回1，就代表登录不成功



def add_func():
    backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999 100.1.7.999","weight":20,"maxconn":30}}'
    add_record = input("请输入您要增加的记录：\n\t\t 记录格式如下：%s \n" % (backend_name))
    add_dict = json.loads(add_record)
    aa = read_func(add_dict["backend"])
    flag = aa[0]
    que_li = aa[1]
    poin = aa[2]
    if flag:
        server_dict = add_dict["record"]
        record_name = "server %s weight %d maxconn %d" % (server_dict["server"],server_dict["weight"],server_dict["maxconn"])
        if record_name in que_li:
            print("您要添加的记录已存在！")
        else:
            f = open("haproxy.cfg")
            fp = list(f)
            record_name = "%s%s\n" % (" "*8,record_name)
            fp.insert(poin+1,record_name)
            f = open("haproxy.cfg","w")
            f.writelines(fp)
            f.flush()
            f.close()
    else:
        server_dict = add_dict["record"]
        record_name = "\nbackend %s\n%sserver %s weight %d maxconn %d\n" % (add_dict["backend"]," "*8,server_dict["server"],server_dict["weight"],server_dict["maxconn"])
        f = open("haproxy.cfg","a")
        f.write(record_name)
        f.flush()
        f.close()

def read_func(backend):
    str = "backend {0}"
    que_li = []
    pos = 0
    poin  = 0
    with open("haproxy.cfg","r") as f: #读取配置文件
        flag = False
        for line in f: #循环文件的每一行,对配置文件逐行做以下处理，一次处理一行
            if  str.format(backend) == line.strip():
                flag = True
                poin = pos
                continue
            elif flag and line.startswith("backend"): #目前flag为True，假如flag为True并且行的开头以backend开头则跳出本次循环，提前退出可以防止遍历下面不符合要求的行，
                break
            elif flag and line != "\n": #假如flag为True并且line不为空，则输出记录
                que_li.append(line.strip())
                continue
            pos += 1
    f.close()
    return (flag,que_li,poin)

def del_func():
    backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999 100.1.7.999","weight":20,"maxconn":30}}'
    del_record = input("请输入您要删除的记录：\n\t\t 记录格式如下：%s \n" % (backend_name))
    del_dict = json.loads(del_record)
    aa = read_func(del_dict["backend"])
    flag = aa[0]
    que_li = aa[1]
    if flag:
        server_dict = del_dict["record"]
        record_name = "server %s weight %d maxconn %d" % (server_dict["server"],server_dict["weight"],server_dict["maxconn"])
        print(record_name)
        print(que_li)
        if record_name in que_li:
            f = open("haproxy.cfg")
            fp = list(f)
            print(fp)
            record_name =  "%s%s\n" % (" "*8,record_name)
            print(record_name)
            fp.remove(record_name)
            f = open("haproxy.cfg","w")
            f.writelines(fp)
            f.flush()
            f.close()
        else:
            print("backend %s里没有此条记录！" % del_dict["backend"])
    else:
        print("没有此条backend！")

if __name__ == '__main__':  #主程序，入口
        flag=user_login()                  #调用登录函数，并返回登录结果
        if flag == 1:                     #如果登录结果为失败
            exit()                      #退出循环，即退出程序
        else:
            while 1:
                opera = input("请输入您要进行的操作：A：查询ha记录，B：增加ha记录，C：删除ha记录，Q：退出")
                if opera.upper() == 'A':
                    query_func()
                if opera.upper() == 'B':
                    add_func()
                if opera.upper() == 'C':
                    del_func()
                if opera.upper() == 'Q':
                    exit()




