"""
Домашняя работа
3.2 Системы счисления

Реализуйте модуль number_system для перевода числа из одной системы счисления в
 другую.

Модуль должен содержать 6 функций для перевода из десятичной системы счисления в
двоичную, восьмеричную, шестнадцатиричную и наоборот:

(!) Запрещено использовать встроенные функции/методы, решающие эту задачу.

Подсказка. Не спешите писать 6 разных реализаций, подумайте, можно ли написать
универсальный алгоритм перевода.

В решении не должно присутствовать операций ввода-вывода.

Ситуации, когда в исходном числе есть не допустимые цифры (буквы), игнорируются.
"""
DICKT_CONWERT = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7,
                 '8' : 8, '9' : 9, 'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13,
                 'e' : 14, 'f' : 15}

# функция перевода из десятичной в любую
def dec_to(number_in, num_base):
    """
    реализация функции перевода деятичной СС в любую, заданную
    """
    num_str = ''
    if number_in == 0:
        num_str = '0'
    while number_in != 0:
        last_n = number_in % num_base
        num_str = (str(last_n) if last_n < 10 else serch_in(last_n)) + num_str
        number_in //= num_base
    return num_str

#украденная функция работы со словарем
def serch_in(hex_num):
    """
    поиск значений и подставление в словарь
    """
    for key, value in DICKT_CONWERT.items():
        if value == hex_num:
            return key

def to_dec(string_in, num_base):
    """
    реализация функции перевода из любой СС в десятичную
    """
    string_in = list(string_in) # меняю стоку на список, необязательно
    string_in_out = 0
    lon_str = len(string_in)
    for num_len in range(lon_str): #запускаю цикл проверки
        if string_in[num_len] in DICKT_CONWERT:
            string_in[num_len] = DICKT_CONWERT[string_in[num_len]]
            string_in_out += (int(string_in[num_len])) * \
                             (num_base ** (lon_str-num_len-1))
    return string_in_out

def dec2bin(number):
    '''
    перевод из 10 - 2
    '''
    return dec_to(number, 2)

def dec2oct(number):
    '''
    перевод из 10 - 8
    '''
    return dec_to(number, 8)

def dec2hex(number):
    '''
    перевод из 10 - 16
    '''
    return dec_to(number, 16)

def bin2dec(number):
    """
    перевод из 2 - 10
    """
    return to_dec(number, 2)

def oct2dec(number):
    """
    перевод из 8 - 10
    """
    return to_dec(number, 8)

def hex2dec(number):
    """
    перевод из 16 - 10
    """
    return to_dec(number, 16)
