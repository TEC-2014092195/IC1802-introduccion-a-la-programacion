from tkinter import *
from tkinter import messagebox
import clase_U_Ingresar

v_cliente_main=Tk()

clase_U = clase_U_Ingresar.claseC_Main()
frm = Frame(v_cliente_main)
frm.grid(padx=10,pady=10)


lbl=Label(frm,text="Nombre de usuario: ")
lbl.grid(row=0,column=0)

varUsuario=StringVar()
entUsuario=Entry(frm,textvariable=varUsuario)
entUsuario.grid(row=0,column=1)

btnNuevo=Button(frm,text="Crear Cuenta")
btnNuevo.grid(row=1,column=0,pady=10)
btnNuevo.configure(command=lambda: clase_U.crearNuevo())

btnIngresar=Button(frm,text="INGRESAR")
btnIngresar.grid(row=1,column=1,pady=10)
btnIngresar.configure(command=lambda: clase_U.verificarIngreso( varUsuario.get(),v_cliente_main ))


v_cliente_main.update_idletasks()#primero actualiza las cantidades
alto=v_cliente_main.winfo_height()
ancho=v_cliente_main.winfo_width()
screenwidth = ( v_cliente_main.winfo_screenwidth() - ancho )  / 2
screenheight = ( v_cliente_main.winfo_screenheight() - alto )  / 2
v_cliente_main.geometry("%dx%d+%d+%d" %( ancho , alto , screenwidth , screenheight ) )


v_cliente_main.mainloop()
