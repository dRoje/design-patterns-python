from quackable import Quackable


class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self, quacker):
        # type: (Quackable) -> None
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def registerObserver(self, observer):
        for quacker in self.quackers:
            quacker.registerObserver(observer)

    def notifyObservers(self):
        for quacker in self.quackers:
            quacker.notifyObservers()

