# -*- coding: utf-8 -*-
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', 1, x = 1)
f2(1, 2, c = 3, d = 4, ext = None)

args = (1, 2)
kw = {'d' : 44, 'x' : 't'}
# f1(*args, **kw)
f2(*args, **kw)