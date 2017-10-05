class Light:
    def __init__(self):
        self.state = "off"

    def on(self):
        print "light on"
        self.state = "on"

    def off(self):
        print "light off"
        self.state = "off"


class GarageDoor:
    def __init__(self):
        self.door = "down"
        self.light = "off"

    def up(self):
        self.door = "up"
        print "garage door up"

    def down(self):
        self.door = "down"
        print "garage door down"

    def stop(self):
        self.door = "stop"
        print "garage door stop"

    def lightOn(self):
        self.light = "on"
        print "garage door light On"

    def lightOff(self):
        self.light = "off"
        print "garage door light Off"


class Stereo:
    def __init__(self):
        self.state = "off"
        self.volume = 0

    def on(self):
        print "stereo on"
        self.state = "on"

    def off(self):
        print "stereo off"
        self.state = "off"

    def setCd(self):
        print "stereo set cd"

    def setVolume(self, volume):
        print "stereo set volume " + str(volume)
        assert type(volume) is int
        self.volume = volume


class CellingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self.location = location
        self.speed = CellingFan.OFF

    def high(self):
        self.speed = CellingFan.HIGH
        print "Celling fan speed HIGH"

    def medium(self):
        self.speed = CellingFan.MEDIUM
        print "Celling fan speed MEDIUM"

    def low(self):
        self.speed = CellingFan.LOW
        print "Celling fan speed LOW"

    def off(self):
        self.speed = CellingFan.OFF
        print "Celling fan speed OFF"

    def getSpeed(self):
        return self.speed

