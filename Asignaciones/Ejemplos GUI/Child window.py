##import tkinter as tk
##
##class MainWindow(tk.Frame):
##    counter = 0
##    def __init__(self, *args, **kwargs):
##        tk.Frame.__init__(self, *args, **kwargs)
##        self.button = tk.Button(self, text="Create new window", 
##                                command=self.create_window)
##        self.button.pack(side="top")
##
##    def create_window(self):
##        self.counter += 1
##        t = tk.Toplevel(self)
##        t.wm_title("Window #%s" % self.counter)
##        l = tk.Label(t, text="This is window #%s" % self.counter)
##        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
##
##if __name__ == "__main__":
##    root = tk.Tk()
##    main = MainWindow(root)
##    main.pack(side="top", fill="both", expand=True)
##    root.mainloop()
# display message in a child window
from tkinter import *
def messageWindow():
    # create child window
    win = Toplevel()
    # display message
    message = "This is the child window"
    Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()
    
# create root window
root = Tk()

# put a button on it, or a menu
Button(root, text='Bring up Message', command=messageWindow).pack()
# start event-loop
root.mainloop()
    
