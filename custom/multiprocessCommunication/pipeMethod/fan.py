class Fan:
    def __init__(self):
        self.state = "off"

    def turnOn(self):
        print "Turn on fan"
        self.state = "on"

    def turnOff(self):
        print "Turn off fan"
        self.state = "off"

    def getState(self):
        return self.state