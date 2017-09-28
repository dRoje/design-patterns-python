import beverageCondiments
import beverages

beverage1 = beverages.Espresso()
print beverage1.getDescription() + " $" + str(beverage1.cost())

beverage2 = beverages.DarkRoast()
beverage2.setSize(beverages.Beverage.VENTI)
beverage2 = beverageCondiments.Mocha(beverage2)
beverage2 = beverageCondiments.Mocha(beverage2)
beverage2 = beverageCondiments.Whip(beverage2)
print beverage2.getDescription() + " $" + str(beverage2.cost())


beverage3 = beverages.Espresso()
beverage3.setSize(beverages.Beverage.VENTI)
beverage3 = beverageCondiments.Whip(beverage3)
print beverage3.getDescription() + " $" + str(beverage3.cost())