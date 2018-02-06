import sys

def show_menu():
    print('''\nЕжедневник.\nГлавное меню. Выберете действие:\n
    1. Вывести список задач\n
    2. Добавить задачу\n
    3. Отредактировать задачу\n
    4. Завершить задачу\n
    5. Начать задачу сначала\n
    6. Выход''')


def task_list():
    print('1. Вывести список задач')
    # print('\nСписок текущих задач:\n')
    # return


def add_task():
    print('2. Добавить задачу')
    #return print('\nВы можете добавить новую задачу:\n')


def edit_task():
    print('3. Отредактировать задачу')
    #return print('\nВы можете отредактировать одну из созданных задач:\n')


def close_task():
    print('4. Завершить задачу')
    #return print('\nВы можете завершить одну из текущих задач:\n')


def restart_task():
    print('5. Начать задачу сначала')
    #return print('\nВы можете начать одну из предыдущих задач заново:\n')


def exit_work():
    print('6. Выход')
    sys.exit()
    #return print('\nСпасибо за работу. До новых встреч!\n')


def menu_daily_log():
    dict_of_menu = {'1': task_list,
                    '2': add_task,
                    '3': edit_task,
                    '4': close_task,
                    '5': restart_task,
                    '6': exit_work
                    }
    show_menu()

    while True:
        num_act = input('\nВведите номер меню:\n')
        func = dict_of_menu.get(num_act)

        if func:
            func()
        else:
            print('Номер меню задан неверно')
