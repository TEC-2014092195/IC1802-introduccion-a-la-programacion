from tkinter import *
from tkinter import messagebox
import pickle
import os

class crearStickers():
    
    def __init__(self):
        self.nom = []
        self.paginas=0
        self.fila=0
        self.columna=0
        self.frmdic={}
        self.btn={}
        self.pagina_actual=0
        self.listapostales=[]
        
    def primeraVista(self):
        
        self.frmdic["frm"+str(0)].grid()

    def cambiarNombre(self,event):
        vtemp=Toplevel()
        frmtemp=Frame(vtemp)
        frmtemp.grid()

        lbltemp = Label(frmtemp,text="Ingrese nuevo nombre: ")
        lbltemp.grid(row=0,column=0)

        vartemp=StringVar()
        enttemp=Entry(frmtemp,textvariable=vartemp)
        enttemp.grid(row=0,column=1)
        def cerrar(ventana):
            ventana.destroy()
            event.widget.configure( text=vartemp.get() )
        btntemp=Button(frmtemp,text="CONFIRMAR")
        btntemp.grid(row=0,column=2)
        btntemp.configure(command=lambda: cerrar(vtemp))
        
    def crearBotones(self,frm):
        self.frmdic = {}
        for i in range(self.paginas):
            self.frmdic["frm"+str(i)] = Frame(frm)
            self.frmdic["frm"+str(i)].configure(bg="white")
            self.frmdic["frm"+str(i)].grid(row=0,column=1,padx=5)

        pagina=0
        self.fila=0
        self.columna=0
        while pagina < self.paginas:
            fi=self.fila
            co=self.columna
            
            i,j=0,0
            for h in range(fi,fi+10):
                j=0
                for k in range(co,co+5):
                    try:
                        self.btn["btn"+'%d.%d' %(h,k)] = Button(self.frmdic["frm"+str(pagina)],text=self.nom.pop(0))
                        self.btn["btn"+'%d.%d' %(h,k)].configure(width=10,relief="ridge")
                        self.btn["btn"+'%d.%d' %(h,k)].bind("<Button-1>", lambda event: self.cambiarNombre(event) )
                        self.btn["btn"+'%d.%d' %(h,k)].grid(row=i,column=j+1,pady=2,padx=2,ipadx=10,ipady=10)
                        self.frmdic["frm"+str(pagina)].grid_remove()
                    except:
                        True
                    j+=1
                i+=1
            print(pagina)
            pagina+=1
            self.fila+=10
            self.columna+=5
        
        self.primeraVista()

    def botonAnterior(self):
            
            try:
                
                if self.pagina_actual == 0:
                    True
                else:
                    self.pagina_actual-=1
                    actual=self.pagina_actual
                    anterior=self.pagina_actual+1
                    self.frmdic["frm"+str(anterior)].grid_remove()
                    self.frmdic["frm"+str(actual)].grid()
                    
            except:
                True

    def botonSiguiente(self):
            
            try:
                if self.pagina_actual == self.paginas-1:
                    True
                else:
                    self.pagina_actual+=1
                    actual=self.pagina_actual
                    anterior=self.pagina_actual-1
                    print("actual",actual)
                    print("ant",anterior)
                    self.frmdic["frm"+str(anterior)].grid_remove()
                    self.frmdic["frm"+str(actual)].grid()
            except:
                True

##    def __getstate__(self):
##            state = self.__dict__.copy()
##            del state['log']
##            del state['cfg']
##            del state['view']
##            return state

    def getStickers(self):
##        self.listapostales
        paginas=self.paginas
        pagina=0
        fila=0
        columna=0
        while pagina < paginas:
            fi=fila
            co=columna
            
            i,j=0,0
            for h in range(fi,fi+10):
                j=0
                for k in range(co,co+5):
                    try:
                        
                        self.listapostales.append( self.btn["btn"+'%d.%d' %(h,k)].cget("text") )
                        
                    except:
                        True
                    j+=1
                i+=1
##            print(pagina)
            pagina+=1
            fila+=10
            columna+=5
##        print(self.listapostales)
        
    def guardarDatos(self,canequipos,canbilletes):
            
        print(canequipos," billetes",canbilletes)
        
        self.getStickers()
        
        file = open("Template.txt","wb")

        pickle.dump(canequipos,file)
        pickle.dump(canbilletes,file)
        pickle.dump(self.listapostales,file)
        
        
        file.close()

        users=[]
        f = open("Usuarios/Usuarios.txt","wb")
        pickle.dump(users,f)
        f.close()
        messagebox.showinfo("Album","Se ha guardado correctamente")

        
            
    
    def crearFrame(self,canequipos,frm,canbilletes):
        
        self.nom=[]
        for i in range(canequipos):
            self.nom.append("postal #"+str(i))

        paginas=canequipos/50
        paginas=int(paginas)


        ultimacolumna=canequipos%5
        print("ultima columna",ultimacolumna)

        ultimafila= (canequipos - (paginas*50)) / 5
        ultimafila=int(ultimafila)
        if ultimacolumna !=0:
            ultimafila+=1
        print("ultima fila",ultimafila)
        if ultimacolumna != 0 or ultimafila !=0:
            paginas+=1 
        print("paginas",paginas)
        self.paginas=paginas

        self.crearBotones(frm)

        
                

        btnAnt=Button(frm,text=" «« ")
        btnAnt.grid(row=0,rowspan=5,column=0,padx=5)
        btnAnt.configure(command=self.botonAnterior)

        
            

        btnSig=Button(frm,text=" »» ")
        btnSig.grid(row=0,rowspan=5,column=frm.grid_size()[0],padx=5)
        btnSig.configure(command=self.botonSiguiente)

        
        btnGuardar = Button(frm,text="GUARDAR")
        btnGuardar.grid(row=frm.grid_size()[1],column=1,padx=5)
        btnGuardar.configure(command=lambda: self.guardarDatos(canequipos,canbilletes))



















        
