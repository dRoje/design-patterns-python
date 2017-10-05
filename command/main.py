import vendor
import lightCommands
import stereoCommands
import garageDoorCommands
import cellingFanCommands
from macroCommand import MacroCommand
from remoteControl import RemoteControlWithUndo

light = vendor.Light()
cellingFan = vendor.CellingFan("Living room")
stereo = vendor.Stereo()
garageDoor = vendor.GarageDoor()

lightOn = lightCommands.LightOnCommand(light)
lightOff = lightCommands.LightOffCommand(light)
garageDoorUp = garageDoorCommands.GarageDoorOpenCommand(garageDoor)
garageDoorDown = garageDoorCommands.GarageDoorCloseCommand(garageDoor)
stereoOn = stereoCommands.StereoOnCommand(stereo)
stereoOff = stereoCommands.StereoOffCommand(stereo)
cellingFanMedium = cellingFanCommands.CellingFanMediumCommand(cellingFan)
cellingFanHigh = cellingFanCommands.CellingFanHighCommand(cellingFan)
cellingFanOff = cellingFanCommands.CellingFanOffCommand(cellingFan)

partyOn = [lightOn, stereoOn, garageDoorUp, cellingFanHigh]
partyOff = [lightOff, stereoOff, garageDoorDown, cellingFanOff]

partyOnMacro = MacroCommand(partyOn)
partyOffMacro = MacroCommand(partyOff)

remoteControl = RemoteControlWithUndo()
remoteControl.setCommand(0, partyOnMacro, partyOffMacro)

print remoteControl
remoteControl.onButtonWasPushed(0)
remoteControl.offButtonWasPushed(0)
