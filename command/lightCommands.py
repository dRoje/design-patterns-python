from command import Command
from vendor import Light


class LightOnCommand(Command):
    def __init__(self, light):
        assert isinstance(light, Light)
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        assert isinstance(light, Light)
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

