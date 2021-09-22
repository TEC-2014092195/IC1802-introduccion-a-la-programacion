import sys
from tkinter import *



class Constructor_Entry(Entry):

    def __init__(self,variable,parent,**kw):
        Entry.__init__(self,parent,kw)
        self.Variable=variable

    def getvar(self):
        print(self.Variable.get())
        write(self.Variable.get())

    def write(self):
        
        nombre=self.Variable.get()
        name = nombre+'.txt'  # Name of text file coerced with +.txt

        try:
            file = open(name, 'w')   # You can use open(name, 'w'); which create the file if the file does not exist, but it will truncate existing file.
            file.close()             # Alternatively can use open(name, 'a'); will create the file if the file does not exist, will not truncate the existing file.

        except:
            print('Something went wrong! Can\'t tell what?')
            sys.exit(0) # quit Python

    


v=Tk()

v.geometry("500x500")

varentrada=StringVar()
entrada=Constructor_Entry(varentrada,v,textvariable=varentrada)
entrada.pack()

def ejecutar():
    entrada.write()

btn=Button(v,text="Exce",command=ejecutar)
btn.pack()



v.mainloop()

