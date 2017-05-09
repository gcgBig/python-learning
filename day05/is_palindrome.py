# -*- coding: utf-8 -*-
# 判断是否为回文数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 100000))
print(list(output))