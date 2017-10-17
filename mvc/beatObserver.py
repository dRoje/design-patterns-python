from abc import ABCMeta, abstractmethod


class BeatObserver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def updateBeat(self):
        pass


