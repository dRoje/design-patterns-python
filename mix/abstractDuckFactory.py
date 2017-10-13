from abc import ABCMeta, abstractmethod


class AbstractDuckFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createMallardDuck(self): pass

    @abstractmethod
    def createRedheadDuck(self): pass

    @abstractmethod
    def createDuckCall(self): pass

    @abstractmethod
    def createRubberDuck(self): pass


