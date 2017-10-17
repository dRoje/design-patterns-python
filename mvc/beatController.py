from designPatterns.mvc.controllerInterface import ControllerInterface
from designPatterns.mvc.DJView import DJView
from designPatterns.mvc.beatModelInterface import BeatModelInterface


class BeatController(ControllerInterface):
    def __init__(self, model):
        # type: (BeatModelInterface) -> None
        self.model = model
        self.view = DJView(self.model, self)
        self.view.createView()
        self.view.disableStopMenuItem()
        self.view.enableStartMenuItem()
        self.model.initialize()

    def start(self):
        self.model.on()
        self.view.disableStartMenuItem()
        self.view.enableStopMenuItem()

    def stop(self):
        self.model.off()
        self.view.disableStopMenuItem()
        self.view.enableStartMenuItem()

    def setBPM(self, bpm):
        # type: (int) ->None
        print("Setting BPM to " + str(bpm))
        self.model.setBPM(bpm)

    def increaseBPM(self):
        print("Increase BPM")
        bpm = self.model.getBPM()
        self.model.setBPM(bpm + 1)

    def decreaseBPM(self):
        print("Decrease BPM")
        bpm = self.model.getBPM()
        self.model.setBPM(bpm - 1)


