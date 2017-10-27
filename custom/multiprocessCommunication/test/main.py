import time
from communication import ResponseCommunicator


if __name__ == '__main__':
    localServerAddress = ('localhost', 6000)
    localServerAuthkey = 'localServer'
    localServerListener = ResponseCommunicator(localServerAddress, localServerAuthkey)

    while True:
        localServerListener.listen()
        time.sleep(1)



