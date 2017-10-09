from abc import ABCMeta, abstractmethod


class Duck:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self): pass

    @abstractmethod
    def fly(self): pass


class MallardDuck(Duck):
    def quack(self):
        print "Quack"

    def fly(self):
        print "I'm flying"



