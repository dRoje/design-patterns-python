from components import *
from homeTheaterFacade import HomeTheaterFacade


class HomeTheaterTestDrive:
    def main(self):
        amp = Amplifier()
        tuner = Tuner()
        dvd = DVD()
        cd = CD()
        projector = Projector()
        screen = Screen()
        lights = Lights()
        popper = Popper()

        homeTheater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

        homeTheater.watchMovie("Raiders of the Lost Ark")
        homeTheater.endMovie()


HomeTheaterTestDrive().main()