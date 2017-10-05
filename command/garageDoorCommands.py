from command import Command


class GarageDoorOpenCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.up()
        self.garageDoor.lightOn()

    def undo(self):
        self.garageDoor.down()
        self.garageDoor.lightOff()


class GarageDoorCloseCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.down()
        self.garageDoor.lightOff()

    def undo(self):
        self.garageDoor.up()
        self.garageDoor.lightOn()
