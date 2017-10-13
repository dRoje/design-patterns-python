from abstractDuckFactory import AbstractDuckFactory
from quackCounter import QuackCounter
from ducks import *


class CountingDuckFactory(AbstractDuckFactory):
    def createDuckCall(self):
        return QuackCounter(DuckCall())

    def createMallardDuck(self):
        return QuackCounter(MallardDuck())

    def createRedheadDuck(self):
        return QuackCounter(RedheadDuck())

    def createRubberDuck(self):
        return QuackCounter(RubberDuck())


