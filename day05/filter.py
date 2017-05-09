# -*- coding: utf-8 -*-
# filter 用法
# 筛选基数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

#去除空字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', 'B', '', None, '   ']))