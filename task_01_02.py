"""
Домашняя работа
1.2 Тарелки
"""
PLATES = int(input())
SOAP = int(input())

for DISHES in range(PLATES):
    PLATES -= 1
    SOAP -= 0.5

    if PLATES > 0 and SOAP == 0:
        print('Моющее средство закончилось. Осталось', PLATES, 'тарелок')
        break
    elif PLATES == 0 and SOAP > 0:
        print('Все тарелки вымыты. Осталось', SOAP, 'ед. моющего средства')
    elif PLATES == 0 and SOAP == 0:
        print('Все тарелки вымыты, моющее средство закончилось')
