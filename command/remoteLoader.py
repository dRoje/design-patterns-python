from remoteControl import RemoteControl, RemoteControlWithUndo
from vendor import Light, Stereo, GarageDoor, CellingFan
import lightCommands
import garageDoorCommands
import stereoCommands
import cellingFanCommands


class RemoteLoader:
    def load(self):
        remoteControl = RemoteControlWithUndo()

        livingRoomLight = Light()
        kitchenLight = Light()
        garageDoor = GarageDoor()
        stereo = Stereo()
        cellingFan = CellingFan("Living room")

        livingRoomLightOn = lightCommands.LightOnCommand(livingRoomLight)
        livingRoomLightOff = lightCommands.LightOffCommand(livingRoomLight)
        kitchenLightOn = lightCommands.LightOnCommand(kitchenLight)
        kitchenLightOff = lightCommands.LightOffCommand(kitchenLight)
        garageDoorUp = garageDoorCommands.GarageDoorOpenCommand(garageDoor)
        garageDoorDown = garageDoorCommands.GarageDoorCloseCommand(garageDoor)
        stereoOn = stereoCommands.StereoOnCommand(stereo)
        stereoOff = stereoCommands.StereoOffCommand(stereo)
        cellingFanMedium = cellingFanCommands.CellingFanMediumCommand(cellingFan)
        cellingFanHigh = cellingFanCommands.CellingFanHighCommand(cellingFan)
        cellingFanOff = cellingFanCommands.CellingFanOffCommand(cellingFan)

        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff)
        remoteControl.setCommand(2, garageDoorUp, garageDoorDown)
        remoteControl.setCommand(3, stereoOn, stereoOff)
        remoteControl.setCommand(4, cellingFanHigh, cellingFanOff)
        remoteControl.setCommand(5, cellingFanMedium, cellingFanOff)

        remoteControl.onButtonWasPushed(5)
        remoteControl.offButtonWasPushed(5)
        print remoteControl
        remoteControl.undoButtonWasPushed()

        remoteControl.onButtonWasPushed(4)
        print remoteControl
        remoteControl.undoButtonWasPushed()




RemoteLoader().load()

