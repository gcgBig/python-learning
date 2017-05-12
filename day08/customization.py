# -*- coding: utf-8 -*-
class Student(object):
    """docstring for Student"""
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Student name is: %s' % self._name

    def __getattr__(self, attr):
        if attr == 'score': # 返回属性
            return 99
        if attr == 'age':
            return lambda: 25 # 返回函数
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        print('My name is %s' % self._name)

s = Student('gcg')
print(s)
print(s())
print(s.score)
print(s.age())
#print(s.abc)