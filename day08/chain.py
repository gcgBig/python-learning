# -*- coding: utf-8 -*-
# 动态调用url
class Chain(object):
    """docstring for Chain"""
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda name: Chain('%s/users/%s' % (self.path, name))
        else:
            return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.users('gcg').timeline.list)
