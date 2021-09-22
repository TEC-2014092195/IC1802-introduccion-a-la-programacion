from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Admin_Agregar_Equipos

class Clase_C_Grupos():
    def VentanaCGrupos(v_main):

        v_cgrupos=Toplevel()

        v_cgrupos.geometry("300x200+%d+%d" %((v_cgrupos.winfo_screenwidth() - 300) / 2,(v_cgrupos.winfo_screenheight() - 200) / 2))
        v_cgrupos.configure(bg="#4faa2b")
        v_cgrupos.title("Bracket")

        frm = Frame(v_cgrupos)
        frm.configure(bg="#4faa2b")
        frm.grid()
        frm.place(relx=.5,rely=.5,anchor="c")


        lbl=Label(frm,text="Seleccione la cantidad de grupos")
        lbl.configure(fg="white",bg="#4faa2b",font=("Calibri",12))
        lbl.grid(pady=20)



            
        can=('8','4','2')
        varCantidad=StringVar()
        cbCantidad = ttk.Combobox(frm,textvariable=varCantidad,values=can)
        cbCantidad.configure(justify="center",width=5)
        def qfocus(event):
            event.widget.master.focus_set()
        cbCantidad.bind("<FocusIn>",qfocus)
        cbCantidad.set("-")
        cbCantidad.grid()

        def continuar(cantidad):
            if cantidad.get() != "-":
                v_cgrupos.destroy()
                Admin_Agregar_Equipos.ClaseAgregarEquipos.VentanaAdminAgregar(cantidad.get(),v_main)
            else:
                messagebox.showinfo("BM","No se ha elegido la cantidad")

        btnConfirmar=Button(frm,text="Confirmar")
        btnConfirmar.configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",11)) 
        btnConfirmar.configure(command=lambda:continuar(varCantidad) )
        btnConfirmar.grid(pady=20)

        def cerrar_con_equis():
            v_cgrupos.destroy()
            v_main.update()
            v_main.deiconify()

        v_cgrupos.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

        v_cgrupos.mainloop()
