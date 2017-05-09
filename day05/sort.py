# -*- coding: utf-8 -*-
# 排序
print(sorted([36, 95, -3, 0, 18]))

# 按绝对值排序
print(sorted([36, 95, -3, 0, 18], key = abs))

# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

# 忽略大小写，反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))