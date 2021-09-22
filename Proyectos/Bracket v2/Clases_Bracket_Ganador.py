from tkinter import *
from tkinter import messagebox

class BotonesGrupos(Button):
    
    def __init__(self,grupo,indice,parent,**kw):
        Button.__init__(self,parent,kw)
        template=open("Template.txt","r")
        lista_archivo=template.readlines()
        if grupo=="A":
            
            nombre=lista_archivo[0].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="B":
            
            nombre=lista_archivo[1].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="C":
            
            nombre=lista_archivo[2].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="D":
            
            nombre=lista_archivo[3].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="E":
            
            nombre=lista_archivo[4].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="F":
            
            nombre=lista_archivo[5].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="G":
            
            nombre=lista_archivo[6].split(",")[indice]
            self.configure(text=nombre)
        if grupo=="H":
            
            nombre=lista_archivo[7].split(",")[indice]
            self.configure(text=nombre)
##############################################################################################
##############################################################################################        
##############################################################################################
class AccionesOctavos():
    
    def AccionGrupoA(OctA1,OctA2,seleccionado):
        
        if OctA1.cget("text")!=seleccionado and OctA1.cget("text") == "OctA1" and OctA2.cget("text") != seleccionado:
            OctA1.configure(text=seleccionado)
            
        elif OctA2.cget("text")!=seleccionado and OctA2.cget("text") == "OctA2"and OctA1.cget("text") != seleccionado:
            OctA2.configure(text=seleccionado)
            
        elif OctA2.cget("text")==seleccionado:
            OctA2.configure(text="OctA2")
            
        elif OctA1.cget("text")==seleccionado:
            OctA1.configure(text="OctA1")
            
        elif OctA1.cget("text") != "OctA1" and OctA2.cget("text") != "OctA2":
            messagebox.showinfo("BM","Ganadores del Grupo A estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")
            

        
        
    def AccionGrupoB(OctB1,OctB2,seleccionado):
        if OctB1.cget("text")!=seleccionado and OctB1.cget("text") == "OctB1" and OctB2.cget("text") != seleccionado:
            OctB1.configure(text=seleccionado)
            
        elif OctB2.cget("text")!=seleccionado and OctB2.cget("text") == "OctB2"and OctB1.cget("text") != seleccionado:
            OctB2.configure(text=seleccionado)
        elif OctB2.cget("text")==seleccionado:
            OctB2.configure(text="OctB2")
        elif OctB1.cget("text")==seleccionado:
            OctB1.configure(text="OctB1")
        elif OctB1.cget("text") != "OctB1" and OctB2.cget("text") != "OctB2":
            messagebox.showinfo("BM","Ganadores del Grupo B estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionGrupoC(OctC1,OctC2,seleccionado):
        if OctC1.cget("text")!=seleccionado and OctC1.cget("text") == "OctC1" and OctC2.cget("text") != seleccionado:
            OctC1.configure(text=seleccionado)
            
        elif OctC2.cget("text")!=seleccionado and OctC2.cget("text") == "OctC2"and OctC1.cget("text") != seleccionado:
            OctC2.configure(text=seleccionado)
        elif OctC2.cget("text")==seleccionado:
            OctC2.configure(text="OctC2")
        elif OctC1.cget("text")==seleccionado:
            OctC1.configure(text="OctC1")
        elif OctC1.cget("text") != "OctC1" and OctC2.cget("text") != "OctC2":
            messagebox.showinfo("BM","Ganadores del Grupo C estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")
    
    def AccionGrupoD(OctD1,OctD2,seleccionado):
        if OctD1.cget("text")!=seleccionado and OctD1.cget("text") == "OctD1" and OctD2.cget("text") != seleccionado:
            OctD1.configure(text=seleccionado)
            
        elif OctD2.cget("text")!=seleccionado and OctD2.cget("text") == "OctD2"and OctD1.cget("text") != seleccionado:
            OctD2.configure(text=seleccionado)
        elif OctD2.cget("text")==seleccionado:
            OctD2.configure(text="OctD2")
        elif OctD1.cget("text")==seleccionado:
            OctD1.configure(text="OctD1")
        elif OctD1.cget("text") != "OctD1" and OctD2.cget("text") != "OctD2":
            messagebox.showinfo("BM","Ganadores del Grupo D estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionGrupoE(OctE1,OctE2,seleccionado):
        if OctE1.cget("text")!=seleccionado and OctE1.cget("text") == "OctE1" and OctE2.cget("text") != seleccionado:
            OctE1.configure(text=seleccionado)
            
        elif OctE2.cget("text")!=seleccionado and OctE2.cget("text") == "OctE2"and OctE1.cget("text") != seleccionado:
            OctE2.configure(text=seleccionado)
        elif OctE2.cget("text")==seleccionado:
            OctE2.configure(text="OctE2")
        elif OctE1.cget("text")==seleccionado:
            OctE1.configure(text="OctE1")
        elif OctE1.cget("text") != "OctE1" and OctE2.cget("text") != "OctE2":
            messagebox.showinfo("BM","Ganadores del Grupo E estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionGrupoF(OctF1,OctF2,seleccionado):
        if OctF1.cget("text")!=seleccionado and OctF1.cget("text") == "OctF1" and OctF2.cget("text") != seleccionado:
            OctF1.configure(text=seleccionado)
            
        elif OctF2.cget("text")!=seleccionado and OctF2.cget("text") == "OctF2"and OctF1.cget("text") != seleccionado:
            OctF2.configure(text=seleccionado)
        elif OctF2.cget("text")==seleccionado:
            OctF2.configure(text="OctF2")
        elif OctF1.cget("text")==seleccionado:
            OctF1.configure(text="OctF1")
        elif OctF1.cget("text") != "OctF1" and OctF2.cget("text") != "OctF2":
            messagebox.showinfo("BM","Ganadores del Grupo F estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionGrupoG(OctG1,OctG2,seleccionado):
        if OctG1.cget("text")!=seleccionado and OctG1.cget("text") == "OctG1" and OctG2.cget("text") != seleccionado:
            OctG1.configure(text=seleccionado)
            
        elif OctG2.cget("text")!=seleccionado and OctG2.cget("text") == "OctG2"and OctG1.cget("text") != seleccionado:
            OctG2.configure(text=seleccionado)
        elif OctG2.cget("text")==seleccionado:
            OctG2.configure(text="OctG2")
        elif OctG1.cget("text")==seleccionado:
            OctG1.configure(text="OctG1")
        elif OctG1.cget("text") != "OctG1" and OctG2.cget("text") != "OctG2":
            messagebox.showinfo("BM","Ganadores del Grupo G estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionGrupoH(OctH1,OctH2,seleccionado):
        if OctH1.cget("text")!=seleccionado and OctH1.cget("text") == "OctH1" and OctH2.cget("text") != seleccionado:
            OctH1.configure(text=seleccionado)
            
        elif OctH2.cget("text")!=seleccionado and OctH2.cget("text") == "OctH2"and OctH1.cget("text") != seleccionado:
            OctH2.configure(text=seleccionado)
        elif OctH2.cget("text")==seleccionado:
            OctH2.configure(text="OctH2")
        elif OctH1.cget("text")==seleccionado:
            OctH1.configure(text="OctH1")
        elif OctH1.cget("text") != "OctH1" and OctH2.cget("text") != "OctH2":
            messagebox.showinfo("BM","Ganadores del Grupo H estan completos\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")
##################################################################
##################################################################
##################################################################
class AccionesCuartos():

    def AccionOctAyB1(CuartosA1,seleccionado):
        if seleccionado=="OctA1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctA1")
        elif seleccionado=="OctB2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctB2")
        elif CuartosA1.cget("text")!=seleccionado and CuartosA1.cget("text") == "CuartosA1":
            CuartosA1.configure(text=seleccionado)
        elif CuartosA1.cget("text")==seleccionado:
            CuartosA1.configure(text="CuartosA1")
        elif CuartosA1.cget("text") != "CuartosA1":
            messagebox.showinfo("BM","Ganadores de Cuartos A1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionOctAyB2(CuartosB1,seleccionado):
        if seleccionado=="OctB1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctB1")
        elif seleccionado=="OctA2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctA2")
        elif CuartosB1.cget("text")!=seleccionado and CuartosB1.cget("text") == "CuartosB1":
            CuartosB1.configure(text=seleccionado)
        elif CuartosB1.cget("text")==seleccionado:
            CuartosB1.configure(text="CuartosB1")
        elif CuartosB1.cget("text") != "CuartosB1":
            messagebox.showinfo("BM","Ganadores de Cuartos B1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")
##############-----------------------------------

    def AccionOctCyD1(CuartosC1,seleccionado):
        if seleccionado=="OctC1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctC1")
        elif seleccionado=="OctD2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctD2")
        elif CuartosC1.cget("text")!=seleccionado and CuartosC1.cget("text") == "CuartosC1":
            CuartosC1.configure(text=seleccionado)
        elif CuartosC1.cget("text")==seleccionado:
            CuartosC1.configure(text="CuartosC1")
        elif CuartosC1.cget("text") != "CuartosC1":
            messagebox.showinfo("BM","Ganadores de Cuartos C1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionOctCyD2(CuartosD1,seleccionado):
        if seleccionado=="OctD1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctD1")
        elif seleccionado=="OctC2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctC2")
        elif CuartosD1.cget("text")!=seleccionado and CuartosD1.cget("text") == "CuartosD1":
            CuartosD1.configure(text=seleccionado)
        elif CuartosD1.cget("text")==seleccionado:
            CuartosD1.configure(text="CuartosD1")
        elif CuartosD1.cget("text") != "CuartosD1":
            messagebox.showinfo("BM","Ganadores de Cuartos D1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

##############-----------------------------------
    def AccionOctEyF1(CuartosE1,seleccionado):
        if seleccionado=="OctE1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctE1")
        elif seleccionado=="OctF2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctF2")
        elif CuartosE1.cget("text")!=seleccionado and CuartosE1.cget("text") == "CuartosE1":
            CuartosE1.configure(text=seleccionado)
        elif CuartosE1.cget("text")==seleccionado:
            CuartosE1.configure(text="CuartosE1")
        elif CuartosE1.cget("text") != "CuartosE1":
            messagebox.showinfo("BM","Ganadores de Cuartos E1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionOctEyF2(CuartosF1,seleccionado):
        if seleccionado=="OctF1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctF1")
        elif seleccionado=="OctE2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctE2")
        elif CuartosF1.cget("text")!=seleccionado and CuartosF1.cget("text") == "CuartosF1":
            CuartosF1.configure(text=seleccionado)
        elif CuartosF1.cget("text")==seleccionado:
            CuartosF1.configure(text="CuartosF1")
        elif CuartosF1.cget("text") != "CuartosF1":
            messagebox.showinfo("BM","Ganadores de Cuartos F1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

##############-----------------------------------
    def AccionOctGyH1(CuartosG1,seleccionado):
        if seleccionado=="OctG1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctG1")
        elif seleccionado=="OctH2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctH2")
        elif CuartosG1.cget("text")!=seleccionado and CuartosG1.cget("text") == "CuartosG1":
            CuartosG1.configure(text=seleccionado)
        elif CuartosG1.cget("text")==seleccionado:
            CuartosG1.configure(text="CuartosG1")
        elif CuartosG1.cget("text") != "CuartosG1":
            messagebox.showinfo("BM","Ganadores de Cuartos G1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionOctGyH2(CuartosH1,seleccionado):
        if seleccionado=="OctH1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctH1")
        elif seleccionado=="OctG2":
            messagebox.showinfo("BM","Primero Ingrese el ganador de Octavos OctG2")
        elif CuartosH1.cget("text")!=seleccionado and CuartosH1.cget("text") == "CuartosH1":
            CuartosH1.configure(text=seleccionado)
        elif CuartosH1.cget("text")==seleccionado:
            CuartosH1.configure(text="CuartosH1")
        elif CuartosH1.cget("text") != "CuartosH1":
            messagebox.showinfo("BM","Ganadores de Cuartos H1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")
