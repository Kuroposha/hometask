"""
Домашняя работа
4.2 Парсер HTTP-заголовков

Напишите функцию http_headers_to_json, которая принимает два аргумента:

    путь к файлу с HTTP-заголовками
    путь к файлу с результатами (в формате JSON)
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
"""
import json

def http_headers_to_json(way_to_http, way_to_result):
    """
    парсинг, файлы, жсон
    """
    dict_of_http = {}
    with open(way_to_http) as f_to_pars:

        my_file = f_to_pars.read().split('\n')
        for lines in my_file:
            try:
                list_l = lines.split(':', 1)
                key = list_l[0]
                value = list_l[1].strip(' ')
                dict_of_http[key] = value
            except IndexError:
                list_l = lines.split(' ')
                if list_l[0] == 'HTTP/1.1':
                    dict_of_http = {'protocol': list_l[0],
                                    'status_code': list_l[1],
                                    'status_message': ' '.join(list_l[2:])}#спс
                elif list_l[0] == 'HTTP/2':
                    dict_of_http = {'protocol': list_l[0],
                                    'status_code': list_l[1]}
                elif list_l[0] == 'GET':
                    dict_of_http = {'method': list_l[0],
                                    'uri': list_l[1],
                                    'protocol': list_l[2]}
    with open(way_to_result, 'w') as f_to_res:
        json.dump(dict_of_http, f_to_res, indent=4)
        
