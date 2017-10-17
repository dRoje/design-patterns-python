from abc import ABCMeta, abstractmethod


class BPMObserver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateBPM(self):
        pass


