from iterator import Iterator
from menusIterator import MenusIterator
from menu import Menu
from typing import List


class Waitress:
    def __init__(self, menus):
        # type: (List(Menu)) -> None
        self.menus = menus

    def printMenu(self):
        menusIterator = MenusIterator(self.menus)
        while menusIterator.hasNext():
            menuIterator = menusIterator.next().createIterator()
            self.__printMenu(menuIterator)

    @staticmethod
    def __printMenu(iterator):
        # type: (Iterator) -> None
        print
        while iterator.hasNext():
            menuItem = iterator.next()
            print menuItem


