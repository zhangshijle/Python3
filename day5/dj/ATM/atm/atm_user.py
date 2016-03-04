#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  os,sys
pathdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(pathdir)


from   ATM.db_atm import db

limit = 15000  #额度
money = 0     #账户总支出
bal = limit  #账户余额


def login_atm():
    flag=0  #定义一个标记变量
    for login_num in range(3): #三次循环
        if db.mysql_auth(): #如果数据库认证通过
            username = "jack" #登录用户
            password = "123456" #登录密码
            login_user = input("请输入登录用户名:") #要求用户输入登录用户
            login_password = input("请输入登录密码:") #要求用户输入登录密码
            if login_user == username and login_password == password:  #加入用户秘密通过认证
                flag=0
                break #结束循环
            else:
                print("用户名密码或密码错误,请重新登录") #如果密码不对,返回错误，继续下次循环
                continue
        else:
            flag=1  #标记为1
        return flag  #返回标记变量

def cash_func():   #取现函数
    global money
    global bal
    cash = input("请输入您本次要提现的金额：")
    while True:
        if cash.isdigit():
            q = input("请确认您本次要提现%s元吗？y/n ：" % cash)
            if q.lower() == "y":
                cash=int(cash)
                if cash <= bal:
                    print("提现成功！")
                    hand_charge = cash * 0.05   #记录手续费
                    mon = cash + hand_charge
                    bal -= mon
                    money += mon
                    break
                else:
                    while True:
                        a= input("余额不足！是否重新输入提现金额？ y/n ：")
                        if a.lower() == "y":
                            cash=input("请您重新输入提现金额：")
                            break
                        elif a.lower() == "n":
                            print("您此次没有提现！")
                            return False
                        else:
                            print("您的输入有误，请重新输入！")
                            continue
            elif q.lower() == "n":
                cash=input("请重新输入提现金额：")
                continue
            else:
                print("您的输入有误，请重新输入！")
                continue
        else:
            cash = input("您输入的有误，请输入数字：")
            continue
    return True

def exchange_func():
    pass



if  __name__ == "__main__":
    login_atm()
    cash_func()
    print(money,bal)























