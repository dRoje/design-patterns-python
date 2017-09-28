from abc import ABCMeta, abstractmethod

import ingredients


class PizzaIngredientFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createDough(self): pass

    @abstractmethod
    def createSauce(self): pass

    @abstractmethod
    def createCheese(self): pass

    @abstractmethod
    def createVeggies(self): pass

    @abstractmethod
    def createPepperoni(self): pass

    @abstractmethod
    def createClam(self): pass



class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ingredients.ThinCrustDough()

    def createSauce(self):
        return ingredients.MariniaraSauce()

    def createCheese(self):
        return ingredients.ReggianoChesse()

    def createVeggies(self):
        veggies = [ingredients.Garlic(), ingredients.Onion(), ingredients.Mashroom(), ingredients.RedPepper()]
        return veggies

    def createPepperoni(self):
        return ingredients.SlicedPepperoni()

    def createClam(self):
        return ingredients.FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ingredients.ThickCrustDough()

    def createSauce(self):
        return ingredients.PlumTomatoSauce()

    def createCheese(self):
        return ingredients.Mozzarella()

    def createVeggies(self):
        veggies = [ingredients.EggPlant(), ingredients.Olives(), ingredients.Spinach(), ingredients.RedPepper()]
        return veggies

    def createPepperoni(self):
        return ingredients.SlicedPepperoni()

    def createClam(self):
        return ingredients.FrozenClams()
