from command import Command
from vendor import CellingFan


class CellingFanHighCommand(Command):
    def __init__(self, cellingFan):
        assert isinstance(cellingFan, CellingFan)
        self.cellingFan = cellingFan
        self.previousSpeed = CellingFan.OFF

    def execute(self):
        self.previousSpeed = self.cellingFan.getSpeed()
        self.cellingFan.high()

    def undo(self):
        if self.previousSpeed == CellingFan.HIGH:
            self.cellingFan.high()
        if self.previousSpeed == CellingFan.MEDIUM:
            self.cellingFan.medium()
        if self.previousSpeed == CellingFan.LOW:
            self.cellingFan.low()
        if self.previousSpeed == CellingFan.OFF:
            self.cellingFan.off()


class CellingFanMediumCommand(Command):
    def __init__(self, cellingFan):
        assert isinstance(cellingFan, CellingFan)
        self.cellingFan = cellingFan
        self.previousSpeed = CellingFan.OFF

    def execute(self):
        self.previousSpeed = self.cellingFan.getSpeed()
        self.cellingFan.medium()

    def undo(self):
        if self.previousSpeed == CellingFan.HIGH:
            self.cellingFan.high()
        if self.previousSpeed == CellingFan.MEDIUM:
            self.cellingFan.medium()
        if self.previousSpeed == CellingFan.LOW:
            self.cellingFan.low()
        if self.previousSpeed == CellingFan.OFF:
            self.cellingFan.off()


class CellingFanOffCommand(Command):
    def __init__(self, cellingFan):
        assert isinstance(cellingFan, CellingFan)
        self.cellingFan = cellingFan
        self.previousSpeed = CellingFan.OFF

    def execute(self):
        self.previousSpeed = self.cellingFan.getSpeed()
        self.cellingFan.off()

    def undo(self):
        if self.previousSpeed == CellingFan.HIGH:
            self.cellingFan.high()
        if self.previousSpeed == CellingFan.MEDIUM:
            self.cellingFan.medium()
        if self.previousSpeed == CellingFan.LOW:
            self.cellingFan.low()
        if self.previousSpeed == CellingFan.OFF:
            self.cellingFan.off()
