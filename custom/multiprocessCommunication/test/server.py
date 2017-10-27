from communication import RequestCommunicator
import time
from threading import Timer

address = ('localhost', 6000)
authkey = 'localServer'
communicator = RequestCommunicator(address, authkey)


def sendAfterTimeout(communicator):
    communicator.sendCommand("after timeout")


print "------start----"
timer1 = Timer(5, sendAfterTimeout, [communicator])
timer1.start()

while True:
    reply = communicator.sendCommand("server")
    print reply
    time.sleep(1)
