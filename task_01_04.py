"""
Домашняя работа
1.4 Прямоугольный треугольник
"""

TOP1_X = int(input())
TOP1_Y = int(input())
TOP2_X = int(input())
TOP2_Y = int(input())
TOP3_X = int(input())
TOP3_Y = int(input())

# Определим координаты векторов

VEKTOR12_X = TOP2_X - TOP1_X
VEKTOR12_Y = TOP2_Y - TOP1_Y
VEKTOR23_X = TOP3_X - TOP2_X
VEKTOR23_Y = TOP3_Y - TOP2_Y
VEKTOR13_X = TOP3_X - TOP1_X
VEKTOR13_Y = TOP3_Y - TOP1_Y

# Отыщем скалярное произведение векторов

SKA_VEK_12_13 = VEKTOR12_X * VEKTOR13_X + VEKTOR12_Y * VEKTOR13_Y
SKA_VEK_13_23 = VEKTOR13_X * VEKTOR23_X + VEKTOR13_Y * VEKTOR23_Y
SKA_VEK_12_23 = VEKTOR12_X * VEKTOR23_X + VEKTOR12_Y * VEKTOR23_Y

# Проверим прямоугольность

if SKA_VEK_12_13 == 0 or SKA_VEK_12_23 == 0 or SKA_VEK_13_23 == 0:
    print('yes')
else:
    print('no')
