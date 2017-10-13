from menuItem import MenuItem
from menu import Menu
from iterator import Iterator
from cafeMenuIterator import CafeMenuIterator


class CafeMenu(Menu):
    def __init__(self):
        self.menuItems = {}

        self.addItem("Veggie Burger and Air Fries",
                     "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
                     True, 3.99)
        self.addItem("Soup of the day",
                     "A cup of the soup of the day, with a side salad",
                     False, 3.69)
        self.addItem("Burrito",
                     "A large burrito, with whole pinto beans, salsa, guacamole",
                     True, 4.29)

    def addItem(self, name, description, vegetarian, price):
        # type: (str, str, bool, float) -> None
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.update({menuItem.getName(): menuItem})

    def createIterator(self):
        # type: () -> Iterator
        return CafeMenuIterator(self.menuItems.values())

