from abstractDuckFactory import AbstractDuckFactory
from ducks import *


class DuckFactory(AbstractDuckFactory):
    def createDuckCall(self):
        return DuckCall()

    def createMallardDuck(self):
        return MallardDuck()

    def createRedheadDuck(self):
        return RedheadDuck()

    def createRubberDuck(self):
        return RubberDuck()


