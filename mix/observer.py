from abc import *


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, duck): pass


