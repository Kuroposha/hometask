"""
Домашняя Работа
Декоратор пауза
Требуется реализовать декоратор с параметрами pause, который приостанавливает
 выполнение функции на указанное количество секунд.

В решении пригодится стандартный модуль time.
"""
import time

def pause(sec):
    """Декоратор с параметрами pause"""
    def decorator(func):
        def wrapper(*args, **kwargs):
        """love this wrapper"""
            time.sleep(sec)
            return func(*args, **kwargs)
        return wrapper
    return decorator
