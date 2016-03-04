#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    hobbie = 'ddd'
class Cat(Animal):
    def talk(self):
        return 'Meow!'
class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'
d = Dog() # Dog(d) d.name = ''
c = Cat()


# def animal_talk(obj):
#     print(obj.talk())
#
# c = Cat("SanJiangMei")
# d = Dog("SanJiangYuan")
# animal_talk(c)
# animal_talk(d)
'''
animals = [Cat('Missy'),
           Dog('Lassie')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())
    '''