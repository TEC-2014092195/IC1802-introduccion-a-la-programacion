##
##def cerrar_con_equis():
##        ventana_modo_admin.destroy()
##        v.update()
##        v.deiconify()
##
##    ventana_modo_admin.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

from tkinter import *
from tkinter import messagebox


class Login():
    
    def Verificar(ID,ventana_usuario,v_main):

        try:

            if ID.get()=="":
                messagebox.showinfo("BM","Ingrese al menos un caracter")
                
            if ID.get()!="":
                file=open("Usuarios.txt","r")
                lista=file.readlines()
                
                bandera=False
                Registro="Registrado"
                nom_usuario=""
                id_bracket=""
                for i in range(len(lista)):
                    if lista[i].split(",")[0] == ID.get() and lista[i].split(",")[2] == "Nuevo":
                        bandera=True
                        Registro="Nuevo"
                        nom_usuario=lista[i].split(",")[1]
                        id_bracket=lista[i].split(",")[0]
                    elif lista[i].split(",")[0] == ID.get() and lista[i].split(",")[2] == "Registrado":
                        bandera=True
                        Registro="Registrado"
                        nom_usuario=lista[i].split(",")[1]
                        id_bracket=lista[i].split(",")[0]
                
                if bandera == True :
                    messagebox.showinfo("BM","Ingreso satisfactorio")
                    messagebox.showinfo("BM","Bienvenido tipo de usuario "+Registro)
                    if Registro == "Nuevo":
                        ventana_usuario.destroy()
                        import Usuario_Bracket_Nuevo
                        Usuario_Bracket_Nuevo.ClaseUsuarioNuevo.VentanaUsuarioNuevo(v_main,nom_usuario,id_bracket)
                        file.close()
                    else:
                        ventana_usuario.destroy()
                        import Usuario_Bracket_Registrado
                        Usuario_Bracket_Registrado.ClaseUsuarioRegistrado.VentanaUsuarioRegistrado(v_main,nom_usuario,id_bracket)
                        file.close()
                else:
                    messagebox.showwarning("BM","El Usuario no existe\nCree su propio Bracket primero")
                    ID.set("")

                file.close()
            
                
        except:
            messagebox.showwarning("BM","El archivo Usuarios.txt no existe")
            ID.set("")
            





            
    def AccionBracketNew(frmBracket,frmBracketNew):
        frmBracket.place_forget()
        frmBracketNew.place(relx=.5,rely=.5,anchor="c")





    def CrearBracket( varIDBracketNew,varNombre,frmBracket,frmBracketNew ):
        try:
            if varIDBracketNew.get()=="" and varNombre.get()=="":
                messagebox.showinfo("BM","Id y su nombre\nSon campos obligatorios")
                
                
            if varIDBracketNew.get()=="":
                messagebox.showinfo("BM","Ingrese al menos un caracter en el Nuevo ID")
                
                
            if varNombre.get()=="":
                messagebox.showinfo("BM","Ingrese al menos un caracter en el campo de Nombre")
                
                
            if varIDBracketNew.get()!="" and varNombre.get()!="":
                
                file=open("Usuarios.txt","r")
                lista=file.readlines()
                
                bandera=False
                for i in range(len(lista)):
                    if lista[i].split(",")[0] == varIDBracketNew.get():
                        bandera=True
                
                if bandera == True :
                    messagebox.showwarning("BM","El Usuario ya existe")
                    varIDBracketNew.set("")
                    varNombre.set("")
                else:
                    file.close()
                    file=open("Usuarios.txt","a")
                    file.write( varIDBracketNew.get() )
                    file.write(",")
                    file.write( varNombre.get() )
                    file.write(",")
                    file.write("Nuevo")
                    file.write(",")
                    file.write("\n")

                    varIDBracketNew.set("")
                    varNombre.set("")

                    
                    frmBracketNew.place_forget()
                    frmBracket.place(relx=.5,rely=.5,anchor="c")

                    file.close()

                file.close()

            varIDBracketNew.set("")
            varNombre.set("")
                
        except:
            file=open("Usuarios.txt","w")
            messagebox.showwarning("BM","El archivo Usuarios.txt se ha creado\nRazón: No existía \nAhora sí puede intentar de nuevo")
            varIDBracketNew.set("")
            varNombre.set("")
            file.close()
        
    

