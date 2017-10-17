from tkinter import *
from designPatterns.mvc.DJView import DJView
from designPatterns.mvc.beatModel import BeatModel
from designPatterns.mvc.beatController import BeatController

beatModel = BeatModel()
beatController = BeatController(beatModel)

beatController.view.runView()