############
############
############
############    
############
            
class AccionesSemifinal():

    def AccionCuartosAyB1(SemifinalA1,seleccionado):
        if seleccionado=="CuartosA1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosA1")
        elif seleccionado=="CuartosB1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosB1")
        elif SemifinalA1.cget("text")!=seleccionado and SemifinalA1.cget("text") == "SemifinalA1":
            SemifinalA1.configure(text=seleccionado)
        elif SemifinalA1.cget("text")==seleccionado:
            SemifinalA1.configure(text="SemifinalA1")
        elif SemifinalA1.cget("text") != "SemifinalA1":
            messagebox.showinfo("BM","Ganadores de Semifinal A1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")


    def AccionCuartosCyD1(SemifinalB1,seleccionado):
        if seleccionado=="CuartosC1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosC1")
        elif seleccionado=="CuartosD1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosD1")
        elif SemifinalB1.cget("text")!=seleccionado and SemifinalB1.cget("text") == "SemifinalB1":
            SemifinalB1.configure(text=seleccionado)
        elif SemifinalB1.cget("text")==seleccionado:
            SemifinalB1.configure(text="SemifinalB1")
        elif SemifinalB1.cget("text") != "SemifinalB1":
            messagebox.showinfo("BM","Ganadores de Semifinal B1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

            
    def AccionCuartosEyF1(SemifinalC1,seleccionado):
        if seleccionado=="CuartosE1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosE1")
        elif seleccionado=="CuartosF1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosF1")
        elif SemifinalC1.cget("text")!=seleccionado and SemifinalC1.cget("text") == "SemifinalC1":
            SemifinalC1.configure(text=seleccionado)
        elif SemifinalC1.cget("text")==seleccionado:
            SemifinalC1.configure(text="SemifinalC1")
        elif SemifinalC1.cget("text") != "SemifinalC1":
            messagebox.showinfo("BM","Ganadores de Semifinal B1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionCuartosGyH1(SemifinalD1,seleccionado):
        if seleccionado=="CuartosG1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosG1")
        elif seleccionado=="CuartosH1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de CuartosH1")
        elif SemifinalD1.cget("text")!=seleccionado and SemifinalD1.cget("text") == "SemifinalD1":
            SemifinalD1.configure(text=seleccionado)
        elif SemifinalD1.cget("text")==seleccionado:
            SemifinalD1.configure(text="SemifinalD1")
        elif SemifinalD1.cget("text") != "SemifinalD1":
            messagebox.showinfo("BM","Ganadores de Semifinal B1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

############
############
############
############    
############
            
class AccionesFinal():

    def AccionSemifinalAyB1(FinalA1,seleccionado):
        if seleccionado=="SemifinalA1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de SemifinalA1")
        elif seleccionado=="SemifinalB1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de SemifinalB1")
        elif FinalA1.cget("text")!=seleccionado and FinalA1.cget("text") == "FinalA1":
            FinalA1.configure(text=seleccionado)
        elif FinalA1.cget("text")==seleccionado:
            FinalA1.configure(text="FinalA1")
        elif FinalA1.cget("text") != "FinalA1":
            messagebox.showinfo("BM","Ganadores de Final A1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

    def AccionSemifinalCyD1(FinalB1,seleccionado):
        if seleccionado=="SemifinalC1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de SemifinalC1")
        elif seleccionado=="SemifinalD1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de SemifinalD1")
        elif FinalB1.cget("text")!=seleccionado and FinalB1.cget("text") == "FinalB1":
            FinalB1.configure(text=seleccionado)
        elif FinalB1.cget("text")==seleccionado:
            FinalB1.configure(text="FinalB1")
        elif FinalB1.cget("text") != "FinalB1":
            messagebox.showinfo("BM","Ganadores de Final B1 está completo\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")

