"""
Напишите функцию get_quadrant_number, которая принимает координаты точки X и Y и
возвращает номер четверти, которой эта точка принадлежит. Помните, что если точка
лежит на оси, то она не принадлежит ни одной четверти,
в этом случаи нужно выбросить исключение типа ValueError без сообщения об ошибке.
"""
def get_quadrant_number(X, Y):
    if X > 0 and Y > 0:
        quadrant = 1
    elif X < 0 and Y > 0:
        quadrant = 2
    elif X < 0 and Y < 0:
        quadrant = 3
    elif X > 0 and Y < 0:
        quadrant = 4
    elif X == 0 or Y == 0:
        raise ValueError
    return quadrant
