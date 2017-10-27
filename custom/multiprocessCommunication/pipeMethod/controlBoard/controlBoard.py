from pipeMethod.led import Led
from pipeMethod.fan import Fan
from controlBoardInterface import IControlBoard


class ControlBoard(IControlBoard):
    def __init__(self):
        self.led = Led()
        self.fan = Fan()

    def turnOnLed(self):
        self.led.turnOn()

    def turnOffLed(self):
        self.led.turnOff()

    def turnOnFan(self):
        self.fan.turnOn()

    def turnOffFan(self):
        self.fan.turnOff()

    def getStates(self):
        states = {}
        states.update({'fan': self.fan.state})
        states.update({'led': self.led.state})

        return states

