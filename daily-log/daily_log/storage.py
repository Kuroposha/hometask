"""работа с бд"""

import os.path as Path
import sqlite3

# запрос на добавление строки в таблицу
# запрос вывод списка текущих задач
# ЗАпрос на редакцию задачи (только невыполненные)
# запрос на завершение задачи (только невыполненные)
# запрос на перезапуск задачи  - (только выполненные с изменением даты)
# Селекты - все, все выполненные, все невыполненные, с айди
SQL_SELECT_ALL = '''
    SELECT
        id, name, description, plan_date, status
    FROM
        daily_task
'''

SQL_SELECT_ID = SQL_SELECT_ALL + ' WHERE id=?'

SQL_SELECT_STATUS = SQL_SELECT_ALL + ' WHERE status=?'

SQL_INSERT_TASK = '''
    INSERT INTO daily_task (name, description) VALUES (?, ?)
'''

SQL_UPDATE_TASK_STATUS = '''
    UPDATE daily_task SET status=? WHERE id=?
'''

SQL_UPDATE_ALL_USER_WANT = '''
    UPDATE daily_task SET name=?, description=? WHERE id=?
'''


def dict_factory(cursor, row):# УРА! это дерьмо наконец то заработало!
    """функция, магическим образом помогающая превращать нашу таблицу в словарь для красоты"""
    dict_t = {}

    for idx, col in enumerate(cursor.description):
        dict_t[col[0]] = row[idx]
    return dict_t


def connect(db_name=None):
    """Установить соединение с БД"""# УРА! это дерьмо наконец то заработало!
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initualize(conn, creation_script=None):
    """Инициализировать структуру БД"""# УРА! это дерьмо наконец то заработало!
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__), 'resourses', 'schema.sql')

    with conn, open(creation_script) as file_f:
        conn.executescript(file_f.read())


def add_task(conn, name_task, description_t):
    """Добавляет задачу в БД"""# УРА! это дерьмо наконец то заработало!

    if not name_task:
        raise RuntimeError('Не указано название задачи!')

    with conn:
        cursor = conn.execute(SQL_INSERT_TASK, (name_task, description_t,))
        return cursor


def find_all(conn):# УРА! это дерьмо наконец то заработало!
    """Найти все задачи"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_for_status_task(conn, status_t):
    """Ищем задачи по статусу 0\1"""
    with conn:
        cursor = conn.execute(SQL_SELECT_STATUS, (status_t,))
        return cursor.fetchall()


def change_status_task(conn, status_t, id_t):# УРА! это дерьмо наконец то заработало!
    """Тщетно пытаюсь реализовать инверсию статуса задачи"""
    if not id_t:
        raise RuntimeError('Такой задачи в списке нет!')

    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK_STATUS, (status_t, id_t,))
        return cursor


def change_task_options(conn, name_task, description_t, id_t):
    """Пытаюсь прилепить редакцию задач в Ежедневник"""
    if not id_t:
        raise RuntimeError('Такой задачи в списке нет!')

    with conn:
        cursor = conn.execute(SQL_UPDATE_ALL_USER_WANT, (name_task, description_t, id_t,))

        return cursor
