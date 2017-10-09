from abc import ABCMeta, abstractmethod


class Turkey:
    __metaclass__ = ABCMeta

    @abstractmethod
    def gobble(self): pass

    @abstractmethod
    def fly(self): pass


class WildTurkey(Turkey):

    def gobble(self):
        print "Gobble gobble"

    def fly(self):
        print "fly short distance"
