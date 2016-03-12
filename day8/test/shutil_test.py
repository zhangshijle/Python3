#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  os

import shutil
a = open('test.py','rb')
b = open('new.py','wb')
shutil.copyfileobj(a,b)
a.close()
b.close()
