dict_of_menu = { 1 : '1. Вывести список задач', 2 : '2. Добавить задачу', \
                 3 : '3. Отредактировать задачу', 4 : '4. Завершить задачу', \
                 5 : '5. Начать задачу сначала', 6 : '6. Выход' }

def menu_daily_log():
    """функция вывода меню"""
    print('Ежедневник.\nГлавное меню. Выберете действие:\n')
    for i in dict_of_menu:
        print(dict_of_menu[i])
    print('\nВведите номер действия:\n')
    num_act = int(input())
    return print(dict_of_menu.get(num_act))

def task_list():
    return print('\nСписок текущих задач:\n')

def add_task():
    return print('\nВы можете добавить новую задачу:\n')

def edit_task():
    return print('\nВы можете отредактировать одну из созданных задач:\n')

def close_task():
    return print('\nВы можете завершить одну из текущих задач:\n')

def restart_task():
    return print('\nВы можете начать одну из предыдущих задач заново:\n')

def exit_work():
    return print('\nСпасибо за работу. До новых встреч!\n')
