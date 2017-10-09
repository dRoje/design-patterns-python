from duck import MallardDuck, Duck
from turkey import WildTurkey
from turkeyAdapter import TurkeyAdapter


class DuckTestDrive:
    def test(self):
        self.duck = MallardDuck()
        self.turkey = WildTurkey()
        self.turkeyAdapter = TurkeyAdapter(self.turkey)

        print "The turkey says..."
        self.turkey.gobble()
        self.turkey.fly()

        print "The duck says..."
        self.testDuck(self.duck)

        print "The turkey adapter says..."
        self.testDuck(self.turkeyAdapter)

    def testDuck(self, duck):
        # type: (Duck) -> None
        duck.quack()
        duck.fly()


if __name__ == '__main__':
    DuckTestDrive().test()

