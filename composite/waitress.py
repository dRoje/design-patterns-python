from menu import Menu
from menuComponent import UnsupportedOperationException


class Waitress:
    def __init__(self, allMenus):
        # type: (Menu) -> None
        self.allMenus = allMenus

    def printMenu(self):
        print self.allMenus

    def printVegetarianMenu(self):
        print "\nVEGGIE MENU:\n------"
        iterator = self.allMenus.createIterator()
        while iterator.hasNext():
            menuItem = iterator.next()
            try:
                if menuItem.isVegetarian():
                     print menuItem
            except UnsupportedOperationException:
                pass




