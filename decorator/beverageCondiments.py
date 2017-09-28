from beverageCondiment import CondimentDecorator
from beverage import Beverage
from costMapping import CostMapping, MochaCostMapping


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        CondimentDecorator.__init__(self)
        self.costMapping = MochaCostMapping
        assert isinstance(beverage, Beverage)
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + self.costMapping.getCost(self.beverage.getSize())


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        CondimentDecorator.__init__(self)
        self.costMapping = CostMapping
        assert isinstance(beverage, Beverage)
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return self.beverage.cost() + self.costMapping.getCost(self.beverage.getSize())
