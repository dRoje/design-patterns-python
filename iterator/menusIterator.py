from iterator import Iterator
from menu import Menu
from typing import List


class MenusIterator(Iterator):
    def __init__(self, menus):
        # type: (List(Menu)) -> None
        assert isinstance(menus, list)
        self.menus = menus
        self.position = 0

    def next(self):
        # type: () -> Menu
        menu = self.menus[self.position]
        self.position += 1
        return menu

    def hasNext(self):
        if self.position >= self.menus.__len__() or self.menus[self.position] is None:
            return False
        else:
            return True

