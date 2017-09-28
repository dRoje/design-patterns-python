from pizza import Pizza
from pizzaIngredientFactory import PizzaIngredientFactory


class ClamPizza(Pizza):
    def __init__(self, ingredientFactory):
        Pizza.__init__(self)
        assert isinstance(ingredientFactory, PizzaIngredientFactory)
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print "Preparing " + self.name
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()


class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        Pizza.__init__(self)
        assert isinstance(ingredientFactory, PizzaIngredientFactory)
        self.ingredientFactory = ingredientFactory

    def cut(self):
        print "Cut pizza into squares"

    def prepare(self):
        print "Preparing " + self.name
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.pepperoni = self.ingredientFactory.createPepperoni()


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory):
        Pizza.__init__(self)
        assert isinstance(ingredientFactory, PizzaIngredientFactory)
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print "Preparing " + self.name
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.pepperoni = self.ingredientFactory.createPepperoni()