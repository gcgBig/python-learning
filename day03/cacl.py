# -*- coding: utf-8 -*-
# 计算数的平方相加
'''
def cacl(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
'''

# 可变参数
def cacl(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#print(cacl([1, 3, 6, 5]))
#print(cacl(1, 3, 53, 2))

nums = [1, 2, 3]
print(cacl(*nums))