from tkinter import *
from tkinter import messagebox
import Clases_Bracket_Nuevo

class ClaseUsuarioNuevo():
    def VentanaUsuarioNuevo(v_main,nom_usuario,id_bracket):
        
    
        v=Toplevel()

        v.geometry("1030x700+%d+0" %((v.winfo_screenwidth() - 1030) / 2))
        v.title("Bracket de Torneos")


        frmUsuario=Frame(v)
        frmUsuario.grid()
        frmUsuario.place(in_=v,relx=.5,y=0)
        
        lbluser=Label(frmUsuario,text="Nombre de Usuario")
        lbluser.grid(row=0,column=0)
        lblnom=Label(frmUsuario,text=nom_usuario)
        lblnom.grid(row=1,column=0)
        
        
        #-----Frame Grupos Izquierda-----
        frmGruposIzq=Frame(v)
        frmGruposIzq.grid()
        frmGruposIzq.place(in_=v,relx=.5,rely=.5,anchor="c")

        f=0
        lblGrupoA=Label(frmGruposIzq,text="Grupo A")
        lblGrupoA.grid(row=f,column=0,pady=10)

        f+=1
        btnA1=Clases_Bracket_Nuevo.BotonesGrupos("A",1,frmGruposIzq,text="")
        btnA1.grid(row=f,column=0)

        f+=1
        btnA2=Clases_Bracket_Nuevo.BotonesGrupos("A",2,frmGruposIzq,text="")
        btnA2.grid(row=f,column=0)

        f+=1
        btnA3=Clases_Bracket_Nuevo.BotonesGrupos("A",3,frmGruposIzq,text="")
        btnA3.grid(row=f,column=0)

        f+=1
        btnA4=Clases_Bracket_Nuevo.BotonesGrupos("A",4,frmGruposIzq,text="")
        btnA4.grid(row=f,column=0)
        #-----------------------------Grupo B-------------------
        f+=1
        lblGrupoB=Label(frmGruposIzq,text="Grupo B")
        lblGrupoB.grid(row=f,column=0,pady=10)

        f+=1
        btnB1=Clases_Bracket_Nuevo.BotonesGrupos("B",1,frmGruposIzq,text="")
        btnB1.grid(row=f,column=0)

        f+=1
        btnB2=Clases_Bracket_Nuevo.BotonesGrupos("B",2,frmGruposIzq,text="")
        btnB2.grid(row=f,column=0)

        f+=1
        btnB3=Clases_Bracket_Nuevo.BotonesGrupos("B",3,frmGruposIzq,text="")
        btnB3.grid(row=f,column=0)

        f+=1
        btnB4=Clases_Bracket_Nuevo.BotonesGrupos("B",4,frmGruposIzq,text="")
        btnB4.grid(row=f,column=0)

        #-----------------------------Grupo C-------------------
        f+=1
        lblGrupoC=Label(frmGruposIzq,text="Grupo C")
        lblGrupoC.grid(row=f,column=0,pady=10)

        f+=1
        btnC1=Clases_Bracket_Nuevo.BotonesGrupos("C",1,frmGruposIzq,text="")
        btnC1.grid(row=f,column=0)

        f+=1
        btnC2=Clases_Bracket_Nuevo.BotonesGrupos("C",2,frmGruposIzq,text="")
        btnC2.grid(row=f,column=0)

        f+=1
        btnC3=Clases_Bracket_Nuevo.BotonesGrupos("C",3,frmGruposIzq,text="")
        btnC3.grid(row=f,column=0)

        f+=1
        btnC4=Clases_Bracket_Nuevo.BotonesGrupos("C",4,frmGruposIzq,text="")
        btnC4.grid(row=f,column=0)

        #-----------------------------Grupo D-------------------
        f+=1
        lblGrupoD=Label(frmGruposIzq,text="Grupo D")
        lblGrupoD.grid(row=f,column=0,pady=10)

        f+=1
        btnD1=Clases_Bracket_Nuevo.BotonesGrupos("D",1,frmGruposIzq,text="")
        btnD1.grid(row=f,column=0)

        f+=1
        btnD2=Clases_Bracket_Nuevo.BotonesGrupos("D",2,frmGruposIzq,text="")
        btnD2.grid(row=f,column=0)

        f+=1
        btnD3=Clases_Bracket_Nuevo.BotonesGrupos("D",3,frmGruposIzq,text="")
        btnD3.grid(row=f,column=0)

        f+=1
        btnD4=Clases_Bracket_Nuevo.BotonesGrupos("D",4,frmGruposIzq,text="")
        btnD4.grid(row=f,column=0)
        ################################
        ################################
        ################################
        #-----Frame Grupos Derecha-----

        f=0
        c=10
        lblGrupoE=Label(frmGruposIzq,text="Grupo E")
        lblGrupoE.grid(row=f,column=c,pady=10)

        f+=1
        btnE1=Clases_Bracket_Nuevo.BotonesGrupos("E",1,frmGruposIzq,text="")
        btnE1.grid(row=f,column=c)

        f+=1
        btnE2=Clases_Bracket_Nuevo.BotonesGrupos("E",2,frmGruposIzq,text="")
        btnE2.grid(row=f,column=c)

        f+=1
        btnE3=Clases_Bracket_Nuevo.BotonesGrupos("E",3,frmGruposIzq,text="")
        btnE3.grid(row=f,column=c)

        f+=1
        btnE4=Clases_Bracket_Nuevo.BotonesGrupos("E",4,frmGruposIzq,text="")
        btnE4.grid(row=f,column=c)

        #-----------------------------Grupo F-------------------
        f+=1
        lblGrupoF=Label(frmGruposIzq,text="Grupo F")
        lblGrupoF.grid(row=f,column=c,pady=10)

        f+=1
        btnF1=Clases_Bracket_Nuevo.BotonesGrupos("F",1,frmGruposIzq,text="")
        btnF1.grid(row=f,column=c)

        f+=1
        btnF2=Clases_Bracket_Nuevo.BotonesGrupos("F",2,frmGruposIzq,text="")
        btnF2.grid(row=f,column=c)

        f+=1
        btnF3=Clases_Bracket_Nuevo.BotonesGrupos("F",3,frmGruposIzq,text="")
        btnF3.grid(row=f,column=c)

        f+=1
        btnF4=Clases_Bracket_Nuevo.BotonesGrupos("F",4,frmGruposIzq,text="")
        btnF4.grid(row=f,column=c)

        #-----------------------------Grupo G-------------------
        f+=1
        lblGrupoG=Label(frmGruposIzq,text="Grupo G")
        lblGrupoG.grid(row=f,column=c,pady=10)

        f+=1
        btnG1=Clases_Bracket_Nuevo.BotonesGrupos("G",1,frmGruposIzq,text="")
        btnG1.grid(row=f,column=c)

        f+=1
        btnG2=Clases_Bracket_Nuevo.BotonesGrupos("G",2,frmGruposIzq,text="")
        btnG2.grid(row=f,column=c)

        f+=1
        btnG3=Clases_Bracket_Nuevo.BotonesGrupos("G",3,frmGruposIzq,text="")
        btnG3.grid(row=f,column=c)

        f+=1
        btnG4=Clases_Bracket_Nuevo.BotonesGrupos("G",4,frmGruposIzq,text="")
        btnG4.grid(row=f,column=c)

        #-----------------------------Grupo H-------------------
        f+=1
        lblGrupoH=Label(frmGruposIzq,text="Grupo H")
        lblGrupoH.grid(row=f,column=c,pady=10)

        f+=1
        btnH1=Clases_Bracket_Nuevo.BotonesGrupos("H",1,frmGruposIzq,text="")
        btnH1.grid(row=f,column=c)

        f+=1
        btnH2=Clases_Bracket_Nuevo.BotonesGrupos("H",2,frmGruposIzq,text="")
        btnH2.grid(row=f,column=c)

        f+=1
        btnH3=Clases_Bracket_Nuevo.BotonesGrupos("H",3,frmGruposIzq,text="")
        btnH3.grid(row=f,column=c)

        f+=1
        btnH4=Clases_Bracket_Nuevo.BotonesGrupos("H",4,frmGruposIzq,text="")
        btnH4.grid(row=f,column=c)

        ########################################################
        ########################################################
        ########################################################
        #---------------------------Octavos A y B
        f=0
        c=1
        lblOctavos=Label(frmGruposIzq,text="Octavos de Final")
        lblOctavos.grid(row=f,column=c,pady=10)

        f+=2
        btnOctA1=Button(frmGruposIzq,text="OctA1")
        btnOctA1.grid(row=f,column=c)

        f+=1
        btnOctB2=Button(frmGruposIzq,text="OctB2")
        btnOctB2.grid(row=f,column=c)

        f+=4
        btnOctB1=Button(frmGruposIzq,text="OctB1")
        btnOctB1.grid(row=f,column=c)

        f+=1
        btnOctA2=Button(frmGruposIzq,text="OctA2")
        btnOctA2.grid(row=f,column=c)
        #---------------------------Octavos C y D
        f=12
        c=1

        btnOctC1=Button(frmGruposIzq,text="OctC1")
        btnOctC1.grid(row=f,column=c)

        f+=1
        btnOctD2=Button(frmGruposIzq,text="OctD2")
        btnOctD2.grid(row=f,column=c)

        f+=4
        btnOctD1=Button(frmGruposIzq,text="OctD1")
        btnOctD1.grid(row=f,column=c)

        f+=1
        btnOctC2=Button(frmGruposIzq,text="OctC2")
        btnOctC2.grid(row=f,column=c)
        ##################################################Derecha
        #---------------------------Octavos E y F
        f=0
        c=9
        lblOctavos=Label(frmGruposIzq,text="Octavos de Final")
        lblOctavos.grid(row=f,column=c,pady=10)

        f+=2
        btnOctE1=Button(frmGruposIzq,text="OctE1")
        btnOctE1.grid(row=f,column=c)

        f+=1
        btnOctF2=Button(frmGruposIzq,text="OctF2")
        btnOctF2.grid(row=f,column=c)

        f+=4
        btnOctF1=Button(frmGruposIzq,text="OctF1")
        btnOctF1.grid(row=f,column=c)

        f+=1
        btnOctE2=Button(frmGruposIzq,text="OctE2")
        btnOctE2.grid(row=f,column=c)

        #---------------------------Octavos G y H
        f=12
        c=9

        btnOctG1=Button(frmGruposIzq,text="OctG1")
        btnOctG1.grid(row=f,column=c)

        f+=1
        btnOctH2=Button(frmGruposIzq,text="OctH2")
        btnOctH2.grid(row=f,column=c)

        f+=4
        btnOctH1=Button(frmGruposIzq,text="OctH1")
        btnOctH1.grid(row=f,column=c)

        f+=1
        btnOctG2=Button(frmGruposIzq,text="OctG2")
        btnOctG2.grid(row=f,column=c)


        ########################
        #########################Configuraciones de Botones Grupos

        btnA1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoA(btnOctA1,
                                              btnOctA2,
                                              btnA1.cget("text")))

        btnA2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoA(btnOctA1,
                                              btnOctA2,
                                              btnA2.cget("text")))

        btnA3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoA(btnOctA1,
                                              btnOctA2,
                                              btnA3.cget("text")))

        btnA4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoA(btnOctA1,
                                              btnOctA2,
                                              btnA4.cget("text")))
        ############################################grupoB#############
        btnB1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoB(btnOctB1,
                                              btnOctB2,
                                              btnB1.cget("text")))

        btnB2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoB(btnOctB1,
                                              btnOctB2,
                                              btnB2.cget("text")))

        btnB3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoB(btnOctB1,
                                              btnOctB2,
                                              btnB3.cget("text")))

        btnB4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoB(btnOctB1,
                                              btnOctB2,
                                              btnB4.cget("text")))

        ############################################grupoC#############

        btnC1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoC(btnOctC1,
                                              btnOctC2,
                                              btnC1.cget("text")))

        btnC2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoC(btnOctC1,
                                              btnOctC2,
                                              btnC2.cget("text")))

        btnC3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoC(btnOctC1,
                                              btnOctC2,
                                              btnC3.cget("text")))

        btnC4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoC(btnOctC1,
                                              btnOctC2,
                                              btnC4.cget("text")))

        ############################################grupoD#############

        btnD1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoD(btnOctD1,
                                              btnOctD2,
                                              btnD1.cget("text")))

        btnD2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoD(btnOctD1,
                                              btnOctD2,
                                              btnD2.cget("text")))

        btnD3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoD(btnOctD1,
                                              btnOctD2,
                                              btnD3.cget("text")))

        btnD4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoD(btnOctD1,
                                              btnOctD2,
                                              btnD4.cget("text")))

        ############################################grupoE#############

        btnE1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoE(btnOctE1,
                                              btnOctE2,
                                              btnE1.cget("text")))

        btnE2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoE(btnOctE1,
                                              btnOctE2,
                                              btnE2.cget("text")))

        btnE3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoE(btnOctE1,
                                              btnOctE2,
                                              btnE3.cget("text")))

        btnE4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoE(btnOctE1,
                                              btnOctE2,
                                              btnE4.cget("text")))

        ############################################grupoF#############

        btnF1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoF(btnOctF1,
                                              btnOctF2,
                                              btnF1.cget("text")))

        btnF2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoF(btnOctF1,
                                              btnOctF2,
                                              btnF2.cget("text")))

        btnF3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoF(btnOctF1,
                                              btnOctF2,
                                              btnF3.cget("text")))

        btnF4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoF(btnOctF1,
                                              btnOctF2,
                                              btnF4.cget("text")))

        ############################################grupoG#############

        btnG1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoG(btnOctG1,
                                              btnOctG2,
                                              btnG1.cget("text")))

        btnG2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoG(btnOctG1,
                                              btnOctG2,
                                              btnG2.cget("text")))

        btnG3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoG(btnOctG1,
                                              btnOctG2,
                                              btnG3.cget("text")))

        btnG4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoG(btnOctG1,
                                              btnOctG2,
                                              btnG4.cget("text")))

        ############################################grupoH#############

        btnH1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoH(btnOctH1,
                                              btnOctH2,
                                              btnH1.cget("text")))

        btnH2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoH(btnOctH1,
                                              btnOctH2,
                                              btnH2.cget("text")))

        btnH3.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoH(btnOctH1,
                                              btnOctH2,
                                              btnH3.cget("text")))

        btnH4.configure(command=lambda:Clases_Bracket_Nuevo.AccionesOctavos.AccionGrupoH(btnOctH1,
                                              btnOctH2,
                                              btnH4.cget("text")))

        ########################################################
        ########################################################
        ########################################################
        #---------------------------Cuartos A y B
        f=0
        c=2
        lblCuartos=Label(frmGruposIzq,text="Cuartos de Final")
        lblCuartos.grid(row=f,column=c,pady=10)

        f+=2
        btnCuartosA1=Button(frmGruposIzq,text="CuartosA1")
        btnCuartosA1.grid(row=f,column=c,rowspan=2)



        f+=5
        btnCuartosB1=Button(frmGruposIzq,text="CuartosB1")
        btnCuartosB1.grid(row=f,column=c,rowspan=2)


        #---------------------------Cuartos C y D
        f=12
        c=2

        btnCuartosC1=Button(frmGruposIzq,text="CuartosC1")
        btnCuartosC1.grid(row=f,column=c,rowspan=2)



        f+=5
        btnCuartosD1=Button(frmGruposIzq,text="CuartosD1")
        btnCuartosD1.grid(row=f,column=c,rowspan=2)
        #############################################################Derecha
        #---------------------------Cuartos E y F
        f=0
        c=8
        lblCuartos=Label(frmGruposIzq,text="Cuartos de Final")
        lblCuartos.grid(row=f,column=c,pady=10)

        f+=2
        btnCuartosE1=Button(frmGruposIzq,text="CuartosE1")
        btnCuartosE1.grid(row=f,column=c,rowspan=2)



        f+=5
        btnCuartosF1=Button(frmGruposIzq,text="CuartosF1")
        btnCuartosF1.grid(row=f,column=c,rowspan=2)


        #---------------------------Cuartos G y H
        f=12
        c=8

        btnCuartosG1=Button(frmGruposIzq,text="CuartosG1")
        btnCuartosG1.grid(row=f,column=c,rowspan=2)



        f+=5
        btnCuartosH1=Button(frmGruposIzq,text="CuartosH1")
        btnCuartosH1.grid(row=f,column=c,rowspan=2)

        ########################
        #########################Configuraciones de Botones Octavos

        btnOctA1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctAyB1(btnCuartosA1,
                                              btnOctA1.cget("text")))

        btnOctB2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctAyB1(btnCuartosA1,
                                              btnOctB2.cget("text")))


        btnOctB1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctAyB2(btnCuartosB1,
                                              btnOctB1.cget("text")))

        btnOctA2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctAyB2(btnCuartosB1,
                                              btnOctA2.cget("text")))
        #############################BotonesC y D

        btnOctC1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctCyD1(btnCuartosC1,
                                              btnOctC1.cget("text")))

        btnOctD2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctCyD1(btnCuartosC1,
                                              btnOctD2.cget("text")))


        btnOctD1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctCyD2(btnCuartosD1,
                                              btnOctD1.cget("text")))

        btnOctC2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctCyD2(btnCuartosD1,
                                              btnOctC2.cget("text")))

        #############################Botones E y F

        btnOctE1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctEyF1(btnCuartosE1,
                                              btnOctE1.cget("text")))

        btnOctF2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctEyF1(btnCuartosE1,
                                              btnOctF2.cget("text")))


        btnOctF1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctEyF2(btnCuartosF1,
                                              btnOctF1.cget("text")))

        btnOctE2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctEyF2(btnCuartosF1,
                                              btnOctE2.cget("text")))

        #############################Botones G y H

        btnOctG1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctGyH1(btnCuartosG1,
                                              btnOctG1.cget("text")))

        btnOctH2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctGyH1(btnCuartosG1,
                                              btnOctH2.cget("text")))


        btnOctH1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctGyH2(btnCuartosH1,
                                              btnOctH1.cget("text")))

        btnOctG2.configure(command=lambda:Clases_Bracket_Nuevo.AccionesCuartos.AccionOctGyH2(btnCuartosH1,
                                              btnOctG2.cget("text")))

        ##################################################################
        ##################################################################
        ##################################################################
        ##################################################################
        #---------------------------Semifinal A y B
        f=0
        c=3
        lblCuartos=Label(frmGruposIzq,text="Semifinales")
        lblCuartos.grid(row=f,column=c,pady=10)

        f+=5
        btnSemifinalA1=Button(frmGruposIzq,text="SemifinalA1")
        btnSemifinalA1.grid(row=f,column=c,rowspan=1)



        f+=10
        btnSemifinalB1=Button(frmGruposIzq,text="SemifinalB1")
        btnSemifinalB1.grid(row=f,column=c,rowspan=1)


        #############################################################Derecha
        #---------------------------Semifinal C y D
        f=0
        c=7
        lblCuartos=Label(frmGruposIzq,text="Semifinales")
        lblCuartos.grid(row=f,column=c,pady=10)

        f+=5
        btnSemifinalC1=Button(frmGruposIzq,text="SemifinalC1")
        btnSemifinalC1.grid(row=f,column=c,rowspan=1)



        f+=10
        btnSemifinalD1=Button(frmGruposIzq,text="SemifinalD1")
        btnSemifinalD1.grid(row=f,column=c,rowspan=1)







        ########################
        #########################Configuraciones de Botones Cuartos

        btnCuartosA1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosAyB1(btnSemifinalA1,
                                              btnCuartosA1.cget("text")))




        btnCuartosB1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosAyB1(btnSemifinalA1,
                                              btnCuartosB1.cget("text")))


        #############################BotonesC y D

        btnCuartosC1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosCyD1(btnSemifinalB1,
                                              btnCuartosC1.cget("text")))




        btnCuartosD1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosCyD1(btnSemifinalB1,
                                              btnCuartosD1.cget("text")))



        #############################Botones E y F

        btnCuartosE1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosEyF1(btnSemifinalC1,
                                              btnCuartosE1.cget("text")))




        btnCuartosF1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosEyF1(btnSemifinalC1,
                                              btnCuartosF1.cget("text")))



        #############################Botones G y H

        btnCuartosG1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosGyH1(btnSemifinalD1,
                                              btnCuartosG1.cget("text")))




        btnCuartosH1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesSemifinal.AccionCuartosGyH1(btnSemifinalD1,
                                              btnCuartosH1.cget("text")))


        ##################################################################
        ##################################################################
        ##################################################################
        ##################################################################
        #---------------------------Final A 
        f=0
        c=4
        lblCuartos=Label(frmGruposIzq,text="Final")
        lblCuartos.grid(row=f,column=c,pady=10)

        f+=10
        btnFinalA1=Button(frmGruposIzq,text="FinalA1")
        btnFinalA1.grid(row=f,column=c,rowspan=1)






        #############################################################Derecha
        #---------------------------Final B
        f=0
        c=6
        lblCuartos=Label(frmGruposIzq,text="Final")
        lblCuartos.grid(row=f,column=c,pady=10)

        f+=10
        btnFinalB1=Button(frmGruposIzq,text="FinalB1")
        btnFinalB1.grid(row=f,column=c,rowspan=1)


        ########################
        #########################Configuraciones de Botones Semifinal

        btnSemifinalA1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesFinal.AccionSemifinalAyB1(btnFinalA1,
                                              btnSemifinalA1.cget("text")))



        btnSemifinalB1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesFinal.AccionSemifinalAyB1(btnFinalA1,
                                              btnSemifinalB1.cget("text")))



        btnSemifinalC1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesFinal.AccionSemifinalCyD1(btnFinalB1,
                                              btnSemifinalC1.cget("text")))



        btnSemifinalD1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesFinal.AccionSemifinalCyD1(btnFinalB1,
                                              btnSemifinalD1.cget("text")))


        ##################################################################
        ##################################################################
        ##################################################################
        ##################################################################
        #---------------------------Final A 
        f=0
        c=5
        lblCuartos=Label(frmGruposIzq,text="Ganador")
        lblCuartos.grid(row=f,column=c,pady=10,padx=60)

        f+=10
        btnGanador=Button(frmGruposIzq,text="--Ganador--")
        btnGanador.grid(row=f,column=c,rowspan=1)



        ########################
        #########################Configuraciones de Botones Final

        btnFinalA1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesGanador.AccionFinalAyB1(btnGanador,
                                              btnFinalA1.cget("text")))



        btnFinalB1.configure(command=lambda:Clases_Bracket_Nuevo.AccionesGanador.AccionFinalAyB1(btnGanador,
                                              btnFinalB1.cget("text")))


        btnGanador.configure(command=lambda:Clases_Bracket_Nuevo.Confirmar.VerificarBracket(btnOctA1.cget("text"),
                                                                               btnOctB2.cget("text"),
                                                                               btnOctB1.cget("text"),
                                                                               btnOctA2.cget("text"),
        ##########################################################################                                                                    
                                                                               btnOctC1.cget("text"),
                                                                               btnOctD2.cget("text"),
                                                                               btnOctD1.cget("text"),
                                                                               btnOctC2.cget("text"),
        ##########################################################################
                                                                               btnOctE1.cget("text"),
                                                                               btnOctF2.cget("text"),
                                                                               btnOctF1.cget("text"),
                                                                               btnOctE2.cget("text"),
        ##########################################################################
                                                                               btnOctG1.cget("text"),
                                                                               btnOctH2.cget("text"),
                                                                               btnOctH1.cget("text"),
                                                                               btnOctG2.cget("text"),
        ##########################################################################----------------------------------
                                                                               btnCuartosA1.cget("text"),
                                                                               btnCuartosB1.cget("text"),
        ##########################################################################
                                                                               btnCuartosC1.cget("text"),
                                                                               btnCuartosD1.cget("text"),
        ##########################################################################
                                                                               btnCuartosE1.cget("text"),
                                                                               btnCuartosF1.cget("text"),
        ##########################################################################
                                                                               btnCuartosG1.cget("text"),
                                                                               btnCuartosH1.cget("text"),
        ##########################################################################----------------------------------
                                                                               btnSemifinalA1.cget("text"),
                                                                               btnSemifinalB1.cget("text"),
        ##########################################################################
                                                                               btnSemifinalC1.cget("text"),
                                                                               btnSemifinalD1.cget("text"),
        ##########################################################################----------------------------------
                                                                               btnFinalA1.cget("text"),
                                                                               btnFinalB1.cget("text"),
        ##########################################################################----------------------------------
                                                                               btnGanador.cget("text"),
        ##########################################################################----------------------------------                                                                       
                                                                               v,
        ##########################################################################----------------------------------             
                                                                               id_bracket
                                                                               ))

        #-----------------------Cerrar con equis
        def cerrar_con_equis():
            messagebox.showinfo("BM","Debe de guardar su bracket primero")
        
        v.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

        
        v.mainloop()
