from abc import ABCMeta, abstractmethod
from beverage import Beverage


class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getDescription(self): pass