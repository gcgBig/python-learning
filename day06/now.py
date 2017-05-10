# -*- coding: utf-8 -*-
import functools
'''
# 日志打印
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-3-5')
'''

#加强版
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-9-5')

f = now
f()

# 打出函数名
print(now.__name__)
print(f.__name__)