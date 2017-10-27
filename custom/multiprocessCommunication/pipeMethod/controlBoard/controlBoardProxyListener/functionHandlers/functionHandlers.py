from functionHandler import FunctionHandler
from pipeMethod.controlBoard.controlBoard import ControlBoard


class TurnOnLedHandler(FunctionHandler):
    def __init__(self, controlBoard):
        # type: (ControlBoard) -> None
        FunctionHandler.__init__(self, functionName="turnOnLed")
        self.controlBoard = controlBoard

    def handleFunction(self, args):
        self.controlBoard.led.turnOn()


class TurnOffLedHandler(FunctionHandler):
    def __init__(self, controlBoard):
        # type: (ControlBoard) -> None
        FunctionHandler.__init__(self, functionName="turnOnLed")
        self.controlBoard = controlBoard

    def handleFunction(self, args):
        self.controlBoard.led.turnOff()