class Usuario():
    def ventana_usuario(v_main):
        v_main.withdraw()
        v_usuario = Toplevel()
        v_usuario.geometry("300x300+%d+%d" %((v_main.winfo_screenwidth() - 300) / 2,(v_main.winfo_screenheight() - 300) / 2))
        v_usuario.configure(bg="#4faa2b")
        
        frmBracket=Frame(v_usuario)
        frmBracket.grid()
        frmBracket.configure(bg="#4faa2b")
        frmBracket.place(in_=v_usuario,relx=.5,rely=.5,anchor="c")

        f=0
        c=0
        lblIDBracket=Label(frmBracket,text="ID de Bracket: ",bg="#4faa2b",font=("Calibri",11),fg="#121f0a")
        lblIDBracket.grid(row=f,column=c)

        c=1
        varIDBracket=StringVar()
        entrIDBracket=Entry(frmBracket,textvariable=varIDBracket)
        entrIDBracket.configure(bd=0,font=("Calibri",11))
        entrIDBracket.grid(row=f,column=c,pady=5)

        f+=1
        c=0   
        btnIngresarID=Button(frmBracket,text="Ingresar")
        btnIngresarID.grid(row=f,column=c,columnspan=2,pady=5)
        btnIngresarID.configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",11))
        btnIngresarID.configure(command=lambda: Login.Verificar(varIDBracket ,v_usuario ,v_main ))

        frmBracketNew=Frame(v_usuario)
        frmBracketNew.grid()
        frmBracketNew.configure(bg="#4faa2b")
        frmBracketNew.place(x=100,y=100)
        frmBracketNew.place_forget()
        #------------
        f=0
        c=0
        lblIDBracket=Label(frmBracketNew,text="Nuevo ID de Bracket: ",bg="#4faa2b",font=("Calibri",11),fg="#121f0a")
        lblIDBracket.grid(row=f,column=c)

        c=1
        varIDBracketNew=StringVar()
        entrIDBracketNew=Entry(frmBracketNew,textvariable=varIDBracketNew)
        entrIDBracketNew.configure(bd=0,font=("Calibri",11))
        entrIDBracketNew.grid(row=f,column=c,pady=5)


        f+=1
        c=0
        lblNombre=Label(frmBracketNew,text="Su nombre: ",bg="#4faa2b",font=("Calibri",11),fg="#121f0a")
        lblNombre.grid(row=f,column=c)

        c=1
        varNombre=StringVar()
        entrNombre=Entry(frmBracketNew,textvariable=varNombre)
        entrNombre.configure(bd=0,font=("Calibri",11))
        entrNombre.grid(row=f,column=c,pady=5)



        f+=1
        c=0   
        btnIngresarIDNew=Button(frmBracketNew,text="Agregar")
        btnIngresarIDNew.grid(row=f,column=c,columnspan=2,pady=5)
        btnIngresarIDNew.configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",11))
        btnIngresarIDNew.configure(command=lambda: Login.CrearBracket( varIDBracketNew,varNombre,frmBracket,frmBracketNew ))

        f+=1
        btnCrearID=Button(frmBracket,text="Crear Nueva Cuenta")
        btnCrearID.grid(row=f,column=c,columnspan=2,pady=5)
        btnCrearID.configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11))
        btnCrearID.configure(command=lambda: Login.AccionBracketNew(frmBracket,frmBracketNew))
        
        


        def cerrar_con_equis():
            v_usuario.destroy()
            v_main.update()
            v_main.deiconify()

        v_usuario.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

        v_usuario.mainloop()

        


        
