from tkinter import *
from tkinter import messagebox
import Admin_C_Grupos

class Login():
    
    def Verificar(user,password,ventana_admin , v_main):
        if user.get() == "admin" and password.get() == "admin" :
            messagebox.showinfo("BM","Ingreso satisfactorio")
            ventana_admin.destroy()
            
            Admin_C_Grupos.Clase_C_Grupos.VentanaCGrupos(v_main)
            
        else:
            messagebox.showwarning("BM","Usuario o contraseña invalidos\nIntente de nuevo")
            user.set("")
            password.set("")
            
        
        


class Administrador():
    def ventana_admin(v_main):
        v_main.withdraw()
        v_admin = Toplevel()
        v_admin.geometry("300x200+%d+%d" %((v_admin.winfo_screenwidth() - 300) / 2,(v_admin.winfo_screenheight() - 200) / 2))
        v_admin.configure(bg="#4faa2b")

        
        frmAdmin=Frame(v_admin)
        frmAdmin.grid()
        frmAdmin.configure(bg="#4faa2b")
        frmAdmin.place(in_=v_admin,relx=.5,rely=.5,anchor="c")

        f=0
        c=0
        lblUsuario=Label(frmAdmin,text="Usuario: ",bg="#4faa2b",font=("Calibri",11),fg="#121f0a")
        lblUsuario.grid(row=f,column=c)

        c=1
        varUsuarioAdmin=StringVar()
        entrUsuarioAdmin=Entry(frmAdmin,textvariable=varUsuarioAdmin)
        entrUsuarioAdmin.configure(bd=0,font=("Calibri",11))
        entrUsuarioAdmin.grid(row=f,column=c,pady=5)

        f+=1
        c=0
        lblPass=Label(frmAdmin,text="Contraseña: ",bg="#4faa2b",font=("Calibri",11),fg="#121f0a")
        lblPass.grid(row=f,column=c)

        c=1
        varPassAdmin=StringVar()
        entrPassAdmin=Entry(frmAdmin,textvariable=varPassAdmin,show="*")
        entrPassAdmin.configure(bd=0,font=("Calibri",11))
        entrPassAdmin.grid(row=f,column=c)

        f+=1
        c=0
            
        btnIngresarAdmin=Button(frmAdmin,text="Ingresar")
        btnIngresarAdmin.grid(row=f,column=c,columnspan=2,pady=5)
        btnIngresarAdmin.configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",11)) #Azul .configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",12))
        btnIngresarAdmin.configure(command=lambda: Login.Verificar(varUsuarioAdmin ,varPassAdmin , v_admin , v_main ))



        def cerrar_con_equis():
            v_admin.destroy()
            v_main.update()
            v_main.deiconify()

        v_admin.protocol('WM_DELETE_WINDOW', cerrar_con_equis)
