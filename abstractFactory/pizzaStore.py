from abc import ABCMeta, abstractmethod


class PizzaStore:
    __metaclass__ = ABCMeta

    def orderPizza(self, type):
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def createPizza(self, type): pass

