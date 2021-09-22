from tkinter import *
from tkinter import messagebox
import pickle
import random
import socket
import pickle
import usuario_Inicio

class claseC_Main():

    def __init__(self):
        self.sock=0
    
    def crearNuevo(self):
        vtemp = Toplevel()
        frmtemp = Frame(vtemp)
        frmtemp.grid()
        lbl=Label(frmtemp,text="Nombre de nuevo usuario: ")
        lbl.grid(row=0,column=0)

        varUsuario=StringVar()
        entUsuario=Entry(frmtemp,textvariable=varUsuario)
        entUsuario.grid(row=0,column=1)

        def asignar(usuario):
            file = open("Template.txt","rb")
            ce = pickle.load(file)#cantidad cartas
            cb = pickle.load(file)#cantidad de billetes
            postales = pickle.load(file)#lista postales
            file.close()

            limite = ce * 0.30
            limite=int(limite)
            
            newt=[]
            for i in range(2):
                t=random.sample(postales,  limite )#limite es el 30 % asignado
                newt.extend(t)
            random.shuffle(newt)
            primerpaquete=[]
            for i in range( limite ):
                primerpaquete.append(random.choice(newt))
            
            f = open("Usuarios/Registrados/user_"+usuario+".txt","wb")
            pickle.dump(ce,f)
            pickle.dump(cb,f)
            pickle.dump(postales,f)
            pickle.dump(primerpaquete,f)
            f.close()

            
            
        
        def crear(usuario):
            usuario=usuario.strip()
            if usuario == "":
                messagebox.showinfo("Album","Campo requerido")
            else:    
                file = open("Usuarios/Usuarios.txt","rb")
                usuarios=pickle.load(file)
                file.close()

                
                if usuario in usuarios:
                    messagebox.showinfo("Album","Usuario ya existe")
                    varUsuario.set("")
                else:
                    usuarios.append(usuario)
                    
                    asignar(usuario)
                    
                    file = open("Usuarios/Usuarios.txt","wb")
##                    usuarios=[] para borrar
                    pickle.dump(usuarios,file)
                    file.close()
                    print(usuarios)
                    vtemp.destroy()
            
            
        btnGuardar=Button(frmtemp,text="Crear Usuario")
        btnGuardar.grid(row=1,column=1,pady=10)
        btnGuardar.configure(command=lambda: crear( varUsuario.get() ) )



    def conectarServer(self,usuario):
        print("Cliente")
        host = "localhost"
        port = 9999
        sock = socket.socket()
        sock.connect((host,port))
        
        dato="userServer"
        dato = pickle.dumps(dato)
        sock.send(dato)
        
        validar = False
        validar = sock.recv(1024)
        validar = pickle.loads(validar)
        print(type(validar))
        usuario=pickle.dumps(usuario)
        sock.send(usuario)

        
        sock.close()

        

    def verificarIngreso(self,usuario,v_cliente_main):
        usuario=usuario.strip()
        if usuario == "":
            messagebox.showinfo("Album","Campo requerido")
        else:    
            file = open("Usuarios/Usuarios.txt","rb")
            usuarios=pickle.load(file)
            file.close()

            
            if usuario in usuarios:
                messagebox.showinfo("Album","Bienvenido "+usuario)
                #heredar a la siguiente ventana nombre de usuario
                self.conectarServer(usuario)
                
                v_cliente_main.destroy()
                usuario_Inicio.Principal.Cargar()

                
                
                
            else:
                messagebox.showinfo("Album","Debe crear una cuenta primero")
