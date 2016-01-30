#/usr/bin/env  python
# -*- coding:utf-8 -*-

import json
import os,time
import  sys
import  re,hashlib

def user_login_func():
    for i in range(3):
        login_user = input("请输入登陆用户:")
        login_password = input("请输入用户密码:")
        if login_user == "admin" and int(login_password) == int(123456):
            print("欢迎登陆haproxy管理系统")

            break
        else:
            print("用户或密码错误,请重新输入!")


def add_user_data():
    #backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999","weight": 20,"maxconn": 30}}' #定义要输入的内容
    #input_user_data = input("\n请输入要添加的完整的backend名称,可复制--> %s\033[31;1m\n请在此输入要添加的backend的全称:\033[1m" % backend_name) #用户输入的内容
    json_user_input_data = json.loads(input_user_data)  #使用json转换成字典

    input_backend_name   =  json_user_input_data["backend"] #取出用户输入的backend后面的名称

    input_record_name   =  json_user_input_data["record"] #取出用户输入的record的主机配置明细

    add_backend_name = "backend %s " %  input_backend_name #生成与haproxy同样的backend xxx行,目前字典,需要拼接一下

    #{'maxconn': 30, 'server': '100.1.7.999', 'weight': 20} #拼接之前的字典格式
    add_record_name = "server %s  maxconn %s  weight  %s "   % (input_record_name["server"],input_record_name["maxconn"],input_record_name["weight"])  #生成与生成与haproxy同样的record
    print("分析中...")
    time.sleep(2)
    print("分析中......")
    time.sleep(2)
    print("要添加的主记录: %s" % add_record_name)  #拼接成和haprox同样的主机行,add_record_name是dd_backend_name下面如果就要添加的一行主机的记录
    print("要添加的backend名称: %s " % add_backend_name) #输出用户输入的bacnend


    # with open("haproxy.cfg",'r') as old_haproxy, open("haproxy.cfg.new","w") as new_haproxy:
    #     for x in old_haproxy:
    #         new_haproxy.write(x)
    #         new_haproxy.flush()

def get_data(args):
    #backend_cfg_name = input("请输入要查看的后端Server名称:") #后端backend名称，等于backend + 变量传进来的名称
    backend_new_name = "backend %s" % backend_cfg_name
    list1 = [] #定义一个空的列表，用于保存用户查找到的数据
    #print(backend_new_name)
    with open("haproxy.cfg") as f: #读取配置文件
        flag = False #定义个标记位，用于后续处理
        #print(flag)
        for line in f: #循环文件的每一行,对配置文件逐行做以下处理，一次处理一行
            #print(type(line))
            line = line.strip() #去除每一行的开始和换行符，并赋值给line，line.strip获取到的是一个没有换行符的str
            if backend_new_name == line: #假如循环到的当前行等于要查询的backend 名称,满足之后直接进入下一行
                flag = True #将flag标记位True
                continue #跳出本次循环
            elif flag and line.startswith("backend"): #目前flag为True，假如flag为True并且行的开头以backend开头则跳出本次循环，提前退出可以防止遍历下面不符合要求的行，
                break
            elif flag and line: #假如flag为True并且line不为空，则将数据写入列表保存，此数据为backend的内容
                list1.append(line)  #将筛选出的数据附加到列表
                continue
        print("%s内包含的server为: %s" % (backend_cfg_name,list1))




if  __name__ == "__main__":
    get_data_input = input("请选择要进行的操作, 1,查看  2,添加 3,删除, 4退出:")
    if  int(get_data_input) == 1:
        backend_cfg_name = input("请输入要查看的后端Server名称:") #后端backend名称，等于backend + 变量传进来的名称
        get_data(backend_cfg_name)
    if  int(get_data_input) == 2:
        backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999","weight": 20,"maxconn": 30}}' #定义要输入的内容
        input_user_data = input("\n请输入要添加的完整的backend名称,可复制--> %s\033[31;1m\n请在此输入要添加的backend的全称:\033[1m" % backend_name) #用户输入的内容
        add_user_data()


    elif int(get_data_input) == 4:
        print("您已经成功退出")
        sys.exit(0)




#if __name__ == "__main__":

    #user_login_func()
    #get_data()
    #add_user_data()
