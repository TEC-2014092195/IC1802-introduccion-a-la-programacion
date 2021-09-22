from tkinter import *
from tkinter import messagebox
import Clase_Admin_Agregar

class ClaseAgregarEquipos():
    def VentanaAdminAgregar(c_grupos,v_main):
        v_admin=Toplevel()
        
        v_admin.geometry("800x600+%d+%d" %((v_admin.winfo_screenwidth() - 800) / 2,(v_admin.winfo_screenheight() - 600) / 2))
        
        v_admin.configure(bg="#4faa2b")


        v_admin.title("Bracket Mundial")


        frm=Frame(v_admin)
        frm.grid()
        frm.configure(bg="#4faa2b")
        frm.place(relx=.5,rely=.5,anchor="c")




        g=('GrupoA','GrupoB','GrupoC','GrupoD','GrupoE','GrupoF',
           'GrupoG','GrupoH','GrupoI','GrupoJ','GrupoK','GrupoL','GrupoM','GrupoN')
        lst = {}
        var = {}
        ent = {}
        btn = {}
        
        can_grupos=int(c_grupos)
        print(can_grupos)
        
        c=0
        f=0
        for i in range(can_grupos):
            mitad=can_grupos/2

            if i < mitad:
                f=0
                
                lbl=Label( frm , text=(g[i]) )
                lbl.configure(fg="white",bg="#4faa2b")
                lbl.grid(row=f,column=c)

                f+=1
                lst[ "lst"+str(g[i]) ]=Listbox( frm )
                lst[ "lst"+str(g[i]) ].configure( width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
                lst[ "lst"+str(g[i]) ].grid(row=f,column=c)
                
                f+=1
                lbl=Label( frm , text="Ingrese nombre de Equipo\n|\nV" )
                lbl.configure(fg="white",bg="#4faa2b")
                lbl.grid(row=f,column=c,padx=5,pady=3)

                f+=1
                var[ "var"+str(g[i]) ] = StringVar()
                ent[ "ent"+str(g[i]) ] = Entry( frm,textvariable=var[ "var"+str(g[i]) ] )
                ent[ "ent"+str(g[i]) ].configure( width=25,bd=0 )
                ent[ "ent"+str(g[i]) ].grid( row=f,column=c,padx=5,pady=3 )

                f+=1
                btn[ "btnAgregar"+str(g[i]) ] = Clase_Admin_Agregar.BotonAgregar(var,lst,g[i], frm,text="AGREGAR" )
                btn[ "btnAgregar"+str(g[i]) ].configure(bg="#0b2532",bd=0,relief=FLAT,fg="white")
                btn[ "btnAgregar"+str(g[i]) ].configure( command= btn[ "btnAgregar"+str(g[i]) ].Agregar)
                btn[ "btnAgregar"+str(g[i]) ].grid( row=f,column=c,padx=5,pady=3 )
                
                f+=1
                btn[ "btnLimpiar"+str(g[i]) ] = Clase_Admin_Agregar.BotonLimpiar( lst,g[i], frm,text="LIMPIAR LISTA" )
                btn[ "btnLimpiar"+str(g[i]) ].configure( relief=FLAT , bg="#edbe34", foreground="#47351d" )
                btn[ "btnLimpiar"+str(g[i]) ].configure( command=btn[ "btnLimpiar"+str(g[i]) ].Limpiar )
                btn[ "btnLimpiar"+str(g[i]) ].grid( row=f,column=c,padx=5,pady=3 )
                
                c+=1
                if i == (mitad-1):
                    c=0
            else:
                f=6

                lbl=Label( frm , text=(g[i]) )
                lbl.configure(fg="white",bg="#4faa2b")
                lbl.grid(row=f,column=c)

                f+=1
                lst[ "lst"+str(g[i]) ]=Listbox( frm )
                lst[ "lst"+str(g[i]) ].configure( width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
                lst[ "lst"+str(g[i]) ].grid(row=f,column=c)
                
                f+=1
                lbl=Label( frm , text="Ingrese nombre de Equipo\n|\nV" )
                lbl.configure(fg="white",bg="#4faa2b")
                lbl.grid(row=f,column=c,padx=5,pady=3)

                f+=1
                var[ "var"+str(g[i]) ] = StringVar()
                ent[ "ent"+str(g[i]) ] = Entry( frm,textvariable=var[ "var"+str(g[i]) ] )
                ent[ "ent"+str(g[i]) ].configure( width=25,bd=0 )
                ent[ "ent"+str(g[i]) ].grid( row=f,column=c,padx=5,pady=3 )

                f+=1
                btn[ "btnAgregar"+str(g[i]) ] = Clase_Admin_Agregar.BotonAgregar(var,lst,g[i], frm,text="AGREGAR" )
                btn[ "btnAgregar"+str(g[i]) ].configure(bg="#0b2532",bd=0,relief=FLAT,fg="white")
                btn[ "btnAgregar"+str(g[i]) ].configure( command= btn[ "btnAgregar"+str(g[i]) ].Agregar)
                btn[ "btnAgregar"+str(g[i]) ].grid( row=f,column=c,padx=5,pady=3 )
                
                f+=1
                btn[ "btnLimpiar"+str(g[i]) ] = Clase_Admin_Agregar.BotonLimpiar( lst,g[i], frm,text="LIMPIAR LISTA" )
                btn[ "btnLimpiar"+str(g[i]) ].configure( relief=FLAT , bg="#edbe34", foreground="#47351d" )
                btn[ "btnLimpiar"+str(g[i]) ].configure( command=btn[ "btnLimpiar"+str(g[i]) ].Limpiar )
                btn[ "btnLimpiar"+str(g[i]) ].grid( row=f,column=c,padx=5,pady=3 )
                
                c+=1

        f+=1
        btnGuardar = Button(frm,text="GUARDAR")
        btnGuardar.configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",pady=5,padx=5 )
        btnGuardar.configure(command=lambda: Clase_Admin_Agregar.Guardar.Verificar(lst,can_grupos,v_admin,v_main))
        btnGuardar.grid(row=f,columnspan=4,padx=5,pady=3)

        def cerrar_con_equis():
            v_admin.destroy()
            v_main.update()
            v_main.deiconify()

        v_admin.protocol('WM_DELETE_WINDOW', cerrar_con_equis)
        
        v_admin.mainloop()

