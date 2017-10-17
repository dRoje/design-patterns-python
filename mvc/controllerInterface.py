from abc import ABCMeta, abstractmethod


class ControllerInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def setBPM(self, bpm):
        # type: (int) ->None
        pass

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def increaseBPM(self): pass

    @abstractmethod
    def decreaseBPM(self): pass


