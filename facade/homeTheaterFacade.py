from components import *


class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        # type: (Amplifier, Tuner, DVD, CD, Projector,  Screen, Lights, Popper) -> None
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watchMovie(self, movie):
        # type: (str) -> None
        print ("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()

        self.lights.dim()

        self.screen.down()

        self.projector.on()
        self.projector.wideScreenMode()

        self.amp.on()
        self.amp.setDvd(self.dvd)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)

        self.dvd.on()
        self.dvd.play(movie)

    def endMovie(self):
        print "Shutting movie theater down..."
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

