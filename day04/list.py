# -*- coding: utf-8 -*-
# [1*1, 2*2, 3*3...10*10]

'''
L = []
for x in range(1, 11):
    L.append(x * x)
'''
# L = [x * x for x in range(1, 11)] # 取1-10的平方
# L = [x * x for x in range(1, 11) if x % 2 == 0] # 取偶数的平方
# L = [m + n for m in 'ABC' for n in 'XYZ'] # 双层循环
'''
d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
L = [k + '=' + v for k, v in d.items()] # 使用两个变量生成列表
'''
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L] # 变成小写
print(L)