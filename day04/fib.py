# -*- coding: utf-8 -*-
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

'''
f = fib(1000)
for s in f:
    print(s)
'''

g = fib(10)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break