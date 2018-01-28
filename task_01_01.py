"""
Домашняя работа
1.1 Високосный год
"""

YEAR = int(input())

if ((YEAR % 100 == 0) and (YEAR % 400 != 0)) or (YEAR % 4 != 0):
    print('no')
else:
    print('yes')
