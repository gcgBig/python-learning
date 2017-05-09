# -*- coding: utf-8 -*-
# 匿名函数
f = lambda x: x * x

def build(x, y):
    return lambda: x * x + y * y

print(f)
print(f(5))
print(build(3, 5)())