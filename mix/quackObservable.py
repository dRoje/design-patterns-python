from abc import *


class QuackObservable:
    __metaclass__ = ABCMeta

    def registerObserver(self, observer): pass

    def notifyObservers(self): pass

