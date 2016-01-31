#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  hashlib
import re
import json
import os
import  sys,shutil
import  time,datetime

def file_exit(): #判断文件是否存在
    filename = "haproxy.cfg.new" #定义新的文件名称,之后先对就文件做操作
    print(os.path.exists(filename)) #取出来文件是否存在
    if not filename:
        shutil.copy("haproxy.cfg","haproxy.cfg.new")  #复制出一份新文件交haproxy.cfg.new
        print("copy------>")

    else:
        print("========>")

def user_login_func():  #用户登录认认证函数
    for i in range(3):
        login_user = input("请输入登陆用户:")
        login_password = input("请输入用户密码:")
        if login_user == "admin" and int(login_password) == int(123456):
            print("欢迎登陆haproxy管理系统")

            break
        else:
            print("用户或密码错误,请重新输入!")


def haproxy_add_func():
    backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999 100.1.7.999","weight":20,"maxconn":30}}' #举例要添加的格式
    user_input_data = input("\n请输入要添加的完整的backend名称,可复制--> %s\033[31;1m\n请在此输入要添加的backend的全称:\033[1m" % backend_name)
    json_user_input_data = json.loads(user_input_data)  #使用json转换成字典
    input_backend_name   =  json_user_input_data["backend"] #取出用户输入的backend后面的名称

    #backend的名称  test.oldboy.org
    print(input_backend_name,"---------->")
    input_haproxy_add_func_record   =  json_user_input_data["record"] #取出用户输入的record的主机配置明细
    add_backend_name = "backend %s " %  input_backend_name #生成与haproxy同样的backend xxx行,目前字典,需要拼接一下
    #backend test.oldboy.org   #要添加的backend行

    #{"maxconn": 30, "server": "100.1.7.999", "weight": 20} #拼接之前的字典格式
    add_haproxy_add_func_record = "server %s  maxconn %s  weight  %s "   % (input_haproxy_add_func_record["server"],input_haproxy_add_func_record["maxconn"],input_haproxy_add_func_record["weight"])  #生成与生成与haproxy同样的record
    #server 100.1.7.999  maxconn 30  weight  20  要添加的主机记录内容,添加在backend下面的地方
    print("要添加的主记录: %s" % add_haproxy_add_func_record)  #拼接成和haprox同样的主机行,add_haproxy_add_func_record是dd_backend_name下面如果就要添加的一行主机的记录
    print("要添加的backend名称: %s " % add_backend_name) #输出用户输入的bacnend
    str = "backend {0}" #字串格式化
    add_list = [] #空列表
    num  = 0 #标记,记录backend的行号
    num1 = 0 #标记,用于记录行号
    #shutil.copy("haproxy.cfg","haproxy.cfg.new")
    src = open("haproxy.cfg", "r+")
    des = open("haproxy.cfg.new", "w+")
    des.writelines(src.read())
    src.close()
    des.close()

    #time.sleep(1000)
    with open("haproxy.cfg.new") as f: #以只读方式度配置文件
        flag = False #标记位
        for line in f: #对配置文件做循环
            #print(line)
            if  str.format(json_user_input_data["backend"]) == line.strip(): #加输入的行和文件的入行是匹配的
                flag = True  #设置标记位为True,表示已经匹配到backend行
                num = num1  #赋值给num
                continue  #跳出本次循环
            elif flag and line.startswith("backend"): #找到下一个以backend开头行,表示已经跳出当前bacnend的主机配置范围
                break #则结束循环
            elif flag and line != "\n": #非空得行附加到礼列表
                add_list.append(line.strip())  #附加到列表
                #print(add_list)
                continue #结束本次循环进入下一次
            num1 += 1  #行的记录值加1
    if flag:  #假如backend名称不在文件中
        haproxy_add_func_dict = json_user_input_data["record"]  #从字典取出主机记录
        haproxy_add_func_record = "server %s weight %d maxconn %d" % (haproxy_add_func_dict["server"],haproxy_add_func_dict["weight"],haproxy_add_func_dict["maxconn"]) #拼成主机记录
        if haproxy_add_func_record in add_list: #加入主机记录在列表中
            print("该主机的配置文件已经存在,无需添加！") #输出主机已经存在
        else:  #如果不存在列表中
            with open("haproxy.cfg.new") as f: #打开配置文件
                haproxy_data_add = list(f) #转换成列表
                haproxy_add_func_record = "%s%s\n" % (" " * 8,haproxy_add_func_record) #拼接出主机配置信息
                haproxy_data_add.insert(num+1,haproxy_add_func_record) #在下方插入新的主机信息
                f = open("haproxy.cfg.new","w") #以写方式再打开配置文件并写入保存
                f.writelines(haproxy_data_add) #
                f.flush()
                f.close()

    else: #如果要增加的backend不在记录中,,即要新增加记录
        haproxy_add_func_dict = json_user_input_data["record"]  #样式格式化
        haproxy_add_func_record = "\nbackend %s\n%sserver %s weight %d maxconn %d\n" % (json_user_input_data["backend"]," " * 8,haproxy_add_func_dict["server"],haproxy_add_func_dict["weight"],haproxy_add_func_dict["maxconn"])
        with open("haproxy.cfg.new","w") as new_f:  #打开配置文件并保存新增加的主机记录
            new_f.write(haproxy_add_func_record)


    write_time = datetime.datetime.now()
    os.rename("haproxy.cfg","haproxy.cfg.bak.%s" % (write_time.strftime("%Y:%m:%d %H:%M:%S"))) #备份旧文件
    #shutil.copy("haproxy.cfg.new","haproxy.cfg.new.bak") #替换新文件
    os.rename("haproxy.cfg.new","haproxy.cfg") #替换新文件



