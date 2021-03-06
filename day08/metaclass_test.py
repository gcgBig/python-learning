# -*- coding: utf-8 -*-
# metaclass模板
class ListMetaclass(type):
    """docstring for ListMetaclass"""
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)