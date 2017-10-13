from menuComponent import MenuComponent
from typing import List


class MenuComponentIterator:
    def __init__(self, menuComponents):
        # type: (List(MenuComponent)) -> None
        self.components = menuComponents
        self.position = 0

    def next(self):
        # type: () -> MenuComponent
        menuComponent = self.components[self.position]

        self.position += 1
        return menuComponent

    def hasNext(self):
        if self.position >= self.components.__len__() or self.components[self.position] is None:
            return False
        else:
            return True


