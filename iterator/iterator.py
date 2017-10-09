from abc import ABCMeta, abstractmethod


class Iterator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def hasNext(self): pass

    @abstractmethod
    def next(self): pass


