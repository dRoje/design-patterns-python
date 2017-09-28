import pizzaIngredientFactory
import pizzas
from pizzaStore import PizzaStore


class NYStylePizzaStore(PizzaStore):
    def createPizza(self, type):
        pizza = None
        ingredientFactory = pizzaIngredientFactory.NYPizzaIngredientFactory()
        if type == "cheese":
            pizza = pizzas.CheesePizza(ingredientFactory)
            pizza.setName("New York Style Cheese Pizza")
        if type == "pepperoni":
            pizza = pizzas.PepperoniPizza(ingredientFactory)
            pizza.setName("New York Style Pepperoni Pizza")
        return pizza


class ChicagoStylePizzaStore(PizzaStore):
    def createPizza(self, type):
        pizza = None
        ingredientFactory = pizzaIngredientFactory.ChicagoPizzaIngredientFactory()
        if type == "cheese":
            pizza = pizzas.CheesePizza(ingredientFactory)
            pizza.setName("Chicago Style Cheese Pizza")
        if type == "pepperoni":
            pizza = pizzas.PepperoniPizza(ingredientFactory)
            pizza.setName("Chicago Style Pepperoni Pizza")
        return pizza