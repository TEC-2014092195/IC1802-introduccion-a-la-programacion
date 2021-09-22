from tkinter import *

def buildInput(master):
     fileInputFrame = Frame(master)
     fileInputFrame.grid(row=0)
     Label(fileInputFrame, text="Input file:").grid(row=0, sticky=W)
     Entry(fileInputFrame).grid(row=0, column=1)

     Label(fileInputFrame, text="Output file:").grid(row=1, sticky=W)
     Entry(fileInputFrame).grid(row=1, column=1)


def buildButtons(master):
     buttonFrame = Frame(master)
     buttonFrame.grid(row=1)
     Button(buttonFrame, text='Testing Testing').grid(row=0)
     Label(buttonFrame, text='Some text').grid(row=0, column=1)
     Button(buttonFrame, text='Cancel').grid(row=1, column=1)


root = Tk()
buildInput(root)
buildButtons(root)
root.mainloop()
