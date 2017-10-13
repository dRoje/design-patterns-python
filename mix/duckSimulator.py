from ducks import *
from goose import *
from gooseAdapter import GooseAdapter
from quackCounter import QuackCounter
from countingDuckFactory import CountingDuckFactory
from abstractDuckFactory import AbstractDuckFactory
from flock import Flock
from quackologist import Quackologist


class DuckSimulator:
    def main(self):
        simulator = DuckSimulator()
        duckFactory = CountingDuckFactory()
        simulator.simulate(duckFactory)

    def simulate(self, duckFactory):
        # type: (AbstractDuckFactory) -> None
        mallardDuck = duckFactory.createMallardDuck()
        redheadDuck = duckFactory.createRedheadDuck()
        duckCall = duckFactory.createDuckCall()
        rubberDuck = duckFactory.createRubberDuck()
        gooseDuck = GooseAdapter(Goose())

        flockOfDucks = Flock()

        flockOfDucks.add(mallardDuck)
        flockOfDucks.add(redheadDuck)
        flockOfDucks.add(rubberDuck)
        flockOfDucks.add(gooseDuck)

        flockOfMallards = Flock()

        mallardDuck1 = duckFactory.createMallardDuck()
        mallardDuck2 = duckFactory.createMallardDuck()
        mallardDuck3 = duckFactory.createMallardDuck()
        mallardDuck4 = duckFactory.createMallardDuck()

        flockOfMallards.add(mallardDuck1)
        flockOfMallards.add(mallardDuck2)
        flockOfMallards.add(mallardDuck3)
        flockOfMallards.add(mallardDuck4)

        flockOfDucks.add(flockOfMallards)

        # print "\nDuck simulator: Whole Flock Simulation"
        # self.__simulate(flockOfDucks)
        #
        # print "\nDuck simulator: Mallard Flock Simulation"
        # self.__simulate(flockOfMallards)

        print "\nDuck simulator: With Observer"
        quackologist = Quackologist()
        flockOfDucks.registerObserver(quackologist)

        self.__simulate(flockOfDucks)

        print "Number of quacks: " + str(QuackCounter.getQuacks())

    def __simulate(self, duck):
        # type: (Quackable) -> None
        duck.quack()


if __name__ == '__main__':
    DuckSimulator().main()