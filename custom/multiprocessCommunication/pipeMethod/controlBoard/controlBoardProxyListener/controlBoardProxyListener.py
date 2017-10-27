from controlBoardProxyMessageReceiver import ControlBoardProxyMessageReceiver
from controlBoardProxyHandler import ControlBoardProxyHandler
from pipeMethod.controlBoard.controlBoard import ControlBoard
from functionHandlers.functionHandlers import *
import multiprocessing


class ControlBoardProxyListener:
    def __init__(self, pipeConnection, controlBoard):
        # type: (multiprocessing.Connection, ControlBoard) -> None
        self.controlBoardProxyMessageReceiver = ControlBoardProxyMessageReceiver(pipeConnection)
        self.controlBoardProxyHandler = ControlBoardProxyHandler(
            [
                TurnOffLedHandler(controlBoard),
                TurnOnLedHandler(controlBoard)
            ]
        )

    def listen(self):
        message = self.controlBoardProxyMessageReceiver.receive()
        self.controlBoardProxyHandler.handleReceivedMessage(message)

