from abc import ABCMeta, abstractmethod


class Pizza:
    __metaclass__ = ABCMeta

    def __init__(self,):
        self.name = ""
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.clam = None
        self.pepperoni = None

    @abstractmethod
    def prepare(self): pass

    def bake(self):
        print "Bake for 25min"

    def cut(self):
        print "Cut pizza into diagonal slices"

    def box(self):
        print "Place pizza in an official PizzaStore box"

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
