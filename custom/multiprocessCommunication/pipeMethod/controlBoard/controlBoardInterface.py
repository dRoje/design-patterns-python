from abc import ABCMeta, abstractmethod


class IControlBoard:
    __metaclass__ = ABCMeta

    @abstractmethod
    def turnOnLed(self): pass

    @abstractmethod
    def turnOffLed(self): pass

    @abstractmethod
    def turnOnFan(self): pass

    @abstractmethod
    def turnOffFan(self): pass

    @abstractmethod
    def getStates(self): pass





