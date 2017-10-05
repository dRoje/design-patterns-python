from command import Command
from vendor import Stereo


class StereoOnCommand(Command):
    def __init__(self, stereo):
        assert isinstance(stereo, Stereo)
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCd()
        self.stereo.setVolume(11)

    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        assert isinstance(stereo, Stereo)
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.setCd()
        self.stereo.setVolume(11)


