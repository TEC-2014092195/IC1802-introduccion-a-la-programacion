from tkinter import *
from tkinter import messagebox
import Admin_Bracket_Ganador
class BotonAgregar(Button):
        def __init__(self,entradas,lst,g,parent,**kw): 
            Button.__init__(self,parent,kw)
            self.Entradas=entradas
            self.Lst=lst
            self.G=g

        def Agregar(self):
            if self.Entradas[ "var"+self.G ].get() == "":
                messagebox.showinfo("BM","Digite un caracter al menos")
                self.Entradas[ "var"+self.G ].set("")
            else:
                
                lista=self.Lst["lst"+self.G].get(0,END)
                if len(lista) >= 4 :
                    messagebox.showinfo("BM","Lista "+self.G+" está llena")
                    self.Entradas[ "var"+self.G ].set("")
                    
                else:
                    limite=len(list(self.Lst.keys()))
                    lista=self.Lst["lst"+self.G].get(0,END)
                    bandera=False
                    ent = self.Entradas[ "var"+self.G ].get()
                    keys=list(self.Lst.keys())
                    for i in range(limite):
                        lista=self.Lst[(keys[i])].get(0,END)
                        if ent in lista:
                            bandera=True
                

                    if bandera==True:
                        messagebox.showinfo("BM","Duplicado")
                        self.Entradas[ "var"+self.G ].set("")
                    else:
                        self.Lst["lst"+self.G].insert(END,self.Entradas[ "var"+self.G ].get())
                        self.Entradas[ "var"+self.G ].set("")
            
class BotonLimpiar(Button):
        def __init__(self,lst,g,parent,**kw): 
            Button.__init__(self,parent,kw)
            self.Lst=lst
            self.G=g
        def Limpiar(self):
            self.Lst["lst"+self.G].delete(0,END)

class Guardar():
    
    def Verificar(lst,c_grupos,v_admin,v_main):
        keys=list(lst.keys())
        bandera=True
        mensaje=""
        for i in range(len(keys)):
            lista=lst[ (keys[i]) ].get( 0,END )
            if len(lista) < 4:
                bandera=False
                mensaje+="\n"+(keys[i])

        if bandera == False:
            
            messagebox.showinfo("BM","Falta llenar \n"+mensaje)

        else:
            
            keys.sort()
            
            file = open("Template.txt", 'w')

            
            for i in range(len(keys)):
                print(keys[i].replace("lst",""))
                    
                file.write(keys[i].replace("lst",""))
                file.write(",")
                
                lista=lst[ (keys[i]) ].get( 0,END )
                print(len(keys))
                print(lista)
                for i in range(4):
                    file.write(lista[i])
                    file.write(",")
                
                file.write("\n")

            file.close()

        v_admin.destroy()
        
        Admin_Bracket_Ganador.ClaseAdminBracketGanador.VentanaAdminGanador(c_grupos,v_main)
        


            

        
        

  
