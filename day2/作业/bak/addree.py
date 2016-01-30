#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

def user_address():
    print("\033[31;1m收获地址\033[0m".center(100,"-"))
    with open("address.txt") as f:
        data = f.readlines()
    for i in data:
        print("您的收货地址-->%s" %(i))
    #print(data[1])
    address1 = data[0]
    address2 = data[1]
    while True:
        address = input("\n请选择您的收获地址,1/为家庭地址1 2/为工作地址:")
        flag = address.isdigit()
        if flag == True:
            if address == "1":
                print("您选择的收获地址为%s," % address1)
                user_riqi = input("请选择配送日期,1/周一到周日,2/周一到周五:")
                if user_riqi == "1":
                    print("\033[31;1m您选择的是周一到周日配送到地址%s,将在两日内到达,请注意收获!\033[0m" % address1)
                    break
                elif user_riqi == "2":
                    print("\033[31;1m您选择的是周一到周五配送到地址%s,将在两日内到达,请注意收获!\033[0m" % address1)
                    break
                else:
                    print("输入错误,请重新输入")
                    continue
            elif address == "2":
                print("您选择的收获地址为%s," % address2)
                user_riqi = input("请选择配送日期,1/周一到周日,2/周一到周五:")
                if user_riqi == "1":
                    print("\033[31;1m您选择的是周一到周日配送到地址%s,将在两日内到达,请注意收获!\033[0m" % address2)
                    break
                elif user_riqi == "2":
                    print("\033[31;1m您选择的是周一到周五配送到地址%s,将在两日内到达,请注意收获!\033[0m" % address2)
                    break
                else:
                    print("输入错误,请重新输入")
                    continue
            else:
                print("您的输入有误,请重新输入")
                continue
        else:
            print("您的输入不符合要求,请输入1或者2选择地址")
            continue

user_address()
