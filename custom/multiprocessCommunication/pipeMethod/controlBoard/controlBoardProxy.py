import multiprocessing
from pipeMethod.controlBoard.controlBoardInterface import IControlBoard
from pipeMethod.controlBoard.controlBoardProxyListener.controlBoardProxyMessage import Message


class ControlBoardProxy(IControlBoard):
    def __init__(self, pipeConnection):
        # type: (multiprocessing.Connection) -> None
        self.conn = pipeConnection

    def turnOnLed(self):
        self.conn.send(Message("turnOnLed"))

    def turnOffLed(self):
        self.conn.send(Message("turnOffLed"))

    def turnOnFan(self):
        self.conn.send(Message("turnOnFan"))

    def turnOffFan(self):
        self.conn.send(Message("turnOffFan"))

    def getStates(self):
        self.conn.send(Message("getStates"))
        states = self.conn.recv()
        return states

    # todo: sending and receiving messages (e.g. getStates)