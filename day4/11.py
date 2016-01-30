#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import re
string ='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

def user_func1(arg)->"#格式化表达式中的 + - 剔除表达式中的空格":
    num = re.sub('\s*','',string) #剔除空格
    num = arg.replace('--','+') #负负为正 “--” = “+”
    num = arg.replace('-+','-')#负正为负 “-+” = “-”
    num = arg.replace('+-','-')#正负为负 “+-” = “-”
    num = arg.replace('++','+')#正正为正 “++” = “+”
    return num #return格式化后的表达式

def mul_div(string):#计算乘除
    string = user_func1(string)#调用格式化表达式方法user_func1（）对表达式进行格式化
    if not re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*',string):#如果不存在匹配的表达式（即不包含乘除）则return返回string
        return string

    s = re.search('\d+\.*\d*[\*,\/]+[\+\-]?\d+\.*\d*',string).group()#检索第一个乘除表达式
    #判断检索到的表达式是 乘 或 除 并交给相应的程序进行处理
    if re.search('\*',s): #如果为乘
        resuit = float(s.split('*')[0])*float(s.split('*')[1])#以乘号为分隔符进行分割 并 对分割后的值进行浮点格式化、乘法运算
        string = string.replace(s,str(resuit),1)#对表达式中的元素进行替换，将计算结果替换对应的程式
    elif re.search('/',s):
        resuit = float(s.split('/')[0])/float(s.split('/')[1])#以除号为分隔符进行分割 并 对分割后的值进行浮点格式化、除法运算
        string = string.replace(s,str(resuit),1)#对表达式中的元素进行替换，将计算结果替换对应的程式
    return mul_div(string)#对方法进行迭代计算 并return返回计算的结果
#计算加减
def add_sub (string):
    string = user_func1(string)#调用格式化表达式方法user_func1（）对表达式进行格式化
    if not re.search('\d+\.?\d*[\+\-]\d+\.?\d*',string): #如果不存在匹配的表达式（即不包含加减）则return返回string
        return string
    s = re.search('\d+\.*\d*[\+,\-]\d+\.*\d*',string).group()#检索第一个加减表达式
    if re.search('\+',s):
        resuit = float(s.split('+')[0])+float(s.split('+')[1])#以“+”号为分隔符进行分割 并 对分割后的值进行浮点格式化、加法运算
        string = string.replace(s,str(resuit),1)#对表达式中的元素进行替换，将计算结果替换对应的程式
    elif re.search('-',s):
        resuit = float(s.split('-')[0])-float(s.split('-')[1])#以“-”号为分隔符进行分割 并 对分割后的值进行浮点格式化、减法运算
        string = string.replace(s,str(resuit),1)#对表达式中的元素进行替换，将计算结果替换对应的程式
    return add_sub(string)#对方法进行迭代计算 并return返回计算的结果


def compute(string):
    string = mul_div(string)#计算乘除
    string = add_sub (string) #计算加减
    return string #返回值


def remove_bracket (string):
    string = user_func1(string)#调用格式化表达式方法user_func1（）对表达式进行格式化
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',string):#如果未检索到括号 则 return 计算结果
        return compute(string)
    s = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',string).group() #检索内层括号
    ds = s.strip('\(\)')#剔除掉表达式的括号便于计算
    resut = compute(ds)#将括号内的表达式交给计算程序进行计算
    string = string.replace(s,resut,1)#将计算出的结果替换掉该括号表达式
    return remove_bracket (string)#迭代执行括号剥离方法、计算出括号内的结果、将结果替换掉原表达式
if __name__ == '__main__':
   print(remove_bracket (string))