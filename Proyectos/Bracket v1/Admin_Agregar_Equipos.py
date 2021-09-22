from tkinter import *
from tkinter import messagebox
import Clases



class ClaseAgregarEquipos():
    def VentanaAdminAgregar(v_main):
        v = Toplevel()

        largo="630"
        ancho="660"
        v.geometry(ancho+"x"+largo+"+%d+0" %( (v.winfo_screenwidth() - int(ancho)) / 2) )

        v.configure(bg="#6ba134")
        v.title("Bracket Mundial")

        frameDefinir = Frame(v)
        frameDefinir.configure(bg="#6ba134")
        frameDefinir.grid()
        frameDefinir.place(x=0,y=0)

        #----------------Grupo A--------------------
        f=0
        c=0
        lblGrupoA=Label( frameDefinir,text="Grupo A" , bg="#6ba134", foreground="white")
        lblGrupoA.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoA=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoA.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoA_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoA_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoA=StringVar()
        varGrupoA.set("")
        entGrupoA=Entry( frameDefinir,textvariable=varGrupoA,width=25,bd=0 )
        entGrupoA.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo B--------------------
        f=0
        c+=1
        lblGrupoB=Label( frameDefinir,text="Grupo B" , bg="#6ba134", foreground="white" )
        lblGrupoB.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoB=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoB.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoB_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoB_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoB=StringVar()
        varGrupoB.set("")
        entGrupoB=Entry( frameDefinir,textvariable=varGrupoB,width=25,bd=0 )
        entGrupoB.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo C--------------------
        f=0
        c+=1
        lblGrupoC=Label( frameDefinir,text="Grupo C" , bg="#6ba134", foreground="white" )
        lblGrupoC.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoC=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoC.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoC_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoC_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoC=StringVar()
        varGrupoC.set("")
        entGrupoC=Entry( frameDefinir,textvariable=varGrupoC,width=25,bd=0 )
        entGrupoC.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo D--------------------
        f=0
        c+=1
        lblGrupoD=Label( frameDefinir,text="Grupo D" , bg="#6ba134", foreground="white" )
        lblGrupoD.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoD=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoD.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoD_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoD_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoD=StringVar()
        varGrupoD.set("")
        entGrupoD=Entry( frameDefinir,textvariable=varGrupoD,width=25 ,bd=0 )
        entGrupoD.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo E--------------------
        f=8
        c=0
        lblGrupoE=Label( frameDefinir,text="Grupo E" , bg="#6ba134", foreground="white" )
        lblGrupoE.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoE=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 , bd=0 )
        lstGrupoE.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoE_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoE_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoE=StringVar()
        varGrupoE.set("")
        entGrupoE=Entry( frameDefinir,textvariable=varGrupoE,width=25 ,bd=0 )
        entGrupoE.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo F--------------------
        f=8
        c+=1
        lblGrupoF=Label( frameDefinir,text="Grupo F" , bg="#6ba134", foreground="white" )
        lblGrupoF.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoF=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoF.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoF_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoF_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoF=StringVar()
        varGrupoF.set("")
        entGrupoF=Entry( frameDefinir,textvariable=varGrupoF,width=25 ,bd=0 )
        entGrupoF.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo G--------------------
        f=8
        c+=1
        lblGrupoG=Label( frameDefinir,text="Grupo G" , bg="#6ba134", foreground="white" )
        lblGrupoG.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoG=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoG.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoG_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoG_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoG=StringVar()
        varGrupoG.set("")
        entGrupoG=Entry( frameDefinir,textvariable=varGrupoG,width=25 ,bd=0 )
        entGrupoG.grid( row=f,column=c,padx=5,pady=3 )

        #----------------Grupo H--------------------
        f=8
        c+=1
        lblGrupoH=Label( frameDefinir,text="Grupo H" , bg="#6ba134", foreground="white" )
        lblGrupoH.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lstGrupoH=Listbox( frameDefinir,width=25,height=6,activestyle='none',selectbackground="white",selectforeground="black",highlightthickness=0 ,bd=0 )
        lstGrupoH.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        lblGrupoH_entrada=Label( frameDefinir,text="Ingrese nombre de Equipo\n|\nV" , bg="#6ba134", foreground="white" )
        lblGrupoH_entrada.grid( row=f,column=c,padx=5,pady=3 )

        f+=1
        varGrupoH=StringVar()
        varGrupoH.set("")
        entGrupoH=Entry( frameDefinir,textvariable=varGrupoH,width=25 ,bd=0 )
        entGrupoH.grid( row=f,column=c,padx=5,pady=3 )

        ########
        ########
        ########
        ########
        #-----Botones Agregar---------------------------------------------------------------

        f=4
        c=0
        btnGrupoA=Clases.Boton_Grupos( lstGrupoA, varGrupoA ,lstGrupoB,lstGrupoC,lstGrupoD,lstGrupoE,lstGrupoF,lstGrupoG,lstGrupoH, frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoA.configure(command=btnGrupoA.AgregarEquipo)
        btnGrupoA.grid( row=f,column=c,padx=5,pady=3 )

        c+=1
        btnGrupoB=Clases.Boton_Grupos( lstGrupoB, varGrupoB ,lstGrupoA,lstGrupoC,lstGrupoD,lstGrupoE,lstGrupoF,lstGrupoG,lstGrupoH ,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoB.configure(command=btnGrupoB.AgregarEquipo)
        btnGrupoB.grid( row=f,column=c,padx=5,pady=3 )

        c+=1
        btnGrupoC=Clases.Boton_Grupos( lstGrupoC, varGrupoC ,lstGrupoA,lstGrupoB,lstGrupoD,lstGrupoE,lstGrupoF,lstGrupoG,lstGrupoH ,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoC.configure(command=btnGrupoC.AgregarEquipo)
        btnGrupoC.grid( row=f,column=c,padx=5,pady=3 )

        c+=1
        btnGrupoD=Clases.Boton_Grupos( lstGrupoD, varGrupoD ,lstGrupoA,lstGrupoB,lstGrupoC,lstGrupoE,lstGrupoF,lstGrupoG,lstGrupoH,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoD.configure(command=btnGrupoD.AgregarEquipo)
        btnGrupoD.grid( row=f,column=c,padx=5,pady=3 )

        f=12
        c=0
        btnGrupoE=Clases.Boton_Grupos( lstGrupoE, varGrupoE ,lstGrupoA,lstGrupoB,lstGrupoC,lstGrupoD,lstGrupoF,lstGrupoG,lstGrupoH,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoE.configure(command=btnGrupoE.AgregarEquipo)
        btnGrupoE.grid( row=f,column=c,padx=5,pady=3 )

        c+=1
        btnGrupoF=Clases.Boton_Grupos( lstGrupoF, varGrupoF ,lstGrupoA,lstGrupoB,lstGrupoC,lstGrupoD,lstGrupoE,lstGrupoG,lstGrupoH,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoF.configure(command=btnGrupoF.AgregarEquipo)
        btnGrupoF.grid( row=f,column=c,padx=5,pady=3 )

        c+=1
        btnGrupoG=Clases.Boton_Grupos( lstGrupoG, varGrupoG ,lstGrupoA,lstGrupoB,lstGrupoC,lstGrupoD,lstGrupoE,lstGrupoF,lstGrupoH ,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoG.configure(command=btnGrupoG.AgregarEquipo)
        btnGrupoG.grid( row=f,column=c,padx=5,pady=3 )

        c+=1
        btnGrupoH=Clases.Boton_Grupos( lstGrupoH, varGrupoH ,lstGrupoA,lstGrupoB,lstGrupoC,lstGrupoD,lstGrupoE,lstGrupoF,lstGrupoG ,frameDefinir,text="AGREGAR", relief=FLAT , bg="#2c5559", foreground="white" )
        btnGrupoH.configure(command=btnGrupoH.AgregarEquipo)
        btnGrupoH.grid( row=f,column=c,padx=5,pady=3 )

        #-----Limpiar Listas--------------------------------------------------

        f=5
        c=0
        btnGrupoA_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoA_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoA))
        btnGrupoA_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        c+=1
        btnGrupoB_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoB_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoB))
        btnGrupoB_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        c+=1
        btnGrupoC_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoC_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoC))
        btnGrupoC_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        c+=1
        btnGrupoD_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoD_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoD))
        btnGrupoD_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        f=13
        c=0
        btnGrupoE_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoE_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoE))
        btnGrupoE_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        c+=1
        btnGrupoF_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoF_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoF))
        btnGrupoF_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        c+=1
        btnGrupoG_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoG_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoG))
        btnGrupoG_limpiar.grid( row=f,column=c,padx=5,pady=3 )


        c+=1
        btnGrupoH_limpiar = Button( frameDefinir,text="LIMPIAR LISTA", relief=FLAT , bg="#edbe34", foreground="#47351d" )
        btnGrupoH_limpiar.configure(command=lambda:Clases.Limpiar.LimpiarLista(lstGrupoH))
        btnGrupoH_limpiar.grid( row=f,column=c,padx=5,pady=3 )

        ##############
        ##############
        ##############
        ##############
        ##############
        ##############
        ##############
        #------------------------------------------------------------Boton Confirmación------------------------------------------------------------

        #f+=1
        btnConfirmar = Clases.Boton_Confirmacion( lstGrupoA,lstGrupoB,lstGrupoC,lstGrupoD,lstGrupoE,lstGrupoF,lstGrupoG,lstGrupoH,frameDefinir,text="CONFIRMAR", relief=RIDGE )
        btnConfirmar.configure( relief=FLAT , bg="#2c5559", foreground="white" )
        btnConfirmar.configure(command=lambda:btnConfirmar.ValidarListas(v_main))
        btnConfirmar.grid( row=14,column=1,columnspan=2,padx=5,pady=10 )
        #-----------------------Cerrar con equis
        def cerrar_con_equis():
            v.destroy()
            v_main.update()
            v_main.deiconify()
        
        v.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

        v.mainloop()
