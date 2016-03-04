#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  os,sys
pathdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(pathdir)


from  backend.logic.handle import  homepage

homepage()