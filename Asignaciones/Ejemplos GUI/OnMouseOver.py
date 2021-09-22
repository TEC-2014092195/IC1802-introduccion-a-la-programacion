import tkinter as tk

class Labels(object):
    def __init__(self,number,basicStr,onMouseStr):
        self.i = number
        self.basicStr = basicStr + str(number)
        self.onMouseStr = onMouseStr
        mylist=['a','b','c','d','e']
        self.label = tk.Label(root,text="Label"+str(i))
        self.label.grid(row=1+i,column=1)
        self.label.bind("<Enter>", self.fun1)
        self.label.bind("<Leave>", self.fun2)
    def fun1(self,event):
        self.label.config(text=self.basicStr)
    def fun2(self,event):
        self.label.config(text=self.onMouseStr)
root=tk.Tk()
labelsList = []
for i in range(5):
    lab = Labels(i,"haha","Label"+str(i))
    labelsList.append(lab)

root.mainloop()


