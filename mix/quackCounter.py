from quackable import Quackable


class QuackCounter(Quackable):
    # decorator
    numberOfQuacks = 0

    def __init__(self, duck):
        # type: (Quackable) -> None
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.numberOfQuacks += 1

    @staticmethod
    def getQuacks():
        return QuackCounter.numberOfQuacks

    def notifyObservers(self):
        self.duck.notifyObservers()

    def registerObserver(self, observer):
        self.duck.registerObserver(observer)

    def __str__(self):
        return self.duck.__str__()