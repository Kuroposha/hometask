"""
Домашняя работа
Генератор чисел Фибоначчи
"""

def fibonacci(lid):
    x, y = 0, 1
    for n in range(lid):
        x, y = y, x + y
        yield x
