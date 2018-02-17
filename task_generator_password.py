"""
Домашняя работа
Генератор случайных паролей.
Требуется реализовать генератор случайных паролей указанной длины.
В пароле можно использовать любые символы в верхнем и нижнем регистре.
Например: password_generator(16), вернет случайный пароль длиной 16 символов.
Пригодится стандартный модуль random
В решении не должно присутствовать операций ввода-вывода.

"""
import random
from string import digits, ascii_letters, punctuation

def password_generator(len_pass):
    '''генератор паролей'''
    alphabet_of_pass = list(digits + ascii_letters + punctuation)
    while True:
        new_pass = ('')
        list_of_n_pass = []
        for i in range(len_pass):
            new_simb = random.choice(alphabet_of_pass)
            list_of_n_pass.append(new_simb)
        new_pass = ''.join(list_of_n_pass)
        yield new_pass
        # нужна последовательность из любых символов в регистрах
