from iterator import Iterator
from dinerMenuIterator import DinerMenuIterator
from menuItem import MenuItem
from menu import Menu


class DinerMenu(Menu):
    MAX_ITEMS = 6

    def __init__(self):
        self.numberOfItems = 0
        self.menuItems = [None]*6
        self.addItem("Vegetarian BLT",
                     "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT",
                     "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day",
                     "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog",
                     "A hot dog, with saurkraut, relish, onions, topped with cheese",
                     False, 3.05)
        self.addItem("Steamed Veggies and Brown Rice",
                     "Steamed vegetables over brown rice", True, 3.99)
        self.addItem("Pasta",
                     "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
                     True, 3.89)

    def addItem(self, name, description, vegetarian, price):
        # type: (str, str, bool, float) -> None
        menuItem = MenuItem(name, description, vegetarian, price)
        if self.numberOfItems >= DinerMenu.MAX_ITEMS:
            print "Sorry menu is full"
        else:
            self.menuItems[self.numberOfItems] = menuItem
            self.numberOfItems += 1

    def createIterator(self):
        # type: () -> Iterator
        return DinerMenuIterator(self.menuItems)
