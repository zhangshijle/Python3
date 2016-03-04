#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

import  hashlib

m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.hexdigest())

m.update(b"xxx")
print(m.hexdigest())

hash = hashlib.sha512()
hash.update(b"xxx")
print(hash.hexdigest())

'''
#python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
import hmac
h = hmac.new(b'passwprd')
h.update(b'password')
print(h.hexdigest())

'''