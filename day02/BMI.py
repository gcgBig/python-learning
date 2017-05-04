# -*- coding: utf-8 -*-
# BMI算法
hei_input = input('please input your height:')
height = float(hei_input)
wei_input = input('please input your weight:')
weight = float(wei_input)
bmi = weight / height / height
if bmi <= 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')