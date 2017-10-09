from iterator import Iterator
from menu import Menu


class Waitress:
    def __init__(self, pancakeHouseMenu, dinerMenu):
        # type: (Menu, Menu) -> None
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu

    def printMenu(self):
        pancakeIterator = self.pancakeHouseMenu.createIterator()
        dinerIterator = self.dinerMenu.createIterator()

        print "\nBREAKFAST:"
        self.__printMenu(pancakeIterator)
        print "\nLUNCH:"
        self.__printMenu(dinerIterator)

    @staticmethod
    def __printMenu(iterator):
        # type: (Iterator) -> None
        while iterator.hasNext():
            menuItem = iterator.next()
            print menuItem