class AccionesGanador():
    def AccionFinalAyB1(Ganador,seleccionado):
        if seleccionado=="FinalA1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de FinalA1")
        elif seleccionado=="FinalB1":
            messagebox.showinfo("BM","Primero Ingrese el ganador de FinalB1")
        elif Ganador.cget("text")!=seleccionado and Ganador.cget("text") == "--Ganador--":
            Ganador.configure(text=seleccionado)
        elif Ganador.cget("text")==seleccionado:
            Ganador.configure(text="--Ganador--")
        elif Ganador.cget("text") != "--Ganador--":
            messagebox.showinfo("BM","Ganador ya se definió\nNOTA: Seleccione el nombre del equipo que quiere cambiar\npara cambiar su elección")


            
class Confirmar():
    
    def VerificarBracket(OctA1,OctB2,OctB1,OctA2, OctC1,OctD2,OctD1,OctC2, OctE1,OctF2,OctF1,OctE2, OctG1,OctH2,OctH1,OctG2,
                         CuartosA1,CuartosB1,CuartosC1,CuartosD1,CuartosE1,CuartosF1,CuartosG1,CuartosH1,
                         SemifinalA1,SemifinalB1,SemifinalC1,SemifinalD1,
                         FinalA1,FinalB1,
                         Ganador,
                         v_main,
                         ventana
                         ):


        
        botones=('OctA1','OctB2','OctB1','OctA2','OctC1','OctD2','OctD1','OctC2','OctE1','OctF2','OctF1','OctE2', 'OctG1','OctH2','OctH1','OctG2',
                 'CuartosA1','CuartosB1','CuartosC1','CuartosD1','CuartosE1','CuartosF1','CuartosG1','CuartosH1',
                 'SemifinalA1','SemifinalB1','SemifinalC1','SemifinalD1',
                 'FinalA1','FinalB1',
                 '--Ganador--'
                 )
        
        d={}
        
        d["Octavos"]=OctA1,OctB2,OctB1,OctA2, OctC1,OctD2,OctD1,OctC2, OctE1,OctF2,OctF1,OctE2, OctG1,OctH2,OctH1,OctG2
        d["Cuartos"]=CuartosA1,CuartosB1,CuartosC1,CuartosD1,CuartosE1,CuartosF1,CuartosG1,CuartosH1
        d["Semifinal"]=SemifinalA1,SemifinalB1,SemifinalC1,SemifinalD1
        d["Final"]=FinalA1,FinalB1
        d["Ganador"]=Ganador
        
        #--------------------------------------
        mensaje=""
        bandera=True
        for i in range(len(botones)):
            if botones[i] in d["Octavos"] or botones[i] in d["Cuartos"] or botones[i] in d["Semifinal"] or botones[i] in d["Semifinal"] or botones[i] in d["Final"] or botones[i] in d["Ganador"]:
                mensaje+="Hace falta: "+str(botones[i])+"\n"
                bandera=False

        #--------------------------------------     
        if bandera==False:
            
            messagebox.showinfo("BM",mensaje)#False es que esta duplicado
        else:
            
            file = open("Bracket_Ganador.txt", 'w')
            
            #-----Octavos-----
            
            lista=[]
            for i in range( len(d["Octavos"]) ):
                lista.append(d["Octavos"][i])
            print(lista)
            
            file.write("Octavos")
            file.write(",")
            for i in range( len(lista) ):
                file.write(lista[i])
                file.write(",")

            file.write("\n")

            #-----Cuartos-----
            
            lista=[]
            for i in range( len(d["Cuartos"]) ):
                lista.append(d["Cuartos"][i])
            print(lista)
            
            file.write("Cuartos")
            file.write(",")
            for i in range( len(lista) ):
                file.write(lista[i])
                file.write(",")

            file.write("\n")

            #-----Semifinal-----
            
            lista=[]
            for i in range( len(d["Semifinal"]) ):
                lista.append(d["Semifinal"][i])
            print(lista)
            
            file.write("Semifinal")
            file.write(",")
            for i in range( len(lista) ):
                file.write(lista[i])
                file.write(",")

            file.write("\n")

            #-----Final-----
            
            lista=[]
            for i in range( len(d["Final"]) ):
                lista.append(d["Final"][i])
            print(lista)
            
            file.write("Final")
            file.write(",")
            for i in range( len(lista) ):
                file.write(lista[i])
                file.write(",")

            file.write("\n")

            #-----Ganador-----
            
            
            file.write("Ganador")
            file.write(",")
            
            file.write(d["Ganador"])
            file.write(",")

            file.write("\n")

            #-----Cerrar Documento-----

            file.close()

            messagebox.showinfo("BM","Bracket Guardado")
            #-----Cerrar Ventana-----
            ventana.destroy()
            v_main.update()
            v_main.deiconify()
        
