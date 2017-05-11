# -*- coding: utf-8 -*-
class MyObject(object):
    """docstring for MyObject"""
    name = 'student'

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

s = MyObject()
print(s.name)
print(MyObject.name)
s.name = 'gcg'
print(s.name)
print(MyObject.name)
del s.name
print(s.name)