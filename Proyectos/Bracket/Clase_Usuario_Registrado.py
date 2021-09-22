from tkinter import *
from tkinter import messagebox
import Clase_Validar_Pts

class Grupos():
    def LlenarGrupos(btn):
        keys=list(btn.keys())
        
        file = open("Template.txt","r")
        lista = file.readlines()
        n=0
        for i in range(len(lista)):
            for j in range(1,5):
                texto=lista[i].split(",")[j]
                btn["btn"+str(n)].configure(text=texto)
                n+=1

    

        
        
    def LlenarBotones8(btn2,btn3,btn4,btn5,btn6,id_bracket,v_ganador,v_main):
        def Llenar(btnx,indice):
            keys=list(btnx.keys())
##            print(len(keys))
            
            file = open(("Usuarios/Registrados/user_"+id_bracket+".txt"), 'r')
            lista = file.readlines()
            for i in range( len(keys) ):
                t=lista[indice].split(",")[i]    
                btnx[ "btn"+str(i) ].configure(text=t)
            
            

            
        Llenar(btn2,0) # Indice= la fila de los que el user elgió en la primera fase
        Llenar(btn3,1)
        Llenar(btn4,2)
        Llenar(btn5,3)
        Llenar(btn6,4)
        
    def LlenarBotones4(btn2,btn3,btn4,btn5,id_bracket,v_ganador,v_main):
        def Llenar(btnx,indice):
            keys=list(btnx.keys())
##            print(len(keys))
            
            file = open(("Usuarios/Registrados/user_"+id_bracket+".txt"), 'r')
            lista = file.readlines()
            for i in range( len(keys) ):
                t=lista[indice].split(",")[i]    
                btnx[ "btn"+str(i) ].configure(text=t)
            
            

            
        Llenar(btn2,0) # Indice= la fila de los que el user elgió en la primera fase
        Llenar(btn3,1)
        Llenar(btn4,2)
        Llenar(btn5,3)
         

    def LlenarBotones2(btn,btn2,btn3,btn4,id_bracket,v_ganador,v_main):
        def Llenar(btnx,indice):
            keys=list(btnx.keys())
##            print(len(keys))
            
            file = open(("Usuarios/Registrados/user_"+id_bracket+".txt"), 'r')
            lista = file.readlines()
            for i in range( len(keys) ):
                t=lista[indice].split(",")[i]    
                btnx[ "btn"+str(i) ].configure(text=t)
            
            

            
        Llenar(btn2,0) # Indice= la fila de los que el user elgió en la primera fase
        Llenar(btn3,1)
        Llenar(btn4,2)
         

   
    
