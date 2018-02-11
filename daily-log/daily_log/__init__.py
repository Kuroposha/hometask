import sys

from daily_log import storage


get_connection = lambda: storage.connect('daily_task.sqlite')


def action_show_menu():
    """Вывод меню"""
    print(
    '''
    0. Выход
    1. Показать меню
    2. Вывести список задач
    3. Добавить задачу
    4. Отредактировать задачу
    5. Завершить задачу
    6. Начать задачу сначала
    '''
    )


def action_add_t():# УРА! это дерьмо наконец то заработало!
    """Добавить задачу"""
    name_task = input('\nВведите название задачи: ')

    answ = input("\nВы хотите ввести описание поставленной задачи? (да/ нет)")
    if answ == 'да':
        description_t = input("\nВведите описание задачи: ")
    else:
        description_t = name_task
    with get_connection() as conn:
        name = storage.add_task(conn, name_task, description_t)
    print('\nНовая задача добавлена в ежедневник!')


def action_show_tl():# УРА! это дерьмо наконец то заработало!
    """Вывести список задач"""
    with get_connection() as conn:
        all_tasks = storage.find_all(conn)
    id_t = 1
    for id_t in all_tasks:
        visual = '{id_t[id]} - {id_t[name]} - {id_t[description]} - {id_t[plan_date]} - {id_t[status]}'
        print(visual.format(id_t=id_t))


def action_edit_t():# УРА! это дерьмо наконец то заработало!
    """Отредактировать задачу"""
    """Идея в том, что редактировать закртые задачи нельзя! Поэтому нужна выборка по открытым
    задачам. Редактировать в них можно название, описание и дату на любую, кроме прошлого
    нужно предложить пользователю список открытых задач, или сразу ввести название или номер"""
    answ = input('\nВы знаете номер задачи, которую хотите отредактировать? да/ нет: ')
    if answ == 'да':
        id_t = int(input('\nВведите номер задачи для редактирования: '))
    else:
        print('Выберете задачу из списка:\n')
        with get_connection() as conn:
            all_open_tasks = storage.find_for_status_task(conn, 0)

        for id_t in all_open_tasks:
            visual = '{id_t[id]} - {id_t[name]} - {id_t[description]}'
            print(visual.format(id_t=id_t))

        id_t = input('\nВведите номер задачи для редактирования: ')
    name_task = input('\nВведите новое имя задачи: ')
    description_t = input('\nВведите новое описание задачи: ')

    with get_connection() as conn:
        name = storage.change_task_options(conn, name_task, description_t, id_t)


def action_replay_t():# УРА! это дерьмо наконец то заработало!
    """Начать задачу заново"""
    """Идея в том, что нельзя начать заново то. что еще не закончено. И пока я писала предыдущие тексты
    я решила, что нет смысла делать отбор по имени и пошла менять все, что есть на айди
    также список или номер"""
    answ = input('\nВы знаете номер задачи, которую хотите начать заново? да/ нет: ')
    if answ == 'да':
        id_t = int(input('\nВведите номер задачи для перезапуска: '))
    else:
        print('Выберете задачу из списка:\n')
        with get_connection() as conn:
            all_close_tasks = storage.find_for_status_task(conn, 1)
"""когда нибудь я вынесу это в отдельную функцию, но пока работает"""
        for id_t in all_close_tasks:
            visual = '{id_t[id]} - {id_t[name]} - {id_t[description]}'
            print(visual.format(id_t=id_t))

        id_t = int(input('\nВведите номер задачи для перезапуска: '))

    with get_connection() as conn:
        status_t = storage.change_status_task(conn, 0, id_t)



def action_close_t():# УРА! это дерьмо наконец то заработало!
    """Завершить задачу"""

    """Идея в том, что завершить можно только открытую задачу. Поэтому нужна выборка по
    открытым задачам и одновременно с этим по имени или айди задачи. НУжно предложить пользователю Вывести
    айди, имя или список открытых задач."""
    answ = input('\nВы знаете номер задачи, которую хотите завершить? да/ нет: ')
    if answ == 'да':
        id_t = int(input('\nВведите номер задачи для завершения: '))
    else:
        print('Выберете задачу из списка:\n')
        with get_connection() as conn:
            all_open_tasks = storage.find_for_status_task(conn, 0)

        for id_t in all_open_tasks:
            visual = '{id_t[id]} - {id_t[name]} - {id_t[description]}'
            print(visual.format(id_t=id_t))

        id_t = int(input('\nВведите номер задачи для завершения: '))

    with get_connection() as conn:
        status_t = storage.change_status_task(conn, 1, id_t)


def action_exit():
    """Завершить работу программы"""
    print("Спасибо за работу. До новых встреч!")
    sys.exit(0)

def main_dl():
    """Запуск программы ежедневника"""
    print('''
    Ежедневник.
    Главное меню.
    ''')
    with get_connection() as conn:
        storage.initualize(conn)

        actions = {
            '0': action_exit,
            '1': action_show_menu,
            '2': action_show_tl,
            '3': action_add_t,
            '4': action_edit_t,
            '5': action_close_t,
            '6': action_replay_t,
        }

        action_show_menu()

        while True:
            num_act = input('\nВведите номер меню: \n')
            func = actions.get(num_act)

            if func:
                func()
            else:
                print('Номер меню задан неверно')
