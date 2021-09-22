from tkinter import *

class Boton_Grupos(Button):
    Grupo_Seleccionado=None
    Entrada=None
    lst_Otro1=None
    lst_Otro2=None
    lst_Otro3=None
    lst_Otro4=None
    lst_Otro5=None
    lst_Otro6=None
    lst_Otro7=None
    
    def __init__(self,lista_grupo,entrada,otra1,otra2,otra3,otra4,otra5,otra6,otra7,parent,**kw):

        Button.__init__(self,parent,kw)
        self.Grupo_Seleccionado=lista_grupo
        self.Entrada=entrada
        self.lst_Otro0=lista_grupo
        self.lst_Otro1=otra1
        self.lst_Otro2=otra2
        self.lst_Otro3=otra3
        self.lst_Otro4=otra4
        self.lst_Otro5=otra5
        self.lst_Otro6=otra6
        self.lst_Otro7=otra7

    #-----AgregarEquipo-----
    def AgregarEquipo(self):
        
        if self.VerDuplicados() == True:
            messagebox.showwarning("Bracket Mundial","Equipo Duplicado\nIngrese otro nombre diferente")
            self.Entrada.set("")
            
        else:
            
            lista_seleccionada = list(self.Grupo_Seleccionado.get(0,END))
            if self.Entrada.get() != "":
                if len(lista_seleccionada) <= 3:
                    self.Grupo_Seleccionado.insert( END , self.Entrada.get() )
                    self.Entrada.set("")
                else:
                    messagebox.showwarning("Bracket Mundial","El grupo esta lleno.\nSi no le complace el orden del grupo puede presionar en el boton limpiar")
                    print("El grupo esta lleno")
                    self.Entrada.set("")
            else:
                messagebox.showinfo("Bracket Mundial","Debe ingresar al menos un carácter que lo identifique")

    #-----ValidarLista-----
    def ValidarLista(self,lista):
        if len(lista) != 0:
            for i in range( len(lista) ):
                if self.Entrada.get() == lista[i]:
                    return(True)
                    
        if len(lista) == 0:
            return(False)
    #------------------------------
    def VerDuplicados(self):
        bandera=False
        listaOtro0=list( self.lst_Otro0.get(0,END) )
        listaOtro1=list( self.lst_Otro1.get(0,END) )
        listaOtro2=list( self.lst_Otro2.get(0,END) )
        listaOtro3=list( self.lst_Otro3.get(0,END) )
        listaOtro4=list( self.lst_Otro4.get(0,END) )
        listaOtro5=list( self.lst_Otro5.get(0,END) )
        listaOtro6=list( self.lst_Otro6.get(0,END) )
        listaOtro7=list( self.lst_Otro7.get(0,END) )

        if self.ValidarLista(listaOtro0)==True:
            bandera=True
        if self.ValidarLista(listaOtro1)==True:
            bandera=True
        if self.ValidarLista(listaOtro2)==True:
            bandera=True
        if self.ValidarLista(listaOtro3)==True:
            bandera=True
        if self.ValidarLista(listaOtro4)==True:
            bandera=True
        if self.ValidarLista(listaOtro5)==True:
            bandera=True
        if self.ValidarLista(listaOtro6)==True:
            bandera=True
        if self.ValidarLista(listaOtro7)==True:
            bandera=True

        #------If bandera-----
        if bandera==True:
            return (True)
        else:
            return (False)
            #print("Ya esta el quipo")
        
##########################################
##########################################    
##########################################

class Limpiar():
    
    def LimpiarLista(lista):
        lista.delete(0,END)

