"""
меняем меню
"""
import sys
from abc import ABCMeta, abstractmethod

#from daily_log import storage
#get_connection = lambda: storage.connect('daily_task.sqlite')

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

@Command.command('exit')
class ExitCommand(Command):
    def execute(self):
        pass

#
# class ShowCommand(Command):
#     pass

@Command.command('menu')
class MenuCommand(Command):
    pass

@Command.command('list')
class ListCommand(Command):
    def execute(self):
        pass


@Command.command('add')
class AddCommand(Command):
    pass


@Command.command('edit')
class EditCommand(Command):
    pass


@Command.command('close')
class CloseCommand(Command):
    pass


@Command.command('replay')
class ReplayCommand(Command):
    pass


class Menu(metaclass=ABCMeta):
