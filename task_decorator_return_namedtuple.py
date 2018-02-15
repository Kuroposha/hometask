"""
Домшняя работа. 13.02.18
Задача 3.
Возвращение блудного именованного кортежа

Требуется реализовать декоратор с параметрами return_namedtuple, который в случае,
если функция возвращает кортеж, подменяет его именованным кортежем. Имена задаются в
параметрах декоратора.

Для проверки типа данных переменной использовать функцию isinstance(переменная, тип).

Именованный кортеж находится в стандартном модуле collections.

(!) Декоратор универсальный, количество имен в кортеже переменное.
"""
from collections import namedtuple

def return_namedtuple(*tup_arg): # рабоатет
    """Декоратор с параметрами для кортежа"""
    def decorator(func):
        """Декоратор для функции"""
        def wrapper(*args, **kwargs):
            """Мой любимый враппер"""
            result = func(*args, **kwargs)
            if isinstance(result , tuple):
                klassnoe_name = namedtuple('ostroumnoe_name', list(tup_arg))
                result = klassnoe_name(*result)
            return result
        return wrapper
    return decorator
# @return_namedtuple('one', 'two', 'three')
# def func():
#     return 1, 2, 3
# #
# # r = func()
# # print(r.three) # 3
