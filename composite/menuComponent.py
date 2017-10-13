from abc import ABCMeta


class UnsupportedOperationException(Exception):
    message = "Operation not supported"


class MenuComponent:
    __metaclass__ = ABCMeta

    def add(self, menuComponent):
        # type: (MenuComponent)-> None
        raise UnsupportedOperationException

    def remove(self, menuComponent):
        # type: (MenuComponent)-> None
        raise UnsupportedOperationException

    def getChild(self, i):
        # type: (int)-> None
        raise UnsupportedOperationException

    def getName(self):
        raise UnsupportedOperationException

    def getDescription(self):
        raise UnsupportedOperationException

    def getPrice(self):
        raise UnsupportedOperationException

    def isVegetarian(self):
        raise UnsupportedOperationException

    def __str__(self):
        raise UnsupportedOperationException

