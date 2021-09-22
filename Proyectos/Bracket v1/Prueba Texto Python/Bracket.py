from tkinter import *
from tkinter import messagebox

v =Tk()

v.geometry("500x500")


class Botones_Octavos(Button):
    pass

    def __init__( self,elegido,cambiante,cambiante2,parent,**kw ):
        
        Button.__init__(self,parent,kw)
        self.Elegido=elegido
        self.Cambiante=cambiante
        self.Cambiante2=cambiante2
    def getElegido(self):
        
        if self.Cambiante.get() == "1_clasificado" and self.Cambiante2.get() != self.Elegido.get():

            self.Cambiante.set( self.Elegido.get() )
            
        elif self.Cambiante2.get() == "2_clasificado" and self.Cambiante.get() != self.Elegido.get():
            self.Cambiante2.set( self.Elegido.get() )
            
        elif self.Cambiante.get() == self.Elegido.get() and self.Elegido.get() != self.Cambiante2.get():
            
            self.Cambiante.set("1_clasificado")
            
        elif self.Cambiante2.get() == self.Elegido.get() and self.Cambiante.get() != self.Elegido.get():
            
            self.Cambiante2.set("2_clasificado")
            
        else:
            
            messagebox.showinfo("Mundial Brazil 2014","Ya esta ocupado, deseleccione alguno para cambiar de valor")
        




v.configure(bg="#e8e9ee")

frameGrupoD = Frame( v )
frameGrupoD.configure(bg="#363636")
frameGrupoD.grid()
frameGrupoD.place(x=50,y=100)


lblGrupoD=Label(frameGrupoD,text="Grupo D")
lblGrupoD.grid(row=0,column=0,pady=5,padx=5,columnspan=2)

varD1=StringVar()
varD1.set("1_clasificado")
btnD1=Button( frameGrupoD,textvariable=varD1 ,font=("Calibri",12),bd=0,bg="#111111",foreground="white" )
btnD1.grid(row=1,column=1,pady=5,padx=5)

varD2=StringVar()
varD2.set("2_clasificado")
btnD2=Button( frameGrupoD,textvariable=varD2 ,font=("Calibri",12),bd=0,bg="#111111",foreground="white" )
btnD2.grid(row=2,column=1,pady=5,padx=5)



varURU=StringVar()
varURU.set( "Uruguay" )
btnURU=Botones_Octavos( varURU , varD1 , varD2 , frameGrupoD ,text=varURU.get() ,font=("Calibri",12),bd=0,bg="#009999",foreground="white" )
btnURU.configure( command=btnURU.getElegido )
btnURU.grid(row=1,column=0,pady=5,padx=5)


varCRC=StringVar()
varCRC.set( "Costa Rica" )
btnCRC=Botones_Octavos( varCRC , varD1 , varD2 , frameGrupoD ,text=varCRC.get() ,font=("Calibri",12),bd=0,bg="#009999",foreground="white" )
btnCRC.configure( command=btnCRC.getElegido )
btnCRC.grid(row=2,column=0,pady=5,padx=5)


varING=StringVar()
varING.set( "Inglaterra" )
btnING=Botones_Octavos( varING,varD1, varD2 , frameGrupoD ,text=varING.get() ,font=("Calibri",12),bd=0,bg="#009999",foreground="white" )
btnING.configure( command=btnING.getElegido )
btnING.grid(row=3,column=0,pady=5,padx=5)


varITA=StringVar()
varITA.set( "Italia" )
btnITA=Botones_Octavos( varITA,varD1, varD2 , frameGrupoD ,text=varITA.get() ,font=("Calibri",12),bd=0,bg="#009999",foreground="white" )
btnITA.configure( command=btnITA.getElegido )
btnITA.grid(row=4,column=0,pady=5,padx=5)




v.mainloop()
