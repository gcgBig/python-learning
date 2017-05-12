# -*- coding: utf-8 -*-
class Fib(object):
    """docstring for Fib"""
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化计数器a, b

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    # 取特定的值
    def __getitem__(self, n): # n是索引
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    def hello(self):
        print('hello')

f = Fib()
print(f[3])
print(f[2:5])

for n in Fib():
    print(n)
