#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  os,sys
pathdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(pathdir)

from config import  settings
def db_auth(configs):
    if configs.DATABASE["user"] == "root" and configs.DATABASE["password"] == "123":
        print("db authentication passed!")
        return  True

    else:
        print("auth error")

def select(table,column):
    if db_auth(settings):
        if table == "user":
            user_info = {
                "001":["tom",22,"IT"],
                "002":["JACK",18,"IT"]
            }
            return user_info