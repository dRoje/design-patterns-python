from abc import ABCMeta, abstractmethod


class Beverage:
    __metaclass__ = ABCMeta
    TALL = 'TALL'
    GRANDE = 'GRANDE'
    VENTI = 'VENTI'

    def __init__(self):
        self.description = "Unknown Beverage"
        self.size = Beverage.TALL

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self): return 0

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size
