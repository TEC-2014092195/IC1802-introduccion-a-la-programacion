from tkinter import *
from tkinter import messagebox
import socket
import pickle
import clase_U_Inicio


class Principal():
    def Cargar():

        v_user_Inicio = Tk()

        print("usuario_Inicio")

        host = "localhost"

        port = 9999

        sock = socket.socket()

        sock.connect((host,port))


        usuario = "getusername"
        usuario = pickle.dumps(usuario)

        sock.send(usuario)

        usuario = sock.recv(1024)
        usuario = pickle.loads(usuario)


        sock.close()


        frm = Frame(v_user_Inicio)
        frm.grid(padx=10,pady=10)

        lbl = Label(frm,text="Nombre de usuario: ")
        lbl.grid(row=0,column=0)

        lbl = Label(frm,text=usuario)
        lbl.grid(row=0,column=1)

        lbl = Label(frm,text="Cantidad de billetes: ")
        lbl.grid(row=1,column=0)


        varBilletes=StringVar()
        lbl = Label(frm,textvariable=varBilletes)
        lbl.grid(row=1,column=1)

        print("usuario_Inicio")

        host = "localhost"

        port = 9999

        sock = socket.socket()

        sock.connect((host,port))
        clase=clase_U_Inicio.clase_U_Inicio(sock)


        clase.varDefault(usuario,varBilletes)

        frmBtn=Frame(v_user_Inicio)
        frmBtn.grid(row=1)

        clase.crearFrame(frmBtn)



        frmPaquete=LabelFrame(v_user_Inicio,text="Paquete")
        frmPaquete.grid(row=1,column=1,padx=10,sticky="n")

        frmVenta = LabelFrame(v_user_Inicio,text="Paquete")
        frmVenta.grid(row=0,column=1,padx=10,sticky="n")

        clase.crearPaquete(frmPaquete,frmVenta)

        sock.close()


        v_user_Inicio.mainloop()
