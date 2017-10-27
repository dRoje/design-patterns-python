import multiprocessing
import random
import time
from pipeMethod.controlBoard.controlBoardProxy import ControlBoardProxy


def main(pipeConnection):
    # type: (multiprocessing.Connection) -> None
    controlBoard = ControlBoardProxy(pipeConnection)

    while True:
        command = random.randrange(0, 5)
        if command == 1:
            controlBoard.turnOnLed()
        elif command == 2:
            controlBoard.turnOffLed()
        elif command == 3:
            controlBoard.turnOnFan()
        elif command == 4:
            controlBoard.turnOffFan()
        elif command == 5:
            print controlBoard.getStates()
        time.sleep(1)

        # todo: test getting states ( send command and return response)
