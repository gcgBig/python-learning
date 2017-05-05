# -*- coding: utf-8 -*-
# 关键字参数
'''
def person(name, age, **kw):
    print('name:', name, ',age:', age, ',other:', kw)
'''
# person('Michael', 30, list = [1, 2], t = 'aa')

# 自定义限制参数
'''
def person(name, age, **kw):
    if not 'city' in kw:
        raise TypeError('don\'t have city')
    if not 'job' in kw:
        raise TypeError('don\'t have job')
    print('name:', name, ',age:', age, ',other:', kw)
'''

# 传一个dict
'''
extra = {'city' : 'ningbo'}
person('gcg', '22', **extra)
'''

# 限制参数，关键字参数，后面必须输入并且带名称
'''
def person(name, age, *, city, job):
    print(name, age, city, job)

person('gcg', 22, city = 'ningbo')
'''

# 如果有一个可变参数后面关键字参数不需要*
'''
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('tt', 2, 3, 4, 6, city = 'nongbo', job = 'zhuxi')
'''

# 关键自参数不需要定义也可以
def person(name, age, *args, city = 'ningbo', job):
    print(name, age, args, city, job)

extra = {'sex' : 'man', 'school' : 'roushi'}
person('gcg', 20, extra, job = 'aa')