from abc import ABCMeta, abstractmethod


class Observer:
    # interface
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, observable, *args): pass