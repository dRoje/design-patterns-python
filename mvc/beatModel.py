from designPatterns.mvc.beatModelInterface import BeatModelInterface
from designPatterns.mvc.sequencer import Sequencer
from designPatterns.mvc.beatObserver import BeatObserver
from designPatterns.mvc.bpmObserver import BPMObserver


class BeatModel(BeatModelInterface):
    def __init__(self):
        self.sequencer = Sequencer()
        self.beatObservers = []
        self.bpmObservers = []
        self.bpm = 90

    def initialize(self):
        self.setUpMidi()
        self.buildTrackAndStart()

    def on(self):
        self.sequencer.start()
        self.setBPM(90)

    def off(self):
        self.setBPM(0)
        self.sequencer.stop()

    def setBPM(self, bpm):
        # type: (int) -> None
        self.bpm = bpm
        self.sequencer.setTempoInBPM(self.getBPM())
        self.notifyBPMObservers()

    def getBPM(self):
        # type: () -> int
        return self.bpm

    def beatEvent(self):
        self.notifyBeatObservers()

    def registerObserver(self, beatObserver):
        self.beatObservers.append(beatObserver)

    def registerObserverBPM(self, bpmObserver):
        self.bpmObservers.append(bpmObserver)

    def notifyBeatObservers(self):
        for observer in self.beatObservers:
            assert isinstance(observer, BeatObserver)
            observer.updateBeat()

    def notifyBPMObservers(self):
        for observer in self.bpmObservers:
            assert isinstance(observer, BPMObserver)
            observer.updateBPM()

    def setUpMidi(self): pass

    def buildTrackAndStart(self): pass