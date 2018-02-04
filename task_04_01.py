"""
Домашняя работа
4.1 Работа с файлами. Задача №1



Файл "data.txt" заполнен случайными целыми числами, числа разделены одним
пробелом.

    Сформировать файл "out-1.txt" из элементов файла "data.txt", делящихся без
    остатка на n
    Сформировать файл "out-2.txt" из элементов файла "data.txt", возведенных в
    степень p

n и p - целые числа, вводимые с клавиатуры.

"""
with open('data.txt') as f_random, \
     open('out-1.txt', 'w') as f_n, \
     open('out-2.txt', 'w') as f_p:

    n = int(input())# получить n
    p = int(input()) # получим p
    for list_1 in f_random.read().split():
        list_1_int = int(list_1)# переопределить эл-ты в инт
        if list_1_int % n == 0:# ищем кратные n
            elem_n = str(list_1_int) # превращаем значение обратно в строку
            f_n.write(elem_n + ' ') # записываем в файл out-1
        elem_p = str(list_1_int ** p) # посчитаем квадраты
        f_p.write(elem_p + ' ') # запишем полученное в файл out-2
    f_random.seek(0)
    f_n.seek(0)
    f_p.seek(0)
