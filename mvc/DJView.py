from tkinter import *
from designPatterns.mvc. beatModel import BeatModel, BeatModelInterface
from designPatterns.mvc.controllerInterface import ControllerInterface
from designPatterns.mvc.beatBar import BeatBar
from designPatterns.mvc.beatObserver import BeatObserver
from designPatterns.mvc.bpmObserver import BPMObserver


class DJView(BeatObserver, BPMObserver):
    def __init__(self, model, controller):
        # type: (BeatModelInterface, ControllerInterface) -> None
        self.root = Tk()
        self.top = Toplevel()
        self.model = model
        self.controller = controller
        self.beatBar = BeatBar()

        self.menubar = Menu(self.root)
        self.DJmenu = Menu(self.menubar, tearoff=0)

        self.model.registerObserver(self)
        self.model.registerObserverBPM(self)

    def updateBPM(self):
        bpm = self.model.getBPM()
        self.bpmVar.set(bpm)
        self.bpmLabelVar.set("Current BPM: " + str(bpm))

    def updateBeat(self):
        self.beatBar.setValue(100)

    def createView(self):
        self.createRootView()
        self.createTopLevelView()

    def enableStopMenuItem(self):
        self.DJmenu.entryconfig(1, state=NORMAL)

    def disableStopMenuItem(self):
        self.DJmenu.entryconfig(1, state=DISABLED)

    def enableStartMenuItem(self):
        self.DJmenu.entryconfig(1, state=NORMAL)

    def disableStartMenuItem(self):
        self.DJmenu.entryconfig(1, state=DISABLED)

    def setBPM(self):
        bpm = self.bpmEntry.get()
        self.controller.setBPM(int(bpm))

    def increaseBPM(self):
        self.controller.increaseBPM()

    def decreaseBPM(self):
        self.controller.decreaseBPM()

    def start(self):
        self.controller.start()
        self.DJmenu.entryconfig(0, state=DISABLED)   # disable start
        self.DJmenu.entryconfig(1, state=NORMAL)   # enable stop

    def stop(self):
        self.controller.stop()
        self.DJmenu.entryconfig(1, state=DISABLED)   # disable stop
        self.DJmenu.entryconfig(0, state=NORMAL)   # enable start

    def quit(self):
        self.controller.stop()
        self.root.quit()

    def runView(self):
        self.root.mainloop()

    def createTopLevelView(self):
        barFrame = Frame(self.top)
        currentBPMFrame = Frame(self.top)

        barFrame.pack()
        currentBPMFrame.pack()

        # bar
        self.bpmVar = IntVar()
        self.bpmVar.set(self.model.getBPM())
        scale = Scale(barFrame, variable=self.bpmVar, orient=HORIZONTAL, to=500, length=200)
        scale.pack(anchor=CENTER)

        # Current BPM
        self.bpmLabelVar = StringVar()
        self.bpmLabelVar.set("Current BPM: " + str(self.model.getBPM()))
        label = Label(currentBPMFrame, textvariable=self.bpmLabelVar, relief=FLAT)
        label.pack()

    def createRootView(self):
        topFrame = Frame(self.root)
        enterBpmFrame = Frame(self.root)
        setBpmFrame = Frame(self.root)
        bpmButtonsFrame = Frame(self.root)

        topFrame.pack()
        enterBpmFrame.pack()
        setBpmFrame.pack()
        bpmButtonsFrame.pack()

        # DJ Control
        self.DJmenu.add_command(label="Start", command=self.start)
        self.DJmenu.add_command(label="Stop", command=self.stop)
        self.DJmenu.add_command(label="Quit", command=self.quit)
        self.menubar.add_cascade(label="DJ Control", menu=self.DJmenu)
        self.root.config(menu=self.menubar)
        self.DJmenu.entryconfig(1, state=DISABLED)

        # Enter BPM
        bpmLabel = Label(enterBpmFrame, text="Enter BPM: ")
        bpmLabel.pack(side=LEFT)
        self.bpmEntry = Entry(enterBpmFrame, bd=5)
        self.bpmEntry.pack(side=RIGHT)

        # Set button
        setButton = Button(setBpmFrame, text="Set", command=self.setBPM)
        setButton.pack()

        # << >>
        leftButton = Button(bpmButtonsFrame, text="<<", command=self.decreaseBPM)
        leftButton.pack(side=LEFT)
        rightButton = Button(bpmButtonsFrame, text=">>", command=self.increaseBPM)
        rightButton.pack(side=RIGHT)