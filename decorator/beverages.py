from beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.description = "Espresso"

    def cost(self):
        return 1.99


class DarkRoast(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.description = "Dark Roast"

    def cost(self):
        return 1.59


class HouseBlend(Beverage):
    def __init__(self):
        Beverage.__init__(self)
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89