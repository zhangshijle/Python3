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
        result = num1 + num2
        print(c[11])
    except ValueError as e:
        print("ValueError:",e)
    except IndentationError as e:
        print("index error:",2)
    except IndexError as e:
        print(c[4])
    except KeyboardInterrupt as e:
        print("ctrl + c")
    except Exception as e:
        print("捕获到为止异常:")
        print(e)
    finally:
        print("xxxx")