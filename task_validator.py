"""
Домашняя работа.
Задача. Валидатор входных данных
"""
from abc import ABCMeta, abstractmethod
from datetime import datetime

class ValidatorException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class Validator(metaclass=ABCMeta):
    types = {}

<<<<<<< HEAD
    # def __init__(self, value):
    #     self.value = value
=======
#     def __init__(self, value):
#         self.value = value
>>>>>>> e52bd3d13aef08d72b520aa05fbfc94cdc6fd9b6

    @abstractmethod
    def validate(self, value):
        pass
        # return True if value==value

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Validator must have a name!')
        elif not issubclass(klass, Validator):
            raise ValidatorException(
            'Class "{}" is not Validator!'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, name):

        klass = cls.types.get(name)

        if klass is None:
            raise ValidatorException(
                'Validator with name "{}" not found'.format(name)
            )

        return klass()

class EMailValidator(Validator):
<<<<<<< HEAD
    # def __init__(self, value):
    #     super().__init__(value)
=======
#     def __init__(self, value):
#         super().__init__(value)
>>>>>>> e52bd3d13aef08d72b520aa05fbfc94cdc6fd9b6

    def validate(self, value):
        return '@' and '.' in value


class DateTimeValidator(Validator):
<<<<<<< HEAD
    # def __init__(self, value):
    #     super().__init__(value)
=======
#     def __init__(self, value):
#         super().__init__(value)
>>>>>>> e52bd3d13aef08d72b520aa05fbfc94cdc6fd9b6

    def validate(self, value):
        for key in ['%Y-%m-%d',
                    '%Y-%m-%d %H:%M',
                    '%Y-%m-%d %H:%M:%S',
                    '%d.%m.%Y',
                    '%d.%m.%Y %H:%M',
                    '%d.%m.%Y %H:%M:%S',
                    '%d/%m/%Y',
                    '%d/%m/%Y %H:%M',
                    '%d/%m/%Y %H:%M:%S'
                    ]:
            try:
                if datetime.strptime(value, key):
                    return True
            except ValueError:
                pass

        return False

Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)
