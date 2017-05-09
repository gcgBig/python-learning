# -*- coding: utf-8 -*-
# 通过名字排序
def by_name(t):
    return t[0].lower()

# 通过成绩由高到低排序
def by_score(t):
    return t[1] * -1

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key = by_name)
print(L2)

L3 = sorted(L, key = by_name)
print(L3)