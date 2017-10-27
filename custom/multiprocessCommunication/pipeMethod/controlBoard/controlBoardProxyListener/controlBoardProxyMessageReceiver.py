import multiprocessing
from pipeMethod.controlBoard.controlBoardProxyListener.controlBoardProxyMessage import Message


class ControlBoardProxyMessageReceiver:
    def __init__(self, pipeConnection):
        # type: (multiprocessing.Connection) -> None
        self.conn = pipeConnection

    def receive(self):
        # type: () -> Message
        message = self.conn.recv()
        assert isinstance(message, Message)
        return message




