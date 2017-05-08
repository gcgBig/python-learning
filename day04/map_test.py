# -*- coding: utf-8 -*-
# map的用法
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))