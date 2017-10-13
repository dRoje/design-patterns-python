from quackObservable import QuackObservable


class Observable(QuackObservable):
    def __init__(self, duck):
        # type: (QuackObservable) -> None
        self.duck = duck
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.duck)


