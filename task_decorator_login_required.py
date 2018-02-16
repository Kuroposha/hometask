"""
Домашняя работа
Задание 3 декоратор с паролем
"""
import hashlib


def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


def try_to_pass(try_it):
    with open('token.txt') as f:
        iniz = f.read()
    return try_it == iniz


def login_required(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            user_check = input()
            pass_check = input()
            it_make = try_to_pass(make_token(user_check, pass_check))
            if it_make:
                break

        return func(*args, **kwargs) if it_make else None
    return wrapper
