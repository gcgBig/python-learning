# -*- coding: utf-8 -*-
from types import MethodType

class Student(object):
    __slots__ = ('name', 'age') # 限制可以添加的属性
    pass

s = Student()
s.name = 'gcg'
# s.score = 100 # error
print(s.name)

def set_age(self, age):
    self.age = age

# s.set_age = MethodType(set_age, s) 实例绑定函数
Student.set_age = set_age # 类绑定函数
s.set_age(25)
print(s.age)

s2 = Student()
s2.set_age(25)
print(s.age)