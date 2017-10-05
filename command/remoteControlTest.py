import unittest
from garageDoorCommands import GarageDoorOpenCommand
from lightCommands import LightOnCommand
from remoteControl import SimpleRemoteControl
from vendor import Light, GarageDoor


class RemoteControlTest(unittest.TestCase):
    def testLightOn(self):
        remote = SimpleRemoteControl()
        light = Light()
        lightOn = LightOnCommand(light)

        remote.setCommand(lightOn)
        remote.buttonWasPressed()

        self.assertEqual(light.state, "on")

    def testGarageDoor(self):
        remote = SimpleRemoteControl()
        garageDoor = GarageDoor()
        garageDoorOpen = GarageDoorOpenCommand(garageDoor)

        remote.setCommand(garageDoorOpen)
        remote.buttonWasPressed()

        self.assertEqual(garageDoor.door, "up")
        self.assertEqual(garageDoor.light, "on")


if __name__ == '__main__':
        unittest.main()