def del_func():    #删除记录函数
    #backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999 100.1.7.999","weight":20,"maxconn":30}}' #定义删除记录的输入格式
    #del_record = input("请输入您要删除的记录：\n\t\t 记录格式如下：%s \n" % (backend_name))        #输入删除记录

    backend_name = '{"backend":"test.oldboy.org","record":{"server":"100.1.7.999 100.1.7.999","weight":20,"maxconn":30}}' #举例要添加的格式
    del_record = input("\n请输入要添加的完整的backend名称,可复制--> %s\033[31;1m\n请在此输入要添加的backend的全称:\033[1m" % backend_name)

    del_dict = json.loads(del_record)          #将删除记录的字符串转换成字典
    aa = get_data(del_dict["backend"])        #调用read_func()函数，查找要删的记录是否在文件中
    flag = aa[0]                              #判断要删的backend是否已经在文件中
    que_li = aa[1]                #如果要删的backend已经在文件中，会得到此backend下的server记录组成的list，否则为空列表
    if flag:            #如果要删的backend在文件中
        server_dict = del_dict["record"]       #取要删除的server记录
        record_name = "server %s weight %d maxconn %d" % (server_dict["server"],server_dict["weight"],server_dict["maxconn"])  #将server记录的字典拼接成字符串
        if record_name in que_li:      #如果要删除的server记录在que_li列表中
            f = open("haproxy.cfg")        #打开配置文件，并赋值给f
            fp = list(f)              #将文件内容转换成列表
            record_name =  "%s%s\n" % (" "*8,record_name)   #要删除的server记录
            fp.remove(record_name)         #将要删除的server记录移出列表
            f = open("haproxy.cfg","w")       #以w的方式打开配置文件，会新建配置文件
            f.writelines(fp)                  #写入配置文件
            f.flush()                          #刷新到硬盘
            f.close()                         #关闭文件
        else:    #如果要删除的server记录不在文件中
            print("backend %s里没有此条记录！" % del_dict["backend"])
    else:   #如果要删除的backend记录不在配置文件中
        print("没有此条backend！")


def get_data(get_args):  #获取信息
    #backend_cfg_name = input("请输入要查看的后端Server名称:") #后端backend名称，等于backend + 变量传进来的名称
    backend_new_name = "backend %s" % get_args
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
            if flag and line.startswith("backend"): #目前flag为True，假如flag为True并且行的开头以backend开头则跳出本次循环，提前退出可以防止遍历下面不符合要求的行，
                flag = False
                break
            if flag and line: #假如flag为True并且line不为空，则将数据写入列表保存，此数据为backend的内容
                list1.append(line)  #将筛选出的数据附加到列表
                continue #结束本次并进入下一次循环
        print("%s内包含的server为: %s" % (get_args,list1)) #打印结果
    return list1 #返回给函数

if  __name__ == "__main__":
    user_login_func()
    get_data_input = input("请选择要进行的操作, 1,查看  2,添加 3,退出,4,删除:")
    if  int(get_data_input) == 1:  #查询
        backend_cfg_name = input("请输入要查看的后端Server名称:") #后端backend名称，等于backend + 变量传进来的名称
        get_data(backend_cfg_name) #执行获取信息的函数

    elif  int(get_data_input) == 2:  #添加
        haproxy_add_func() #执行添加的函数

    elif  int(get_data_input) == 4:  #添加
        del_func()


    elif int(get_data_input) == 3:
        print("您已经成功退出")
        sys.exit(0) #退出


