"""
Домашняя работа.
Задача. Валидатор входных данных
"""
from abc import ABCMeta, abstractmethod

class ValidatorException(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        
class Validator(metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def validate(value):
        return True if value==value

    @classmethod
    def get_instance(name, *args, **kwargs):

        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ValidatorException(
                'Validator with name "{}" not found'.format(ext)
            )

        return klass(name, *args, **kwargs)

class EMailValidator(Validator):
    def __init__(self, value):
        super().__init__(value)

    def validate(value):
        pass


class DateTimeValidator(Validator):
    def __init__(self, value):
        super().__init__(value)

    def validate(value):
        pass
