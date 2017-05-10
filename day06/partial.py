# -*- coding: utf-8 -*-
# 转换二进制
import functools

'''
def int2(x, base = 2):
    return int(x, base)
'''
# 偏函数
int2 = functools.partial(int, base = 2)

print(int2('10000000000000000000'))
print(int2('10101010101010101010'))

print(int2('1000000', base = 10))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))