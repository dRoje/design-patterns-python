from abc import ABCMeta, abstractmethod


class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass


class NoCommand(Command):
    def execute(self): pass

    def undo(self): pass




