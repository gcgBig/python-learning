# -*- coding: utf-8 -*-
# 字段基类
class Filed(object):
    """docstring for Filed"""
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# string类
class StringField(Filed):
    """docstring for StringField"""
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

# int类
class IntegerField(Filed):
    """docstring for IntegerField"""
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    """docstring for ModelMetaclass"""
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model : %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Filed):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
        
class Model(dict, metaclass = ModelMetaclass):
    """docstring for Model"""
    def __init__(self, arg):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(field), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id = 12345, name = 'gcg', email = '123456@qq.com', password = '123456')
u.save()
        