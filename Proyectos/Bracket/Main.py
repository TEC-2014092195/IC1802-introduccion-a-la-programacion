from tkinter import *
from tkinter import messagebox
import Login_Admin
import Login_Usuario

v_main=Tk()

v_main.geometry("300x200+%d+%d" %((v_main.winfo_screenwidth() - 300) / 2,(v_main.winfo_screenheight() - 200) / 2))
v_main.configure(bg="#4faa2b")
v_main.title("Bracket")


frmAdmin=Frame(v_main)
frmAdmin.grid()
frmAdmin.configure(bg="#4faa2b")
frmAdmin.place(in_=v_main,relx=.5,rely=.5,anchor="c")

btnAdmin=Button(frmAdmin,text="Administrador")
btnAdmin.configure(command=lambda:Login_Admin.Administrador.ventana_admin(v_main))
btnAdmin.configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",12))
btnAdmin.grid(row=0,column=0)

btnUsuario=Button(frmAdmin,text="Usuario")
btnUsuario.configure(command=lambda:Login_Usuario.Usuario.ventana_usuario(v_main))
btnUsuario.configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",12))
btnUsuario.grid(row=0,column=1,padx=20)



v_main.mainloop()
