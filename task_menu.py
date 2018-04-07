"""
меняем меню
"""
import sys
import time
from abc import ABCMeta, abstractmethod
from collections import OrderedDict

#from daily_log import storage
#get_connection = lambda: storage.connect('daily_task.sqlite')
class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):
    __command = {}

    @abstractmethod
    def _do_execute(self):
        pass

    def execute(self):
        #
        #
        self._do_execute()
        #

    @staticmethod
    def command(name):
        def decorator(cls):
            if not name:
                raise RuntimeError

            if not issubclass(cls, Command):
                raise TypeError

            Command.__commands[name] = cls
            return cls

        return decorator

    @classmethod
    def get_instance(cls, name, *args, **kwargs):

        klass = cls.__command.get(name)

        if not klass:
            raise NameError

        return klass(*args, **kwargs)
#
# @Command.command('exit')
# class ExitCommand(Command):
#     def execute(self):
#         pass

@Command.command('show')
class ShowCommand(Command):
    pass
#
# @Command.command('menu')
# class MenuCommand(Command):
#     pass

@Command.command('list')
class ListCommand(Command):
    def execute(self):
        pass
#
#
# @Command.command('add')
# class AddCommand(Command):
#     pass
#
#
# @Command.command('edit')
# class EditCommand(Command):
#     pass
#
#
# @Command.command('close')
# class CloseCommand(Command):
#     pass
#
#
# @Command.command('replay')
# class ReplayCommand(Command):
#     pass


class Menu(object):
    # __command = {}
    def __init__(self):
        self.commands = OrderedDict({})


    def add_command(self, name, klass):

        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

        self.commands[name] = klass


    def execute(self, name, *args, **kwargs):
        command = self.commands.get(name)

        if not command:
            raise CommandException('Command with name "{}" not found'.format(name))
        return command().execute(*args, **kwargs)

    def __iter__(self):
        self.__copy = self.commands.copy()
        return self

    def __next__(self):
        while self.__copy:
            return self.__copy.popitem()
            sleep(1)
        raise StopIteration
