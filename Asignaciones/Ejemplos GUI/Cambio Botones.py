from tkinter import *

v=Tk()

v.geometry("500x500")

class clase_Boton(Button):
    bandera=False
    def __init__(self, valor, parent, **kw):
        Button.__init__(self,parent,kw)
        self.Valor=valor
        
    def Accion(self):
        if self.bandera==False:
            self.configure(bg="red")
            print(self.Valor)
            self.bandera=True
        else:
            self.configure(bg="green")
            print(self.Valor)
            self.bandera=False


b={}

for i in range(5):
    b[i]=clase_Boton("Boton"+str(i),v,text="boton"+str(i))
    b[i].configure(command=b[i].Accion)
    b[i].pack()

##btnPablo = clase_Boton("Boton1",v,text="boton1")
##btnPablo.configure(command=btnPablo.Accion)
##btnPablo.place(x=200,y=300)



v.mainloop()
