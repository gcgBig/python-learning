# -*- coding: utf-8 -*-
# 正整数n次方函数
'''
def power(x, n):
    if n < 0:
        raise TypeError('请输入正整数')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
'''

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3, 6))