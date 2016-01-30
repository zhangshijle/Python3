#/usr/bin/env  python
# -*- coding:utf-8 -*-


with open("password.txt","r+") as  username:
    usernamelist = username.readlines()
    #print usernamelist,">----usernamelist---->"  #获取到的用户名密码和锁定次数的列表
    #["shijie|123456|1\r\n", "jack|123456|3"] #用户名|密码|锁定次数
userdics = {} #定义一个空的用户字典，使用字典保存用户账号和密码

for userdiclist  in  usernamelist:
    userlist = userdiclist.split("|")
    userdics[userlist[0]] = {"pwd":userlist[1],"locking":int(userlist[2].strip())}
    #print userdics.keys(),key为["shijie|123456|1\r\n", "jack|123456|3"] ["shijie"] ["shijie", "jack"]


for i in range(3): #开始循环，获取用户输入并进行判断,三次累计输入的用户密码错误即退出,
    username = raw_input("请输入登陆用户名:")  #让用户输入用户名并赋值给username
    password = raw_input("请输入您登陆的用户密码：") #让用户输入密码并赋值给password
    if username in userdics.keys():   #如果用户输入的用户名是存在userdics.keys()当中的，即有此用户在列表当中
        if userdics[username]["locking"] >= 3: #判断用户存在且密码正确后后，其locking次数如果大于等于3即输出用户被锁定
            print "\033[32;1m%s此账户因错误密码超过三次已被锁定，无法登陆,请联系Python开发工程师张士杰\033[0m" % (username)
            userlist2 = []  #定义空列
            for k,v in userdics.items():  #循环用户的字典，获取用户的密码和锁定次数,k为用户名，v为一个字典格式的用户名和锁定次数
                #print k,v  #生成字典，格式如下两行
                #shijie {"pwd": "123456", "locking": 1}
                #jack {"pwd": "123456", "locking": 3}
                userinfo = "%s|%s|%d" % (k,v["pwd"],v["locking"])  #将用户名密码和锁定次数生成一个按照|分隔的字串,传递用户名，密码和锁定次数作为参数
                #print userinfo #字串格式如下
                #shijie;123456;1
                userlist2.append(userinfo)  #将字串信息附加之列表当中
                #print userlist2
            usernewinfo = "\n".join(userlist2)  #把列表分割并转换为字符串
            #print usernewinfo
            with open("password.txt","wb+") as f:  #以二进制追加写的方式打开password.txt文件,如果是使用rb+的方式打开会出现用户名密码重复出现
                f.write(usernewinfo) #将用户列表写入password.txt文件
                f.flush() #写入完成后立即刷新磁盘
            break  #如果用户被锁定了，就退出

        if password == userdics[username]["pwd"]: #如果密码等于提前设置好的用户密码
            print "欢迎 %s 登陆本系统" % username #欢迎登陆信息
            userdics[username]["locking"] = 0 #登陆成功后将用户锁定的次数充值为0，前提是其锁定次数要在3次数之内才可以登录成功
            userlist2 = []   #定义空列
            for k,v in userdics.items(): #循环用户的字典，获取用户的密码和锁定次数,k为用户名，v为一个字典格式的用户名和锁定次数
                userinfo = "%s|%s|%d" % (k,v["pwd"],v["locking"])   #将用户名密码和锁定次数生成一个按照|分隔的字串
                userlist2.append(userinfo)  #将字串信息附加之列表当中
            usernewinfo = "\n".join(userlist2)  #把列表分割并转换为字符串
            with open("password.txt","wb+") as f:  #以二进制读写的方式打开文件
                f.write(usernewinfo) #把字符串保存在列表
                f.flush() #保存到吸盘
            break  #退出程序

        else: #如果密码不正确
            userdics[username]["locking"] += 1 #将用户锁定次数时时加1
            print "您输入的用户%s的密码为%s,但是该密码是错误的，请核对后重新登陆" % (username,password)
            userlist2 = []   #定义空列
            for k,v in userdics.items(): #循环用户的字典，获取用户的密码和锁定次数,k为用户名，v为一个字典格式的用户名和锁定次数
                userinfo = "%s|%s|%d" % (k,v["pwd"],v["locking"])   #将用户名密码和锁定次数生成一个按照|分隔的字串
                userlist2.append(userinfo)  #将字串信息附加之列表当中
            usernewinfo = "\n".join(userlist2)  #把列表分割并转换为字符串
            with open("password.txt","wb+") as f:  #以二进制读写的方式打开文件
                f.write(usernewinfo) #把字符串保存在列表
                f.flush() #保存到吸盘，一旦用户的锁定次数达到5之后将被锁定
    else:
        print "您输入的用户名%s不存在,请重新输入" % username
else:
    print "\033[31;1m您因密码输入次数大于三次已被禁止登陆本系统\033[0m"