##########################################
##########################################    
##########################################


            
class Boton_Confirmacion(Button):
    lst_GrupoA=None
    lst_GrupoB=None
    lst_GrupoC=None
    lst_GrupoD=None
    lst_GrupoE=None
    lst_GrupoF=None
    lst_GrupoG=None
    lst_GrupoH=None
    Mensaje=""
    
    def __init__(self,lstgrupoA,lstgrupoB,lstgrupoC,lstgrupoD,lstgrupoE,lstgrupoF,lstgrupoG,lstgrupoH,parent,**kw):
        Button.__init__(self,parent,kw)
        self.lst_GrupoA=lstgrupoA
        self.lst_GrupoB=lstgrupoB
        self.lst_GrupoC=lstgrupoC
        self.lst_GrupoD=lstgrupoD
        self.lst_GrupoE=lstgrupoE
        self.lst_GrupoF=lstgrupoF
        self.lst_GrupoG=lstgrupoG
        self.lst_GrupoH=lstgrupoH

    #-------------VALIDAR LISTAS-----------------------------------       
    def ValidarListas(self,v_main):
        
        lista_valores_A = list( self.lst_GrupoA.get(0,END) )
        lista_valores_B = list( self.lst_GrupoB.get(0,END) )
        lista_valores_C = list( self.lst_GrupoC.get(0,END) )
        lista_valores_D = list( self.lst_GrupoD.get(0,END) )
        lista_valores_E = list( self.lst_GrupoE.get(0,END) )
        lista_valores_F = list( self.lst_GrupoF.get(0,END) )
        lista_valores_G = list( self.lst_GrupoG.get(0,END) )
        lista_valores_H = list( self.lst_GrupoH.get(0,END) )
        
        bandera=False
        self.Mensaje=""
        if self.RevisarFaltantes(lista_valores_A,"Grupo A") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_B,"Grupo B") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_C,"Grupo C") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_D,"Grupo D") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_E,"Grupo E") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_F,"Grupo F") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_G,"Grupo G") == True:
            bandera=True
        else:
            bandera=False
        
        if self.RevisarFaltantes(lista_valores_H,"Grupo H") == True:
            bandera=True
        else:
            bandera=False
        
        

    
        if bandera==True:
            messagebox.showinfo("Bracket Mundial",self.Mensaje) #True es completo // False es faltan
            file = open("Template.txt", 'w')
            #-----Grupo A-----
            file.write("Grupo A")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_A[i])
                file.write(",")

            file.write("\n")

            #-----Grupo B-----
            file.write("Grupo B")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_B[i])
                file.write(",")

            file.write("\n")

            #-----Grupo C-----
            file.write("Grupo C")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_C[i])
                file.write(",")

            file.write("\n")

            #-----Grupo D-----
            file.write("Grupo D")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_D[i])
                file.write(",")

            file.write("\n")

            #-----Grupo E-----
            file.write("Grupo E")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_E[i])
                file.write(",")

            file.write("\n")

            #-----Grupo F-----
            file.write("Grupo F")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_F[i])
                file.write(",")

            file.write("\n")

            #-----Grupo G-----
            file.write("Grupo G")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_G[i])
                file.write(",")

            file.write("\n")

            #-----Grupo H-----
            file.write("Grupo H")
            file.write(",")
            for i in range(4):
                file.write(lista_valores_H[i])
                file.write(",")

            file.write("\n")
            
            file.close()

            #-----Leer Archivo-----
            
            file = open("Template.txt", 'r')
            
            lista_archivo=file.readlines()
            for i in range(len(lista_archivo)):
                lista_linea=lista_archivo[i].split(",")
                print(len(lista_linea))
                print(lista_linea)
                print("GRUPO: ",lista_linea[0])
            
            file.close()
            
            #ventana.withdraw()
            import Admin_Bracket_Ganador
            Admin_Bracket_Ganador.ClaseBracketGanador.VentanaBracketGanador(v_main)
            
        else:
            messagebox.showwarning("Bracket Mundial",self.Mensaje)
            
                                 

        
    def RevisarFaltantes(self,lista,nom_grupo):


            
        #---------------------------
        if len(lista) == 4:
            print("La longitud de lista del ",nom_grupo," esta buena")
            self.Mensaje+="El "
            self.Mensaje+=nom_grupo
            self.Mensaje+=" esta completo"
            self.Mensaje+="\n"
            return(True)
        
        else:
            faltante=4-len(lista)
            print("Hacen falta ",faltante,"Equipos en la lista del ",nom_grupo)
            self.Mensaje+="Hacen falta "
            self.Mensaje+=str(faltante)
            self.Mensaje+=" Equipos en la lista del "
            self.Mensaje+=nom_grupo
            self.Mensaje+="\n"
                   

            
            return(False)
            
                    
            
            
        




        

        
        

