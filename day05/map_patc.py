# -*- coding: utf-8 -*-
# 首字母大写，其余小写
from functools import reduce

def normalize(name):
    return name.title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 乘积
def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 字符串转换为浮点数
def str2float(s):
    index = s.find('.', 0)
    def char2num(s):
        return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]
    def fn1(x, y):
        return x * 10 + y
    def fn2(x, y):
        return x / 10 + y
    if index == -1:
        return reduce(fn1, map(char2num, s))
    else:
        list1 = s[: index]
        list2 = s[index + 1 :]
        return reduce(fn1, map(char2num, list1)) + reduce(fn2, map(char2num, list2[::-1])) / 10

print(str2float('123.46'))
