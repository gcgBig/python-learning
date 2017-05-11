# -*- coding: utf-8 -*-
# 学生类
class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        # 加上_就是私有
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('gcg', 52)
bart.print_score()
print(bart.get_grade())
print(bart)
print(bart.get_name())
print(bart.get_score())
print(Student)
print(bart._Student__name)