from iterator import Iterator
from dinerMenuIterator import DinerMenuIterator
from menuItem import MenuItem
from menu import Menu


class PancakeMenu(Menu):
    def __init__(self):
        self.menuItems = []

        self.addItem("K&B's Pancake Breakfast",
                     "Pancakes with scrambled eggs, and toast",
                     True,
                     2.99)

        self.addItem("Regular Pancake Breakfast",
                     "Pancakes with fried eggs, sausage",
                     False,
                     2.99)

        self.addItem("Blueberry Pancakes",
                     "Pancakes made with fresh blueberries, and blueberry syrup",
                     True,
                     3.49)

        self.addItem("Waffles",
                     "Waffles, with your choice of blueberries or strawberries",
                     True,
                     3.59)

    def addItem(self, name, description, vegetarian, price):
        # type: (str, str, bool, float) -> None
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)

    def getMenuItems(self):
        return self.menuItems

    def createIterator(self):
        # type: () -> Iterator
        return DinerMenuIterator(self.menuItems)
