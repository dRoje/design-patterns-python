from abc import ABCMeta, abstractmethod


class QuackBehavior:
    __metaclass__ = ABCMeta
    @abstractmethod
    def quack(self): pass


class Quack(QuackBehavior):
    def quack(self):
        print "Quack"


class Squeak(QuackBehavior):
    def quack(self):
        print "Squeak"


class MuteQuack(QuackBehavior):
    def quack(self):
        print "no quack"