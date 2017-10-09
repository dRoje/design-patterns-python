class Amplifier:
    def __init__(self):
        pass

    def on(self):
        print "Amplifier on"

    def off(self):
        print "Amplifier off"

    def setDvd(self, dvd):
        print "Amplifier setDvd"

    def setSurroundSound(self):
        print "Amplifier setSurroundSound"

    def setVolume(self, vol):
        print "Amplifier setVolume " + str(vol)


class Tuner:
    def __init__(self):
        pass


class CD:
    def __init__(self):
        pass


class DVD:
    def __init__(self):
        pass

    def on(self):
        print "DVD on"

    def off(self):
        print "DVD off"

    def stop(self):
        print "DVD stop"

    def play(self, movie):
        # type: (str) -> None
        print "DVD play " + movie

    def eject(self):
        print "DVD eject"


class Projector:
    def __init__(self):
        pass

    def on(self):
        print "Projector on"

    def off(self):
        print "Projector off"

    def wideScreenMode(self):
        print "Projector wideScreenMode"


class Screen:
    def __init__(self):
        pass

    def up(self):
        print "Screen up"

    def down(self):
        print "Screen down"


class Lights:
    def __init__(self):
        pass

    def dim(self):
        print "Lights dim"

    def on(self):
        print "Lights on"


class Popper:
    def __init__(self):
        pass

    def on(self):
        print "Popper on"

    def off(self):
        print "Popper off"

    def pop(self):
        print "Popper pop"
