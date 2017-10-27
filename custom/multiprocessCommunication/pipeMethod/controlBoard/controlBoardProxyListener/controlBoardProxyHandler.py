from functionHandlers.functionHandler import FunctionHandler
from controlBoardProxyMessage import Message
from typing import List


class ControlBoardProxyHandler:
    def __init__(self, functionHandlers):
        # type: (List(FunctionHandler)) -> None
        self.functionHandlers = functionHandlers

    def handleReceivedMessage(self, message):
        # type: (Message) -> None
        assert isinstance(message, Message)
        for functionHandler in self.functionHandlers:
            assert isinstance(functionHandler, FunctionHandler)
            if functionHandler.getFunctionName() == message.getFunction():
                functionHandler.handleFunction(message.getArgs())

