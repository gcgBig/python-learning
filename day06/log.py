# -*- coding: utf-8 -*-
import functools
'''
# 前后都打印日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call:')
        func(*args, **kw)
        print('end call:')
    return wrapper
'''

# 可加可不加参数
def log(funcOrstr):
    if isinstance(funcOrstr, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s call %s:' % (funcOrstr, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(funcOrstr)
        def wrapper(*args, **kw):
            print('call %s:' % funcOrstr.__name__)
            return funcOrstr(*args, **kw)
        return wrapper

@log
def now():
    print('2017-05-10')

@log('excute')
def now1():
    print('2017-05-10')

now()
now1()
print(now.__name__)