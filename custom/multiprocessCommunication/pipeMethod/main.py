from multiprocessing import Process, Pipe
import proccess1
from controlBoard.controlBoard import ControlBoard
from controlBoard.controlBoardProxyListener.controlBoardProxyListener import ControlBoardProxyListener

if __name__ == '__main__':
    parentConnection, childConnection = Pipe()

    controlBoard = ControlBoard()
    controlBoardProxyListener = ControlBoardProxyListener(parentConnection, controlBoard)

    p = Process(target=proccess1.main, args=(childConnection,))
    p.start()

    while True:
        try:
            controlBoardProxyListener.listen()
        except SystemExit:
            p.join()

