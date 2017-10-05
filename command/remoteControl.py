from command import Command, NoCommand


class SimpleRemoteControl:
    def __init__(self):
        self.slot = Command

    def setCommand(self, command):
        # type: (Command) -> None
        assert isinstance(command, Command)
        self.slot = command

    def buttonWasPressed(self):
        self.slot.execute()


class RemoteControl:
    def __init__(self):
        self.onCommands = [NoCommand()]*7
        self.offCommands = [NoCommand()]*7

    def setCommand(self, slot, onCommand, offCommand):
        assert isinstance(onCommand, Command)
        assert isinstance(offCommand, Command)
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()

    def __str__(self):
        stringBuffer = "\n------- Remote Control -------\n"
        index = 0
        for command in self.onCommands:
            stringBuffer += "[slot " + str(index) + "]" + command.__class__.__name__ + ",\t " + \
                            self.offCommands[index].__class__.__name__ + "\n"
            index += 1

        return stringBuffer


class RemoteControlWithUndo:
    def __init__(self):
        self.onCommands = [NoCommand()]*7
        self.offCommands = [NoCommand()]*7
        self.undoCommand = NoCommand()

    def setCommand(self, slot, onCommand, offCommand):
        # type: (int, Command, Command) -> None
        assert isinstance(onCommand, Command)
        assert isinstance(offCommand, Command)
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPushed(self):
        self.undoCommand.undo()

    def __str__(self):
        stringBuffer = "\n------- Remote Control -------\n"
        index = 0
        for command in self.onCommands:
            stringBuffer += "[slot " + str(index) + "]" + command.__class__.__name__ + ",\t " + \
                            self.offCommands[index].__class__.__name__ + "\n"
            index += 1
        stringBuffer += "[undo]" + self.undoCommand.__class__.__name__ + "\n"


        return stringBuffer