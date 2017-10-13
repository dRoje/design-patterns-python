from observer import Observer
from quackObservable import QuackObservable


class Quackologist(Observer):
    def update(self, duck):
        # type: (QuackObservable) -> None
        print "Quackologist: " + str(duck) + " just quacked"

