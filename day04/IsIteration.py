# -*- coding: utf-8 -*-
# 判断是否可以迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))