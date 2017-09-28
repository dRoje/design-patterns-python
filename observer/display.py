from abc import ABCMeta, abstractmethod


class DisplayElement:
    # interface
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self): pass
