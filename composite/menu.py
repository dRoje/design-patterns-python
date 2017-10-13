from abc import ABCMeta
from menuComponent import MenuComponent
from menuComponentIterator import MenuComponentIterator
from compositeIterator import CompositeIterator


class Menu(MenuComponent):
    __metaclass__ = ABCMeta

    def __init__(self, name, description):
        # type: (str, str) -> None
        self.name = name
        self.description = description
        self.menuComponents = []

    def add(self, menuComponent):
        # type: (MenuComponent)-> None
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        # type: (MenuComponent)-> None
        self.menuComponents.remove(menuComponent)

    def getChild(self, i):
        # type: (int)-> None
        return self.menuComponents.__getitem__(i)

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def __str__(self):
        string = self.getName() + ", " + self.getDescription() + " -- \n"
        for menuComponent in self.menuComponents:
            string += str(menuComponent)
        return string + "\n"

    def createIterator(self):
        return CompositeIterator(MenuComponentIterator(self.menuComponents))



