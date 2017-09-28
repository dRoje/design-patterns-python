from abc import ABCMeta, abstractmethod


class FlyBehavior:
    __metaclass__ = ABCMeta
    @abstractmethod
    def fly(self): pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print "Flying with wings"


class FlyNoWay(FlyBehavior):
    def fly(self):
        print "No flying"


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print "Flying like a rocket"