from abc import ABCMeta, abstractmethod


class State:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insertQuarter(self): pass

    @abstractmethod
    def ejectQuarter(self): pass

    @abstractmethod
    def turnCrank(self): pass

    @abstractmethod
    def dispense(self): pass


