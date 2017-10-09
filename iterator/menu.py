from abc import ABCMeta, abstractmethod
from iterator import Iterator


class Menu:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createIterator(self):
        # type: ()-> Iterator
        pass


