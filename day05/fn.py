# -*- coding: utf-8 -*-
# 把list转换为整数
from functools import reduce

'''
def fn(x, y):
    return x * 10 + y
'''

def char2num(s):
    return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]

''' 整合版
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]
    return reduce(fn, map(char2num, s))
'''

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# print(reduce(fn, [1, 3, 5, 7, 9]))
print(str2int('1234598754'))