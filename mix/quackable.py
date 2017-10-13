from abc import ABCMeta, abstractmethod
from quackObservable import QuackObservable


class Quackable(QuackObservable):
    # interface
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self): pass


