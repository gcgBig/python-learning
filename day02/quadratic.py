# -*- coding: utf-8 -*-
# 求一元二次方程组的解
import math

def quadratic(a, b, c):
    if not (isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(c, (float, int))):
        raise TypeError('参数错误')
    if (a == 0 and b == 0 and c != 0):
        raise TypeError('没有二次项和一次项时，常数项不能为空')
    deat = b * b - 4 * a * c
    if (deat < 0):
        raise TypeError('德尔塔小于0，没有解')
    elif (deat == 0):
        x = -b + math.sqrt(deat) / 2 / a
        return x
    else:
        x = -b + math.sqrt(deat) / 2 / a
        y = -b - math.sqrt(deat) / 2 / a
        return x, y

# print(quadratic('a', 2, 3)) # 第一种错误
# print(quadratic(0, 0, 3)) # 第二种错误
# print(quadratic(1, 2, 3)) # 第三种错误
# print(quadratic(1, 4, 4)) # 一个解
print(quadratic(1, 5, 4)) # 二个解

a = float(print('请输入二次项系数：'))
b = float(print('请输入一次项系数：'))
c = float(print('请输入常数项系数：'))
print('该二项式的解为：', quadratic(a, b, c))
