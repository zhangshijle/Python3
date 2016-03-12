#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
while True:
    try:
        a = input("num1:")
        b = input("num2:")
        c = range(10)

        num1 = int(a)
        num2 = int(b)
        assert  num1 > num2  #必须满足的条件,满足继续向下,不满足跳出
        result = num1 + num2
        print(result)
        print(c[4])
    except ValueError as e: #值错误
        print("ValueError:",e)
    except IndexError as e: #索引错误,可以更换索引
        print(c[4])
    except KeyboardInterrupt as e: #
        print("ctrl + c")

    except Exception as e:
        print("捕获除ctrl+c/语法错误/等特殊异常以外的所有异常:")
        print(e)
    else:
        print("没有出现异常即代码执行成功3才执行")
    finally:
        print("不管有没有异常都执行")
