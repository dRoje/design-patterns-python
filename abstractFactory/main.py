from pizzaStores import NYStylePizzaStore, ChicagoStylePizzaStore


nyPizzaStore = NYStylePizzaStore()
chicagoPizzaStore = ChicagoStylePizzaStore()

nyPizza = nyPizzaStore.orderPizza('cheese')
print nyPizza.getName()

print

chicagoPizza = chicagoPizzaStore.orderPizza('cheese')
print chicagoPizza.getName()
