# -*- coding: utf-8 -*-
# 杨辉三角
def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

o = triangles()
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
