"""
Домашняя работа

Задача №1
Повторите код из презентации. Дополните его простыми реализациями под конкретный
формат. Для простоты возьмите json и pickle. Цель заключается в том, чтобы вы
прочувствовали как оно работает.

"""
from abc import ABCMeta, abstractmethod

import os
import json
import pickle

class ParamHandlerException(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.get_all_params

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )
            cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        #Шаблон "Factory Method"

        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )

        return klass(source, *args, **kwargs)

class TextParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
        with open(self.source, 'w') as f:
            result = f.read()
        return result

    def write(self):
        with open(self.source, 'r') as f:
            f.write(self.params)

class PickleParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
        with open(self.source, 'rb') as f:
            result = pickle.load(f)
        return result

    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)

class JsonParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)

    def read(self):
        with open(self.source) as f:
            result = json.load(f)
        return result

    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)

ParamHandler.add_type("txt", TextParamHandler)
ParamHandler.add_type("pickle", PickleParamHandler)
ParamHandler.add_type("json", JsonParamHandler)
