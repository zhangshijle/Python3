#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import re

change_num = 0
def user_format_str(user_num)->"@运算符替换函数,删除空格并将两个加号减号的进行重新更改":
        str_num = re.sub("\s*","",user_num) #如果输入的公式中有空格则将空格删除,其他不变
        str_num = str_num.replace("++","+") #加一个正数为加,如1++2还是等于1+2,结果为3
        str_num = str_num.replace("+-","-") #加一个负数等于减,如1+-2等于1-2,结果为-1
        str_num = str_num.replace("--","+") #减一个负数等于加,如1--1等于1+1,结果为2
        str_num = str_num.replace("-+","-") #减一个正数等于减,如1-+1等于1-1,结果为0
        #print(num)
        return str_num #将替换好的结果返回给user_format_str函数

def user_division(division_num)->"@乘除加减的函数":
    division_num = user_format_str(division_num) #调用格式化函数处理加减操作符并将处理好的结果赋值给division_num
    #change_num = 0
    if not re.search("\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*",division_num):#如果不存在匹配的表达式（即不包含乘除,就运算后续的加减）则return返回user_num
    #\d+\.*\d*至少有一个是数字开头小数点和小数点后面的数字可有可无,[\*\/]+ 乘或除至少有一个,[\+\-]?加减可有0或一个,d+\.*\d*再以数字开头结尾小数点可有可无
        return division_num

    user_num1 = re.search("\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*",division_num).group() #取出紧连接的乘或者除,search全行匹配但只返回到的一组匹配到的结果
    #user_num1 = \d+\.*\d*至少以一个数字开头其后的小数可有可无,[\*,\/]+后面是至少一个乘或者除,[\+\-]?加和-可以有也可以没有,\d+\.*\d*再以整数或小数点数值结尾
    # print(s[0])

    if re.search("\*",user_num1): #假如匹配到乘
        global  change_num #全局变量,做计算的次数统计
        num1,num2 = user_num1.split("*") #num1和num1分别等于以*分割后的0和1元素
        num3 = float(num1) * float(num2) #num3等于num1乘num2的结果
        user_num = division_num.replace(user_num1,str(num3),1) #1为只替换一次,从左面替换第一次出现的,之后再有也不进行替换
        #print(division_num,"xxx")
        change_num += 1 #运算次数加1
        print("正在进行本公式第%s次乘法计算" % change_num) #输出运算次数

    elif re.search("\/",user_num1): #加入匹配到除
        num1,num2 = user_num1.split("/") #以/分割并赋值给num1和num2
        num3 = float(num1) / float(num2) #运算后赋值给num3
        user_num = division_num.replace(user_num1,str(num3),1) #1为只替换一次,因为默认即作替换
        change_num += 1 #运算次数加2
        print("正在进行本公式第%s次除法计算" % change_num) #输出运算次数

    return user_division(user_num) #返回公式

def user_add(add_num)->"@计算加减的函数":
    global  change_num
    add_num = user_format_str(add_num)#调用将处理好的公式赋值给add_num
    if not re.search("\d+\.*\d*[\+\-]\d+\.*\d*",add_num):#如果不存在匹配的表达式（即不包含加减）则return返回user_num
    #\d+\.*\d* 可以是整数也可以是包含小数点的数字,[\+\-] 加或者减,\d+\.*\d* 整数或小数点
        return add_num
    user_num2  = re.search("\d+\.*\d*[\+\-]\d+\.*\d*",add_num).group() #取出紧连接的乘或者除,负数也匹配出来,也可以没有负数
    #\d+\.*\d* 整数或小数,[\+\-]加或者减,\d+\.*\d*[\+\-]\d+\.*\d* 整数或小数
    # print(s[0])
    if re.search("\+",user_num2): #假如匹配到+,连续的两个加减符号的操作已经被第一个函数替换了
        num1,num2 = user_num2.split("+") #以加号分割出元素并赋值给num1和num2
        num3 = float(num1) + float(num2) #num3等于num1+num2
        add_num = add_num.replace(user_num2,str(num3),1) #1为只替换一次,因为默认即作替换
        change_num += 1 #计算次数加1
        print("正在进行本公式第%s次加法计算" % change_num) #输出替换次数
    elif re.search("\-",user_num2): #假如匹配到-,连续的两个加减符号的操作已经被第一个函数替换了
        num1,num2 = user_num2.split("-") #以减分割并复制给num1和num2
        num3 = float(num1) - float(num2) #num3 等于num1 - num2
        add_num = add_num.replace(user_num2,str(num3),1) #1为只替换一次,因为默认即作替换
        change_num += 1 #计算次数加1
        print("正在进行本公式第%s次减法计算" % change_num) #输出替换次数
    return user_add(add_num) #返回值给函数


def user_del(del_num)->"@删除括号的函数":
    del_num = user_format_str(del_num)  #调用格式化函数对加减符号进行处理
    if not re.search("\(([\+\-\*\/]*\d+\.*\d*){2,}\)",del_num):#至少匹配2次操作符号或数字
        #在del_num匹配0个或多个+=*/的操作符,后面是一个整数或小数,如果没有2次成功匹配,则返回原公式
        return user_compute(del_num)
    index_num = re.search("\(([\+\-\*\/]*\d+\.*\d*){2,}\)",del_num).group() #成功匹配两次
    #以找到(),里面可以有* /或+ -出现0次或多次,然后是一个数字或小数,匹配2次或以上
    #print(index_num,"index_num-->")
    index_num1 = index_num.strip("\(\)") #删除两边的括号()
    index_num2 = user_compute(index_num1)#将删除完括号的公式传递给计算函数user_compute计算并将计算完的结果赋值给index_num2
    del_num = del_num.replace(index_num,index_num2,1)#将将计算完成的结果替换公式
    return user_del(del_num) #将替换完成的公式传递删除括号的函数再次计算,直到没有括号为止

def user_compute(compute_num)->"@计算函数":
    compute_num = user_division(compute_num) #计算乘和除并复制给compute_num
    compute_num = user_add(compute_num) #计算加和减并复制给compute_num
    return compute_num #返回计算成功的值


def user_end()->"#最终处理函数":
    global  change_num
    User_num ="1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
    user_num = input("请输入要计算的公式,比如复制-->%s \n输入要计算的公式:" % User_num) #让用户输入公式
    end_num = user_del(user_num) #最终的计算结果
    #change_num -= 1 #为与最终运算的次数匹配,
    print("\033[31;1m经过本程序的%s次运算,公式最终的计算结果是-->: %s\033[0m" %(change_num,end_num)) #输出最终的计算结果
    change_num = 0 #计数器清0,下一次重新计算次数

if __name__ == "__main__":
    while True:
        try:
            process = input("请选择要进行的操作,1.使用计算器,2.退出:") #输入要执行的操作
            if process == "1":  #如果选择1,调用函数user_end执行计算
                user_end()
            elif process == "2": #如果选择2,退出
                import  sys
                print("欢迎再次使用>>>>!")
                sys.exit(5)
            else: #其他输入,返回错误并要求用户冲重新输入
                print("输入错误,请重新输入!")
        except KeyboardInterrupt:
            print("\n\033[31;1m您已手动终止程序运行!\033[1m")
            break


