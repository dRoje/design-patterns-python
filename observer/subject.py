from observer import Observer
from observable import Observable


class Subject(Observable):
    def __init__(self):
        self.changed = False
        self.observers = []

    def registerObserver(self, observer):
        assert isinstance(observer, Observer)
        self.observers.append(observer)

    def removeObserver(self, observer):
        assert isinstance(observer, Observer)
        self.observers.remove(observer)

    def notifyObservers(self, *args):
        if self.changed:
            for observer in self.observers:
                assert isinstance(observer, Observer)
                observer.update(self, args)
            self.clearChanged()

    def setChanged(self):
        # for extra flexibility, not necessary
        self.changed = True

    def clearChanged(self):
        self.changed = False