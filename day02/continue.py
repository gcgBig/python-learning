# -*- coding : utf-8 -*-
# continue 用法
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)