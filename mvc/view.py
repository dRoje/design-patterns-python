from tkinter import *

# root = Tk()
# frame = Frame(root)
# frame.pack()
# root.mainloop()

class DJView:
    def __init__(self, root):
        self.root = root

    def createView(self):
        frame = Frame(self.root)
        frame.pack()

        bottomframe = Frame(self.root)
        bottomframe.pack(side=BOTTOM)

        redbutton = Button(frame, text="Red", command=self.callback)
        redbutton.pack(side=LEFT)

        greenbutton = Button(frame, text="Brown", fg="brown")
        greenbutton.pack(side=LEFT)

        bluebutton = Button(frame, text="Blue", fg="blue")
        bluebutton.pack(side=LEFT)

        blackbutton = Button(bottomframe, text="Black", fg="black")
        blackbutton.pack(side=BOTTOM)

    def callback(self):
        print ("click!")
