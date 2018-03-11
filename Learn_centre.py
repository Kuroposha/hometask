"""
Домашка на понедельник (26.02.18)
Задача №1. Учебный центр

Перенести в ОО-код следующий пример из реального мира:
- есть курсы, учителя и ученики
- у каждого курса есть свой учитель
- у каждого учителя есть своя группа учеников

Определите какие объекты есть в этом примере, какие у них
свойства и какие методы, как эти объекты будут между собой
взаимодействовать, например, к курсу можно добавить учителя.
Создайте все необходимые классы и приведите пример их
использования.
"""
from abc import ABCMeta, abstractmethod
from datetime import datetime


class Human(metaclass=ABCMeta):
    """ """
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Course(object):
    """создаем основу курса """
    def __init__(self, subject, date_start, duration, location, cost):
        self.subject = subject
        self.date_start = date_start
        self.duration = duration
        self.location = location
        self.cost = cost


    def get_teacher(self, teacher):
         if isinstance(teacher, Teacher):
            self.teacher = teacher.name
        else:
            print('Преподаватель {} не преподает в нашем учебном заведении'.format(teacher.name))


    def get_group(self, group):
         if isinstance(group, Group):
            self.group = group.name
        else:
            print('Группа {} не была сформирована'.format(group.name))


    # def get_programm(*subject, **programm):
    #     """для расписания"""
    def start_course(date_start, duration):
        '''стартуем курс'''
        if isinstance(teacher, Teacher) and isinstance(group, Group):
            date_defense = date_start + duration
            print('Курс по дисциплине "{}" начался.'.format(subject))
            print('Группа "{}".'.format(group))
            print('Преподаватель "{}".'.format(teacher))
            print('Защита курсовых запланирована на "{}"'.format(date_defense))


class Teacher(Human):
    """Учитель - тоже человек!"""
    subjects = {}
    def __init__(self, name, age, exp):
        super().__init__(name)
        super().__init__(age)
        self.exp = exp
        self.subjects = subjects


    def add_subjects(self, subject):
        self.subjects[len(self.subjects)+1] = subject


    def get_course(self, course):
        if isinstance(course, Course):
            self.course = course.subject
        else:
            print('Курс {} не был сформирован'.format(course.subject))

    # def setting_hometask():
    #     pass
    #
    #
    # def set_mark():
    #     pass


class Group(object):
    """ """
    def __init__(self, name):
        self.__students = {}


    def add_student(self, student):
        if isinstance(student, Student):
            self.__students[len(self.__students)+1] = student.name
        else:
            print()


class Student(Human):
    """ """
    courses = {}
    def __init__(self, name, age):
        super().__init__(name)
        super().__init__(age)


    def get_course(self, course):
        pass

    def get_capt_status(self, capitan):
        self.capitan = True

    # def get_contact(self, contact):
    #     pass
    #

    # def do_hometask():
    #     pass
