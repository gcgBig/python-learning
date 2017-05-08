# -*- coding: utf-8 -*-
# 生成器流程
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

o = odd()
next(o)
next(o)
next(o)