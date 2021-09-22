from tkinter import *
from tkinter import messagebox
import socket
import pickle

class clase_U_Inicio():
    def __init__(self,sock):
        self.nom = []
        self.paginas=0
        self.fila=0
        self.columna=0
        self.frmdic={}
        self.btn={}
        self.pagina_actual=0
        self.listapostales=[]

        self.btnPack={}
        self.userAlbum=[]
        self.paraVenta=[]
        self.enVenta=0
        
        
        self.canBilletes=0
        self.Postales=0
        self.primerPaquete=0
        self.sock=sock
        self.usuario=0
        self.listaVentas=0
        
    def varDefault(self,usuario,varBilletes):
        pedir="newuser"
        pedir=pickle.dumps(pedir)
        self.sock.send(pedir)

        pedir=usuario
        
        pedir=pickle.dumps(pedir)
        
        self.sock.send(pedir)
        self.usuario=usuario
        billetes = self.sock.recv(1024)
        print("bien")
        billetes = pickle.loads(billetes)
        print("b",billetes)
        varBilletes.set(billetes)
        self.canBilletes=billetes

        pedir =""
        pedir=pickle.dumps(pedir)
        self.sock.send(pedir)
        
        postales = self.sock.recv(8192)
        postales = pickle.loads(postales)
        self.Postales=postales

        pedir =""
        pedir=pickle.dumps(pedir)
        self.sock.send(pedir)
        
        paquete = self.sock.recv(8192)
        paquete = pickle.loads(paquete)
        self.primerPaquete=paquete
        
        file = open("EnVenta.txt","rb")
        self.enVenta = pickle.load(file)
        file.close()

    def primeraVista(self):
        
        self.frmdic["frm"+str(0)].grid()

    


    def pegarSticker(self,event,frmVenta):

        nomboton = event.widget.cget("text")

        if nomboton in self.userAlbum:
            
            if event.widget.cget("bg") != "#e4af4a":
                print("La postal ya esta en el album")
                

                vtemp=Toplevel()
                frmtemp=Frame(vtemp)
                frmtemp.grid()

                lbltemp = Label(frmtemp,text="Ingrese el precio de la carta: ")
                lbltemp.grid(row=0,column=0)

                vartemp=StringVar()
                enttemp=Entry(frmtemp,textvariable=vartemp)
                enttemp.grid(row=0,column=1)
                def cerrar(ventana):
                    try:
                        carta=event.widget.cget("text")
                        precio=vartemp.get()
                        precio=int(vartemp.get())
                        usuario = self.usuario
                    
                        vender=(usuario,carta,precio)
                        f=open("EnVenta.txt","rb")
                        original=pickle.load(f)
                        f.close()
                        
                        original.append(vender)
                        
                        f=open("EnVenta.txt","wb")
                        pickle.dump(original,f)
                        f.close()
                        
                        self.paraVenta.append(vender)
                        print(self.paraVenta)
                        
                        
                        event.widget.configure(bg="#e4af4a",relief=FLAT)
                        ventana.destroy()
                    except:
                        print("Cantidad incorrrecta")
                    
                btntemp=Button(frmtemp,text="CONFIRMAR")
                btntemp.grid(row=0,column=2)
                btntemp.configure(command=lambda: cerrar(vtemp))
            

        elif nomboton in self.Postales:
           indice = self.Postales.index( nomboton )
           
           print(indice)
           self.btn["btn"+str(indice)].configure( text=nomboton, relief=FLAT,bg="#a7c14e" )
           
           self.userAlbum[indice]=nomboton
           event.widget.grid_forget()
            


    def crearPaquete(self,frm,frmVenta):
        self.btnPack={}
        canpack=len(self.primerPaquete)
        
        copiapack=self.primerPaquete
        

        filas = int(canpack/5)
        
        if filas == 0:
            filas+=1
        print(filas)
        ultimaco = canpack%5
        print(ultimaco)
        if ultimaco != 0:
            filas+=1
        
        bandera=False
        nom=0
        
        for i in range(filas):
            for j in range(5):
                try:
                    self.btnPack["btn"+'%d' %(nom)] = Button(frm,text=copiapack.pop(0))
                    self.btnPack["btn"+'%d' %(nom)].configure(width=10,relief="ridge")
                    self.btnPack["btn"+'%d' %(nom)].bind("<Button-1>", lambda event: self.pegarSticker(event,frmVenta) )
                    self.btnPack["btn"+'%d' %(nom)].grid(row=i,column=j,pady=2,padx=2,ipadx=10,ipady=10)
                    nom+=1
                except:
                    break
                    
        
        
    def verSiesta(self,nombtn):
        lista = self.enVenta #User // carta // precio
        self.listaVentas=[]
        
        for i in range(len(lista)):
            if lista[i][1] == nombtn and lista[i][0] != self.usuario:
                self.listaVentas.append(lista[i])
        
        if self.listaVentas == []:
            return []
        else:
            return self.listaVentas
########################################################################        
########################################################################        
########################################################################        
    def verificarDisponible(self,event):
        if event.widget.cget("bg") != "#a7c14e":
            nombtn = event.widget.cget("text")
            disponibles=[]
            disponibles=self.verSiesta(nombtn)
            print(disponibles)
        
        
        
        


    def crearBotones(self,frm):
        self.frmdic = {}
        for i in range(self.paginas):
            self.frmdic["frm"+str(i)] = Frame(frm)
            self.frmdic["frm"+str(i)].configure(bg="white")
            self.frmdic["frm"+str(i)].grid(row=0,column=1,padx=5)

        pagina=0
        self.fila=0
        self.columna=0
        inom=0
        while pagina < self.paginas:
            fi=self.fila
            co=self.columna
            i,j=0,0
            for h in range(fi,fi+10):
                j=0
                for k in range(co,co+5):
                    try:
                        self.btn["btn"+'%d' %(inom)] = Button(self.frmdic["frm"+str(pagina)],text=self.nom.pop(0))
                        self.btn["btn"+'%d' %(inom)].configure(width=10,relief="ridge")
                        self.btn["btn"+'%d' %(inom)].bind("<Button-1>", lambda event: self.verificarDisponible(event) )
                        self.btn["btn"+'%d' %(inom)].grid(row=i,column=j+1,pady=2,padx=2,ipadx=10,ipady=10)
                        self.frmdic["frm"+str(pagina)].grid_remove()
                        inom+=1
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
                    self.frmdic["frm"+str(anterior)].grid_remove()
                    self.frmdic["frm"+str(actual)].grid()
            except:
                True



    def crearFrame(self,frm):
        
        canpostales=len(self.Postales)
        
        for i in range(canpostales):
            self.nom.append("sticker #"+str(i))

        self.userAlbum.extend( self.nom )
        paginas=canpostales/50
        paginas=int(paginas)


        ultimacolumna=canpostales%5
        print("ultima columna",ultimacolumna)

        ultimafila= (canpostales - (paginas*50)) / 5
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

        













