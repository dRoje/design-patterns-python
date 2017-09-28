from abc import ABCMeta, abstractmethod
from flyBehavior import FlyBehavior, FlyNoWay, FlyWithWings
from quackBehavior import QuackBehavior, Quack, Squeak, MuteQuack

class Duck:
    __metaclass__ = ABCMeta

    def __init__(self, flyBehavior, quackBehavior):
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior

    @abstractmethod
    def display(self): pass

    def swim(self):
        print "swim"

    def performQuack(self):
        self.quackBehavior.quack()

    def performFly(self):
        self.flyBehavior.fly()

    def setFlyBehavior(self, flyBehavior):
        assert isinstance(flyBehavior, FlyBehavior)
        self.flyBehavior = flyBehavior

    def setQuackBehavior(self, quackBehavior):
        assert isinstance(quackBehavior, QuackBehavior)
        self.quackBehavior = quackBehavior


class MallardDuck(Duck):
    def __init__(self):
        flyBehavior = FlyWithWings()
        quackBehavior = Quack()
        Duck.__init__(self, flyBehavior, quackBehavior)

    def display(self):
        print "mallard duck"


class ModelDuck(Duck):
    def __init__(self):
        flyBehavior = FlyNoWay()
        quackBehavior = Quack()
        Duck.__init__(self, flyBehavior, quackBehavior)

    def display(self):
        print "model duck"