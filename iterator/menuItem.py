class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        # type: (str, str, bool, float) -> None
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def isVegetarian(self):
        return self.vegetarian

    def getPrice(self):
        return self.price

    def __str__(self):
        return self.getName() + ", " + self.getDescription() + " -- " + str(self.getPrice())
