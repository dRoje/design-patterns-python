from command import Command
from typing import List


class MacroCommand(Command):
    def __init__(self, commands):
        # type: (List(Command)) -> None
        assert isinstance(commands, list)
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()

