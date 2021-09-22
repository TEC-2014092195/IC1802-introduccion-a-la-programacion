from tkinter import *
from tkinter import messagebox
import clase_A_elegir


def crearbotones(event,canequipos,canbilletes,frm):
    try:
        cantidad = int(canequipos.get())
        billetes = int(canbilletes.get())
        crearStickers2 = clase_A_elegir.crearStickers()
        crearStickers2.crearFrame(cantidad,frm,billetes)
        event.widget.grid_remove()
    except:
        messagebox.showinfo("Album", "Ingrese los campos validos")



v_admin_elegir = Tk()


fram = Frame(v_admin_elegir)
fram.grid(padx=50,pady=50)


lbl = Label(fram,text="Cantidad de postales: ",justify="right")
lbl.grid(row=0 , column=0)

var_canequipos = StringVar()
ent_canequipos = Entry(fram,width=10,textvariable=var_canequipos)
ent_canequipos.grid(row=0,column=1,pady=5)

lbl = Label(fram,text="Cantidad de billetes: ",justify="right")
lbl.grid(row=1 , column=0)

var_canbilletes = StringVar()
ent_canbilletes = Entry(fram,width=10,textvariable=var_canbilletes)
ent_canbilletes.grid(row=1,column=1,pady=5)

frm = Frame(v_admin_elegir)
frm.grid(row=1)

btnconfirmar = Button(fram,text="CONFIRMAR")
btnconfirmar.grid(row=2, columnspan=2,pady=5)
btnconfirmar.bind("<Button-1>" , lambda event: crearbotones(event,var_canequipos,var_canbilletes,frm) )



v_admin_elegir.mainloop()
