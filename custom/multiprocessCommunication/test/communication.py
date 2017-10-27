from multiprocessing.connection import Listener, Client


class RequestCommunicator:
    def __init__(self, address, authkey):
        self.conn = Client(address, authkey=authkey)

    def sendCommand(self, command):
        self.conn.send(command)
        reply = None
        try:
            reply = self.conn.recv()
        except (IOError, EOFError) as e:
            print(e)
        return reply

    def __del__(self):
        self.conn.close()


class ResponseCommunicator:
    def __init__(self, address, authkey):
        self.listener = Listener(address, authkey=authkey)
        self.conn = self.listener.accept()

    def __del__(self):
        self.conn.close()
        self.listener.close()

    def listen(self):
        if self.conn.poll(0.2) is True:     # delay of 0.2s for server to respond...
            self.readCommand()
        else:
            pass

    def readCommand(self):
        try:
            command = self.conn.recv()
            print "received: " + command
            self.reply("main")
        except EOFError:
            self.conn.close()

    def reply(self, reply):
        self.conn.send(reply)