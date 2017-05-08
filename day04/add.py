# -*- coding: utf-8 -*-
# 高阶函数
f = abs
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, f))