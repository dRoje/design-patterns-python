from quackable import Quackable
from observable import Observable


class MallardDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print "Quack!"
        self.notifyObservers()

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __str__(self):
        return "Mallard Duck"


class RedheadDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print "Quack!"
        self.notifyObservers()

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __str__(self):
        return "Redhead Duck"


class DuckCall(Quackable):
    def quack(self):
        print "Kwak!"

    def __str__(self):
        return "Duck Call"


class RubberDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print "Squeak!"
        self.notifyObservers()

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __str__(self):
        return "Rubber Duck"
