#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Foo(object):
    def __init__(self):
        print('___init__')
        self.n =4
    #def __new__(cls, *args, **kwargs):
    #    print('---new---')
    #def __call__(self, *args, **kwargs):

    #    print('__call__')
    def test(self):
        print('---test---')

obj = Foo() # 执行 __init__
#obj()       # 执行 __call__
#print(type(Foo))
#print(type(obj))

class Foo:
    print('foo')

MyShinyClass = type('MyShinyClass', (Foo,), {"test":123,"name":'alex'})
print(type(MyShinyClass))
a =MyShinyClass()
print(MyShinyClass.test)
#print(dir())
