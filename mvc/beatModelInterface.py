from abc import abstractmethod, ABCMeta
from designPatterns.mvc.beatObserver import BeatObserver
from designPatterns.mvc.bpmObserver import BPMObserver


class BeatModelInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def initialize(self): pass

    @abstractmethod
    def on(self): pass

    @abstractmethod
    def off(self): pass

    @abstractmethod
    def setBPM(self, bpm):
        # type: (int) -> None
        pass

    @abstractmethod
    def getBPM(self):
        # type: () -> int
        pass

    @abstractmethod
    def registerObserver(self, beatObserver):
        # type: (BeatObserver) -> None
        pass

    @abstractmethod
    def removeObserver(self, beatObserver):
        # type: (BeatObserver) -> None
        pass

    @abstractmethod
    def registerObserverBPM(self, bpmObserver):
        # type: (BPMObserver) -> None
        pass

    @abstractmethod
    def removeObserverBPM(self, bpmObserver):
        # type: (BPMObserver) -> None
        pass


