#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie


from  backend.db.sql_api import select
def homepage():
    print("welcome to home page")
    q_data = select("user","dd")
    print("query res:",q_data)
def tv():
    print("welcome to tv page")

def movie():
    print("welcome to movie page")
