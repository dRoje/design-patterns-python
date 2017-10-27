class Led:
    def __init__(self):
        self.state = "off"

    def turnOn(self):
        print "Turn on led"
        self.state = "on"

    def turnOff(self):
        print "Turn off led"
        self.state = "off"

    def getState(self):
        return self.state

