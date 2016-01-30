#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

'''
data = "daemon:*:1:1:System Services:/var/root:/usr/bin/false"
username,*ps,sh=data.split(":")
#print(username,*ps,sh)
sh = list(sh)
list1 = []
list1.append(sh)
print(list1)
'''


'''
name = iter(["jack","tom","list"])
print(name.__next__())
print(name.__next__())
print(name.__next__())
print(name.__next__())
'''

'''
def login(func):
    def inner(*arg,**abc):
        print("通过验证")
        return func(*arg,**abc) #返回的是func形参的内存地址,这里func的实参是tc,因此返回了tc的内存地址
    return inner

@login
def tv(*arg,**abc):
    print("欢迎%s登录tv界面")

tv = login(tv) #将tv作为函数login函数的执行参数传递过去
tv("jack","pass=123")

'''
'''

def Before(request,kargs): #第一步将函数放进内存
#第六步,在装饰器之后执行函数
#第十步执行装饰器的内部函数的参数,这次是一个外部函数
    print('before') #十一部,print结果

def After(request,kargs): #第二部放进第二个内存
#十二部执行另一个函数
    print('after')

def Filter(before_func,after_func): #第三部按照顺序放进第三个函数
#第五步执行装饰器,并将装饰器的参数执行,本次为两个函数
    def outer(main_func): #第六到装饰器里面的函数
        #第八步从return返回到这个函数
        def wrapper(request,kargs):
            #第九步执行返回对应的函数,得到request,kargs的值
            before_result = before_func(request,kargs)
            #if(before_result != None):
            #    return before_result;

            main_result = main_func(request,kargs)
            #if(main_result != None):
            #    return main_result;

            after_result = after_func(request,kargs)
            #if(after_result != None):
            #    return after_result;

        return wrapper
    return outer #第七部,装饰器里面的第一个函数返回这个函数内部的函数名,这个函数名是个未执行的内存地址
    #第十部

@Filter(Before, After) #第四部到装饰器界面
def Index(request,kargs):
    print('index')

Index("aa","bb")

'''

'''
def calc(n):
    print(n)
    if n/2 >1:
        res = calc(n/2)
        print("res:",res)
    print("N",n)
    return n
calc(10)
'''
'''

def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1 + arg2)
    arg3 = arg1 + arg2
    print(arg3)

    if arg3 < 30:
        func(arg2,arg3,stop)
func(0,1,35)

'''

'''
def search(data,n):
    mid = int(len(data)/2)
    if len(data) > 1:
        if data[mid] > n: #数据在另一半
            print("要查找的 %s 在左侧" % data[mid])
            search(data[:mid],n)
            print(mid)
        elif data[mid] < n: #数据在这一半
            print("要查找的%s 在这一伴儿" % data[mid])
            search(data[mid:],n)
            print(mid)
        else:
            print("找到了%s" % data[mid])
    else:
        print("找不到")

if __name__ == "__main__":
    data = list(range(6000000))
    search(data,1)
'''



'''
data = [[col for col in range(4)] for row in range(4)]

for i in data:
    print(i)


print("------------------------->")

for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):
        tmp = data[c_index][r_index]
        print(tmp,"tmp")
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = tmp
        print("--------============>")
    for r in data:
        print(r)


'''


'''
num = int(input("please input num: "))
a = [[i for i in range(num)] for j in range(num)]
print(a)
for i in a:
    print(i)

for i in range(num):
    for j in range(i+1,num):
        tmp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = tmp
    #print(a)

print("==============")
for i in a:
    print(i)

'''

'''
dict1 = {"name":"jack","age":18,"job":"IT"}
dict2 = {"Name":"tom","Age":20,"Job":"IT"}
dict1.update(dict2)
print(dict1.values(),"value的结果")

for i in dict1.values():
    print(i)
'''

'''

def  func():
    with open("test.txt") as f:
        try:
            while True:
                line = next(f)
                print(line,end='')
        except StopIteration:
            print("\n已经读取文件完成-->StopIteration执行")
func()

'''


'''
def func(num):
    x = 0 #定义三个变量
    y = 0
    z = 1
    while x < num: #假如x的值小于函数调用的时候传递的num的数值
        print(z) #打印z的结果
        y,z = z,y + z #将y的等于z的值,z的值等于y+z的值,即完成了后面的一个数的值是有前两个数值相加的结果
        x += 1 #然后将x的值自增1
        print("每次相加分割线--------->")
    return z #将最终z的值返回给函数名,最后函数的值就等于z
'''
'''
from collections import  Iterator
print(isinstance((10),Iterator),"10是否迭代器")
print(isinstance([],Iterator),"[]是否迭代器")
print(isinstance((),Iterator),"()是否迭代器")
print(isinstance({},Iterator),"{}是否迭代器")
print(isinstance("abcd",Iterator),"字符串abcd是否迭代器")
print(isinstance((x for x in range(10)),Iterator),"for生成的序列是否迭代器")
g1 = (x * x for x in range(10))
print(isinstance(g1,Iterator),"g1生成的序列是否迭代器")
'''
'''

def login(func):
    def inner(*arg,**abc):
        print("通过验证")
        return func(*arg,**abc) #返回的是func形参的内存地址,这里func的实参是tc,因此返回了tc的内存地址
    return inner

@login
def tv(*arg,**abc):
    print("欢迎%s登录tv界面")

tv = login(tv) #将tv作为函数login函数的执行参数传递过去
tv("jack","pass=123")
'''


def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1 + arg2)
    arg3 = arg1 + arg2
    print(arg3)

    if arg3 < 30:
        func(arg2,arg3,stop)
func(0,1,35)


