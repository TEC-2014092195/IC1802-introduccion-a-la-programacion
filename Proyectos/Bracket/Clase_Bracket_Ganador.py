from tkinter import *
from tkinter import messagebox

class Grupos():
    def LlenarGrupos(btn):
        keys=list(btn.keys())
        print(len(keys))
        
        file = open("Template.txt","r")
        lista = file.readlines()
        n=0
        for i in range(len(lista)):
            for j in range(1,5):
                texto=lista[i].split(",")[j]
                btn["btn"+str(n)].configure(text=texto)
                n+=1
        
        
##################################################################################################################

    
    def AccionF1(btn,btn2):

        def validarcallback(elegido,cambiante1,cambiante2,orig1,orig2):
            
            if cambiante1 == orig1 and cambiante2 != elegido:
                btn2[orig1].configure( text=elegido )
            elif cambiante2 == orig2 and cambiante1 != elegido:
                btn2[orig2].configure( text=elegido )

            elif cambiante1 == elegido and cambiante2 != elegido:
                
                btn2[orig1].configure(text=orig1)
                
            elif cambiante2 == elegido and cambiante1 != elegido:
                
                btn2[orig2].configure(text=orig2)
            else:
                
                messagebox.showinfo("Mundial Brazil 2014","Ya esta ocupado, deseleccione alguno para cambiar de valor")
            
        
        def callback1(event):
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            elegido = t
            cambiante1 = btn2["btn0"].cget("text")
            cambiante2 = btn2["btn1"].cget("text")
            orig1 = "btn0"
            orig2 = "btn1"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback2(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn2"].cget("text")
            cambiante2 = btn2["btn3"].cget("text")
            orig1 = "btn2"
            orig2 = "btn3"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback3(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn4"].cget("text")
            cambiante2 = btn2["btn5"].cget("text")
            orig1 = "btn4"
            orig2 = "btn5"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback4(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn6"].cget("text")
            cambiante2 = btn2["btn7"].cget("text")
            orig1 = "btn6"
            orig2 = "btn7"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback5(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn8"].cget("text")
            cambiante2 = btn2["btn9"].cget("text")
            orig1 = "btn8"
            orig2 = "btn9"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback6(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn10"].cget("text")
            cambiante2 = btn2["btn11"].cget("text")
            orig1 = "btn10"
            orig2 = "btn11"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback7(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn12"].cget("text")
            cambiante2 = btn2["btn13"].cget("text")
            orig1 = "btn12"
            orig2 = "btn13"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        def callback8(event):
            
            print (event.widget.cget("text"))
            t=event.widget.cget("text")
            
            elegido = t
            cambiante1 = btn2["btn14"].cget("text")
            cambiante2 = btn2["btn15"].cget("text")
            orig1 = "btn14"
            orig2 = "btn15"
            
            validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)

        #---------MainDef---------

        listakeys=btn.keys()
        limite=len(listakeys)
        
        for i in range(limite):
            if i < 4:
                btn["btn"+str(i)].bind("<Button-1>", callback1)
            elif i < 8:
                btn["btn"+str(i)].bind("<Button-1>", callback2)
            elif i < 12:
                btn["btn"+str(i)].bind("<Button-1>", callback3)
            elif i < 16:
                btn["btn"+str(i)].bind("<Button-1>", callback4)
            elif i < 20:
                btn["btn"+str(i)].bind("<Button-1>", callback5)
            elif i < 24:
                btn["btn"+str(i)].bind("<Button-1>", callback6)
            elif i < 28:
                btn["btn"+str(i)].bind("<Button-1>", callback7)
            elif i < 32:
                btn["btn"+str(i)].bind("<Button-1>", callback8)

##################################################################################################################
    def AccionF2(btn2,btn3):

        def validarcallback(elegido,cambiante1,cambiante2,orig1,orig2):
            
            if cambiante1 == orig1 and cambiante2 != elegido:
                btn3[orig1].configure( text=elegido )
            elif cambiante2 == orig2 and cambiante1 != elegido:
                btn3[orig2].configure( text=elegido )

            elif cambiante1 == elegido and cambiante2 != elegido:
                
                btn3[orig1].configure(text=orig1)
                
            elif cambiante2 == elegido and cambiante1 != elegido:
                
                btn3[orig2].configure(text=orig2)
            else:
                
                messagebox.showinfo("Mundial Brazil 2014","Ya esta ocupado, deseleccione alguno para cambiar de valor")

        #-----------------
        def validarfase():
            l_get=[]
            l_keysbtn2 = list(btn2.keys())
            for i in range(len(l_keysbtn2)):
                l_get.append( btn2[ l_keysbtn2[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtn2)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
                print("Completo")
                return True
            else:
                print("Falta")
                return False
        #-----------------
        
        def callback1(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn3["btn0"].cget("text")
                cambiante2 = btn3["btn1"].cget("text")
                orig1 = "btn0"
                orig2 = "btn1"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")
            

        def callback2(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn3["btn2"].cget("text")
                cambiante2 = btn3["btn3"].cget("text")
                orig1 = "btn2"
                orig2 = "btn3"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")

        def callback3(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn3["btn4"].cget("text")
                cambiante2 = btn3["btn5"].cget("text")
                orig1 = "btn4"
                orig2 = "btn5"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")

        def callback4(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn3["btn6"].cget("text")
                cambiante2 = btn3["btn7"].cget("text")
                orig1 = "btn6"
                orig2 = "btn7"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase") 

        
        
        listakeys=btn2.keys()
        limite=len(listakeys)
        
        for i in range(limite):
            if i < 4:
                btn2["btn"+str(i)].bind("<Button-1>", callback1)
            elif i < 8:
                btn2["btn"+str(i)].bind("<Button-1>", callback2)
            elif i < 12:
                btn2["btn"+str(i)].bind("<Button-1>", callback3)
            elif i < 16:
                btn2["btn"+str(i)].bind("<Button-1>", callback4)

##################################################################################################################
    def AccionF3(btn3,btn4):

        def validarcallback(elegido,cambiante1,cambiante2,orig1,orig2):
            
            if cambiante1 == orig1 and cambiante2 != elegido:
                btn4[orig1].configure( text=elegido )
            elif cambiante2 == orig2 and cambiante1 != elegido:
                btn4[orig2].configure( text=elegido )

            elif cambiante1 == elegido and cambiante2 != elegido:
                
                btn4[orig1].configure(text=orig1)
                
            elif cambiante2 == elegido and cambiante1 != elegido:
                
                btn4[orig2].configure(text=orig2)
            else:
                
                messagebox.showinfo("Mundial Brazil 2014","Ya esta ocupado, deseleccione alguno para cambiar de valor")

        #-----------------
        def validarfase():
            l_get=[]
            l_keysbtn3 = list(btn3.keys())
            for i in range(len(l_keysbtn3)):
                l_get.append( btn3[ l_keysbtn3[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtn3)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
##                print("Completo")
                return True
            else:
##                print("Falta")
                return False
        #-----------------

        def callback1(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn4["btn0"].cget("text")
                cambiante2 = btn4["btn1"].cget("text")
                orig1 = "btn0"
                orig2 = "btn1"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")

        def callback2(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn4["btn2"].cget("text")
                cambiante2 = btn4["btn3"].cget("text")
                orig1 = "btn2"
                orig2 = "btn3"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")

        listakeys=btn3.keys()
        limite=len(listakeys)
        
        for i in range(limite):
            if i < 4:
                btn3["btn"+str(i)].bind("<Button-1>", callback1)
            elif i < 8:
                btn3["btn"+str(i)].bind("<Button-1>", callback2)

##################################################################################################################
    def AccionF4(btn4,btn5):

        def validarcallback(elegido,cambiante1,cambiante2,orig1,orig2):
            
            if cambiante1 == orig1 and cambiante2 != elegido:
                btn5[orig1].configure( text=elegido )
            elif cambiante2 == orig2 and cambiante1 != elegido:
                btn5[orig2].configure( text=elegido )

            elif cambiante1 == elegido and cambiante2 != elegido:
                
                btn5[orig1].configure(text=orig1)
                
            elif cambiante2 == elegido and cambiante1 != elegido:
                
                btn5[orig2].configure(text=orig2)
            else:
                
                messagebox.showinfo("Mundial Brazil 2014","Ya esta ocupado, deseleccione alguno para cambiar de valor")

        #-----------------
        def validarfase():
            l_get=[]
            l_keysbtn4 = list(btn4.keys())
            for i in range(len(l_keysbtn4)):
                l_get.append( btn4[ l_keysbtn4[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtn4)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
##                print("Completo")
                return True
            else:
##                print("Falta")
                return False
        #-----------------

        def callback1(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn5["btn0"].cget("text")
                cambiante2 = btn5["btn1"].cget("text")
                orig1 = "btn0"
                orig2 = "btn1"
                validarcallback(elegido,cambiante1,cambiante2,orig1,orig2)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")

        listakeys=btn4.keys()
        limite=len(listakeys)
        
        for i in range(limite):
            if i < 4:
                btn4["btn"+str(i)].bind("<Button-1>", callback1)

##################################################################################################################
    def AccionF5(btn5,btn6):
        
        def validarcallback(elegido,cambiante1,orig1):
            
            if cambiante1 == orig1 :
                btn6[orig1].configure( text=elegido )


            elif cambiante1 == elegido :
                
                btn6[orig1].configure(text=orig1)
                
            else:
                
                messagebox.showinfo("Mundial Brazil 2014","Ya esta ocupado, deseleccione alguno para cambiar de valor")

        #-----------------
        def validarfase():
            l_get=[]
            l_keysbtn5 = list(btn5.keys())
            for i in range(len(l_keysbtn5)):
                l_get.append( btn5[ l_keysbtn5[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtn5)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
##                print("Completo")
                return True
            else:
##                print("Falta")
                return False
        #-----------------
        def callback1(event):
            if validarfase() == True: #Puede continuar eligiendo
                t=event.widget.cget("text")
                elegido = t
                cambiante1 = btn6["btn0"].cget("text")
                orig1 = "btn0"

                validarcallback(elegido,cambiante1,orig1)
                
            else:
                messagebox.showinfo("Mundial Brazil 2014","Debe agregar todos los ganadores de la Fase\nHasta que todos esten listos podra elegir la otra Fase")

        listakeys=btn5.keys()
        limite=len(listakeys)
        
        for i in range(limite):
            if i < 4:
                btn5["btn"+str(i)].bind("<Button-1>", callback1)

##################################################################################################################
    def AccionFGanador8(btn,btn2,btn3,btn4,btn5,btn6,v_ganador,v_main):
        
        def validarfase(btnx):
            l_get=[]
            l_keysbtnx = list(btnx.keys())
            for i in range(len(l_keysbtnx)):
                l_get.append( btnx[ l_keysbtnx[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtnx)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
##                print("Completo")
                return True
            else:
                return False
        
        

        def callback1(event):
            flag=True

            if validarfase(btn2) == False:
                flag=False
            elif validarfase(btn3) == False:
                flag=False
            elif validarfase(btn4) == False:
                flag=False
            elif validarfase(btn5) == False:
                flag=False
            elif validarfase(btn6) == False:
                flag=False
            ###
            if flag == False:


                messagebox.showinfo("BM","El Bracket se guardará hasta que el bracket se complete")
            else:
                
                file=open("Ganador.txt","w")
                l_keys = list( btn2.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn2[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn3.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn3[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn4.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn4[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn5.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn5[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn6.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn6[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
                
                file.close()

#--------------------Reiniciar Usuarios
                file=open("Usuarios/Usuarios.txt","w")
                file.close()

                messagebox.showinfo("BM","Bracket Guardado")
                v_ganador.destroy()
                v_main.update()
                v_main.deiconify()
            

        btn6["btn0"].bind("<Button-1>", callback1)
##################################################################################################################
##################################################################################################################
##################################################################################################################
    def AccionFGanador4(btn,btn2,btn3,btn4,btn5,v_ganador,v_main):
        
        def validarfase(btnx):
            l_get=[]
            l_keysbtnx = list(btnx.keys())
            for i in range(len(l_keysbtnx)):
                l_get.append( btnx[ l_keysbtnx[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtnx)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
##                print("Completo")
                return True
            else:
                return False
        
        

        def callback1(event):
            flag=True

            if validarfase(btn2) == False:
                flag=False
            elif validarfase(btn3) == False:
                flag=False
            elif validarfase(btn4) == False:
                flag=False
            elif validarfase(btn5) == False:
                flag=False
            ###
            if flag == False:
                messagebox.showinfo("BM","El Bracket se guardará hasta que el bracket se complete")
            else:
                
                file=open("Ganador.txt","w")
                l_keys = list( btn2.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn2[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn3.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn3[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn4.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn4[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn5.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn5[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
#--------------------Reiniciar Usuarios
                file=open("Usuarios/Usuarios.txt","w")
                file.close()

                messagebox.showinfo("BM","Bracket Guardado")
                v_ganador.destroy()
                v_main.update()
                v_main.deiconify()

        btn5["btn0"].bind("<Button-1>", callback1)
##################################################################################################################
##################################################################################################################
##################################################################################################################
    def AccionFGanador2(btn,btn2,btn3,btn4,v_ganador,v_main):
        
        def validarfase(btnx):
            l_get=[]
            l_keysbtnx = list(btnx.keys())
            for i in range(len(l_keysbtnx)):
                l_get.append( btnx[ l_keysbtnx[i] ].cget("text") )
            
            bandera=True
            for i in range(len(l_keysbtnx)):
                if ("btn"+str(i)) in l_get:
                    bandera=False

            if bandera == True:
##                print("Completo")
                return True
            else:
                return False
        
        

        def callback1(event):
            flag=True

            if validarfase(btn2) == False:
                flag=False
            elif validarfase(btn3) == False:
                flag=False
            elif validarfase(btn4) == False:
                flag=False
            ###
            if flag == False:
                messagebox.showinfo("BM","El Bracket se guardará hasta que el bracket se complete")
            else:
                file=open("Ganador.txt","w")
                l_keys = list( btn2.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn2[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn3.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn3[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")
##############################################################
                l_keys = list( btn4.keys() )
                limite = len(l_keys)
                
                for i in range( limite ):
                    bget = btn4[ "btn"+str(i) ].cget("text")
                    file.write(bget)
                    file.write(",")
                file.write("\n")

#--------------------Reiniciar Usuarios
                file=open("Usuarios/Usuarios.txt","w")
                file.close()
                
                messagebox.showinfo("BM","Bracket Guardado")
                v_ganador.destroy()
                v_main.update()
                v_main.deiconify()
            

        btn4["btn0"].bind("<Button-1>", callback1)
