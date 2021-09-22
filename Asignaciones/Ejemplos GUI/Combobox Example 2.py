from tkinter import *
from tkinter import ttk


def on_field_change(index, value, op):
    print ("combobox updated to ", c.get())
    print(index)
    print(value)
    print(op)
root = Tk()
v = StringVar()
v.trace('w',on_field_change)
c = ttk.Combobox(root, textvar=v, values=["foo", "bar", "baz"])
c.pack()

mainloop()
