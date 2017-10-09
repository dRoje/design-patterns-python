from abc import ABCMeta, abstractmethod


class CaffeineBeverage:
    __metaclass__ = ABCMeta

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    @abstractmethod
    def brew(self): pass

    @abstractmethod
    def addCondiments(self): pass

    def pourInCup(self):
        print "Pouring into cup"

    def boilWater(self):
        print "Boiling water"

    def customerWantsCondiments(self):
        # hook method
        return True
