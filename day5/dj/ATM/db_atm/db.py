#！/usr/bin/env python
#coding:utf-8
#Author ZhangYan
from ATM.config import settings #导入settings文件


def mysql_auth(): #mysql认证
    datasource = settings.db_auth
    if datasource["host"] == "127.0.0.1" and datasource["user"] == "atm_root" and datasource["passwd"] == "123456":
        return True
    else:
        print("ATM用户认证失败")









