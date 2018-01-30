"""
Домашняя работа
2.3 Среднее арифметическое

Напишите функцию average(lst), которая принимает список из чисел, и вычисляет
среднее арифметическое элементов этого списка.

Среднее арифметическое определяется как сумма элементов, деленная на их
количество.

С помощью встроенной функции round, округлите возвращаемое значение до тысячных.

Требуется реализовать только функцию, решение не должно осуществлять операций
ввода-вывода.

"""
def average(lst):
    """функция среднее значение"""
    sr_znach = round(sum(lst) / len(lst), 3)
    return sr_znach


# print(average([14, 8, 3, 1, 89, 2, 45]))
# print(average([0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]))