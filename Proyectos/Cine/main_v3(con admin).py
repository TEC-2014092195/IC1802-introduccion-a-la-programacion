from tkinter import *


v=Tk()

v.geometry("600x500+%d+%d" %((v.winfo_screenwidth() - 600) / 2,(v.winfo_screenheight() - 500) / 2))
v.configure(bg="#d69b6f")



imgTitulo=PhotoImage(file="title.png")
lblTitulo=Label(v,image=imgTitulo,bd=0).place(x=75,y=30)
    
entradaU=StringVar()
lblUsuario=Label(v,text="USUARIO",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626").place(x=275,y=170)
txtUsuario=Entry(v,bd=0,textvariable=entradaU).place(x=245, y=200)

entradaC=StringVar()
lblClave=Label(v,text="CONTRASEÑA",font=("Tw Cen MT Condensed",14),foreground="white",bg="#262626").place(x=265,y=223)
txtClave=Entry(v,bd=0,textvariable=entradaC).place(x=245, y=255)


##--------------Clase matriz----------------------
class claseMatriz():
    c_matriz=[]
    m_matriz=[]
    disponibles=0
    def __init__(self):
        
        for i in range(16):#16 filas
            for j in range(10):#10 columnas
##                if i>2 and j>4: #prueba llenando fila 1
##                    self.c_matriz.append(1)
##                    
##                else:
                self.c_matriz.append(0)
            self.m_matriz.append(self.c_matriz)
            self.c_matriz=[]
        print(self.m_matriz)

    def getMatriz(self):
        return(self.m_matriz)
        

    def verificar_disponibles(self):
        self.disponibles=0
        d={}
        indices=0
        for i in range(16):#16 filas
            for j in range(10):#10 columnas
                if self.m_matriz[i][j]==2: #2 significa disponible
                    self.disponibles+=1
                    d[indices]=(i,j)
                    indices+=1
        
        return(print("Cuantos Disponibles: ",len(d.keys()),"Indices Disponibles: ",list(d.values())))
        
    def llenar_con_ceros(self):
        self.m_matriz=[]
        
        for i in range(16):#16 filas
            for j in range(10):#10 columnas
                    self.c_matriz.append(0)
            self.m_matriz.append(self.c_matriz)
            self.c_matriz=[]
        return(self.m_matriz)
        


    def definir_cuantos_disponibles(self,can_asientos):
        filas=0
        columnas=0
        self.m_matriz=[]
        self.c_matriz=[]
        
        filas=int(can_asientos//10)
        columnas=can_asientos%10
        if filas == 0 and columnas==0:
            print("No selecciono nada")
            self.llenar_con_ceros()
        elif filas==0 and columnas >0:
            
            c_matriz=[]
            for i in range(16):
                for j in range(10):
                    if i == 0 and columnas > 0:
                        self.c_matriz.append(2)
                        columnas-=1
                    else:
                        self.c_matriz.append(0)
                self.m_matriz.append(self.c_matriz)
                self.c_matriz=[]
        else:
            while filas > -1 or columnas > -1:
                print("Columnas",columnas,"filas",filas)
                if filas > 0:
                    for j in range(10):
                            self.c_matriz.append(2)

                    self.m_matriz.append(self.c_matriz)
                
                    self.c_matriz=[]

                    filas-=1
                    
                    
                elif filas == 0 and columnas > 0:
                    
                    self.c_matriz.append(2)
                    columnas-=1
                elif filas == 0 and columnas == 0:
                    if len(self.c_matriz) < 10 and len(self.c_matriz)>0:
                        faltantes=0
                        faltantes = 10 - len(self.c_matriz)
                        for i in range(0,faltantes):
                            self.c_matriz.append(0)
                        self.m_matriz.append(self.c_matriz)
                        
                    print("Long de M_MATRIZ:",len(self.m_matriz))
                    if len(self.m_matriz) <= 16:
                        faltantes=0
                        faltantes = 16 - len(self.m_matriz)
                        print("Faltantes",faltantes)
                        self.c_matriz=[]
                        for i in range(0,faltantes):
                            for j in range(10):
                                self.c_matriz.append(0)

                            self.m_matriz.append(self.c_matriz)
                            self.c_matriz=[]
                        
                    filas-=1
                    columnas-=1
                
        print(self.m_matriz)
                
            
            
            
##        for i in range(16):
##            for j in range(10):
##                if filas > 0:
##                    
##                    self.c_matriz.append(0)
##            self.m_matriz.append(self.c_matriz)
##            self.c_matriz=[]
##        
##        print(self.m_matriz)
        


        
matriz_cine = claseMatriz()

##--------------Clase Diccionario----------------------
class Diccionario(claseMatriz):
    pass
    c={}
    p={}
    h={}
    e={}
    
    e2={}
    h2={}
    p2={}
    c2={}
    def __init__(self):
        self.e={'vip':0,'normal':0,'graderia':0}
        self.e['asien']=self.llenar_con_ceros()
        self.h['3:30']=[self.e]
        self.p['Peli0']=[self.h]
        self.c['Cine0']=[self.p]


        print(self.c)

    def agregarDic(self,nom_cine,peli,hora,asientos):
        print("Cine",nom_cine,"Peli: ",peli,"Horario",hora,"Asientos",asientos)
        e2={}
        h2={}
        p2={}
        c2={}
        if not nom_cine in self.c:
            e2={'vip':0,'normal':0,'graderia':0,'asien':asientos}
            h2[hora]=[e2]
            p2[peli]=[h2]
            c2[nom_cine]=[p2]
            self.c.update(c2)
        else:
            if not peli in self.c[nom_cine][0]:
                e2={'vip':0,'normal':0,'graderia':0,'asien':asientos}
                h2[hora]=[e2]
                p2[peli]=[h2]
                self.c[nom_cine][0].update(p2)
            else:
                if not hora in self.c[nom_cine][0][peli][0]:
                    e2={'vip':0,'normal':0,'graderia':0}

                    e2['asien']=asientos
                    
                    h2[hora]=[e2]
                    self.c[nom_cine][0][peli][0].update(h2)
                else:
                    e2={'vip':0,'normal':0,'graderia':0,'asien':0}
##                    
##                    old_asientos=self.c[nom_cine][0][peli][0][hora][0]['asien']
##                    old_can_entradas=self.c[nom_cine][0][peli][0][hora][0]['vip']

                    e2['asien']=asientos

                    
##                    e2['vip']= old_can_entradas#0
                    self.c[nom_cine][0][peli][0][hora][0].update(e2)

        print(self.c)

    def getDic(self):
        return(self.c)



    def setDic(self,diccionario_temp):
        print(diccionario_temp)
            

claseDic=Diccionario()





#-----Form Modo Admin (Selección de asientos)-----

def ventana_modo_admin():
    v.withdraw()
    ventana_modo_admin = Toplevel()



##    matriz_cine.llenar_con_ceros()
##    matriz_cine.verificar_disponibles()
#######################################################################################################################################   
    #matriz_cine.definir_cuantos_disponibles(150)
    #matriz_cine.verificar_disponibles()

    

    

    class Boton(Button):
        def __init__(self,variable,lista,txt_agregar,parent,**kw): #variable es el texto agragado
            Button.__init__(self,parent,kw)
            self.Variables=variable
            self.Lista=lista
            self.TxtAgregar=txt_agregar
        def get(self):
            if self.Variables.get()!="":
                duplicado=0
                for i in range ( len( self.Lista.get(0,END) ) ): #Tupla de todos los items de lista
                    if self.Variables.get()== self.Lista.get(0,END)[i]:
                        duplicado=1
                if duplicado==1:
                    print("Ya esta en lista")
                else:
                    self.Lista.insert(END,self.Variables.get())
                    self.TxtAgregar.grid_remove()
                    self.grid_remove()#esconde el boton
                    

                self.Variables.set("")
                print(self.Variables.get())
            else:
                print("Debe ingresar algun dato")

        def eliminar(self):
            indice=self.Lista.curselection()[0]
            self.Lista.delete(indice)
            print("Item seleccionado: ",indice)
            
            
    ventana_modo_admin.geometry("1024x768+%d+%d" %((ventana_modo_admin.winfo_screenwidth() - 1024) / 2,(ventana_modo_admin.winfo_screenheight() - 768) / 2))
    ventana_modo_admin.configure(bg="#262626")

    
    frameListas=Frame(ventana_modo_admin)
    frameListas.grid()
    frameListas.configure(bg="#262626")
    frameListas.place(x=30,y=90)


    #------------------Agregar Cines--------------------------------
    lblCine=Label(frameListas,text="SELECCIONAR CINE",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblCine.grid(row=0,column=0)
    
    nom_cine=StringVar()
    txt_nom_cine=Entry(frameListas,textvariable=nom_cine,bd=0,font=("Tw Cen MT Condensed",14))
    txt_nom_cine.grid(row=3,column=0,pady=10)
    txt_nom_cine.grid_remove()


    cadena=StringVar()
    lstCines=Listbox(frameListas,width=30,height=10,bd=0,exportselection=0,selectbackground="#83b5b4",selectforeground="#2f2f2f",font=("Tw Cen MT Condensed",12))

    class Seleccionar_Item_Cine():
        VariableCine=""
        
        def Item_ListaCine(self,event):
            try:
                valor=str(lstCines.get(lstCines.curselection()))
                
                self.VariableCine=valor
                
                indice=lstCines.curselection()[0]
                print(valor,"Indice:",indice)
            except:
                print("No hay elemento seleccionado")

        def getVariable(self):
            if self.VariableCine != "":
                return(self.VariableCine)
            else:
                return(False)

    claseCine = Seleccionar_Item_Cine()
    lstCines.bind('<<ListboxSelect>>',claseCine.Item_ListaCine)
    

    cadena_combo=StringVar()
    cadena_combo="Cinemark","Magaly"
    
    d=claseDic.getDic()
    reg_cines=list(d.keys())
   
    print(reg_cines)
    

    for i in range(len(reg_cines)):
        lstCines.insert(END,reg_cines[i])
    lstCines.grid(row=1,column=0,pady=5,padx=10)

    def esconder():
        txt_nom_cine.grid(pady=10)
        btnAgregarItem.grid(pady=10)
        btnNuevoCine.grid_remove()

    btnNuevoCine=Button(frameListas,text="Nuevo Cine",padx=2,pady=2,font=("Tw Cen MT Condensed",14),bg="#83b5b4",bd=0 ,foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnNuevoCine.configure(command=esconder)
    btnNuevoCine.grid(row=2,column=0,pady=10)

    btnAgregarItem=Boton(nom_cine,lstCines,txt_nom_cine,frameListas,text="Agregar Cine",bg="#83b5b4",bd=0,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnAgregarItem.configure(command=btnAgregarItem.get)
    btnAgregarItem.grid(row=4,column=0,padx=10,pady=10)
    btnAgregarItem.grid_remove()

    


        
######    btnEliminarItem=Boton(nom_cine,lstCines,frameListas,text="Eliminar")
######    btnEliminarItem.configure(command=btnEliminarItem.eliminar)
######    btnEliminarItem.grid(row=1,column=1,padx=10,pady=10)

        
    
    #------------------Agregar Peliculas--------------------------------
    lblPeli=Label(frameListas,text="SELECCIONAR PELICULAS",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblPeli.grid(row=0,column=1)
    
    nom_peli=StringVar()
    txt_nom_peli=Entry(frameListas,textvariable=nom_peli,bd=0,font=("Tw Cen MT Condensed",14))
    txt_nom_peli.grid(row=3,column=1,pady=10)
    txt_nom_peli.grid_remove()


    
    lstPelis=Listbox(frameListas,width=30,height=10,bd=0,exportselection=0,selectbackground="#83b5b4",selectforeground="#2f2f2f",font=("Tw Cen MT Condensed",12))


    class Seleccionar_Item_Peli():
        VariablePeli=""
        def Item_ListaPelis(self,event):
            try:
                valor=str(lstPelis.get(lstPelis.curselection()))
                self.VariablePeli=valor
                indice=lstPelis.curselection()[0]
                print(valor,"Indice:",indice)
            except:
                print("No hay elemento seleccionado")

        def getVariable(self):
            if self.VariablePeli != "":
                return(self.VariablePeli)
            else:
                return(False)

    clasePeli = Seleccionar_Item_Peli()
    lstPelis.bind('<<ListboxSelect>>',clasePeli.Item_ListaPelis)
    

    cadena_pelis=StringVar()
    cadena_pelis="Capitan America","God's Not Dead"
    
    d=claseDic.getDic()
    
    new_d=list(d.values())
    
    dpelis=new_d[0][0]
    
    reg_pelis=list(dpelis.keys())
    
    print(reg_pelis)
##    reg_cines=list(d[0].keys())
##    
##    print(reg_cines)
##    
##
##    for i in range(len(reg_cines)):
##        lstCines.insert(END,reg_cines[i])
##    lstCines.grid(row=1,column=0,pady=5,padx=10)


    for i in range(len(reg_pelis)):
        lstPelis.insert(END,reg_pelis[i])
    lstPelis.grid(row=1,column=1,pady=10,padx=5)

    def esconder():
        txt_nom_peli.grid(pady=10)
        btnAgregarItemPeli.grid(pady=10)
        btnNuevoPeli.grid_remove()


    btnNuevoPeli=Button(frameListas,text="Nueva Pelicula",padx=2,pady=2,font=("Tw Cen MT Condensed",14),bg="#83b5b4",bd=0 ,foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnNuevoPeli.configure(command=esconder)
    btnNuevoPeli.grid(row=2,column=1,pady=10)
    
    btnAgregarItemPeli=Boton(nom_peli,lstPelis,txt_nom_peli,frameListas,text="Agregar Pelicula",bg="#83b5b4",bd=0,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnAgregarItemPeli.configure(command=btnAgregarItemPeli.get)
    btnAgregarItemPeli.grid(row=4,column=1,padx=10,pady=10)
    btnAgregarItemPeli.grid_remove()

    
    
    

    #------------------Agregar Horario--------------------------------
    lblHorario=Label(frameListas,text="SELECCIONAR HORARIO",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblHorario.grid(row=0,column=2)

    horario=StringVar()
    txt_horario=Entry(frameListas,textvariable=horario,bd=0,font=("Tw Cen MT Condensed",14))
    txt_horario.grid(row=3,column=2,pady=10)
    txt_horario.grid_remove()


    
    lstHorario=Listbox(frameListas,width=30,height=10,bd=0,exportselection=0,selectbackground="#83b5b4",selectforeground="#2f2f2f",font=("Tw Cen MT Condensed",12))



    class Seleccionar_Item_Horario():
        VariableHorario=""
        def Item_ListaHorario(self,event):
            try:
                valor=str(lstHorario.get(lstHorario.curselection()))
                
                self.VariableHorario=valor

                indice=lstHorario.curselection()[0]
                print(valor,"Indice:",indice)
            except:
                print("No hay elemento seleccionado")

        def getVariable(self):
            if self.VariableHorario != "":
                return(self.VariableHorario)
            else:
                return(False)

    claseHorario = Seleccionar_Item_Horario()
    lstHorario.bind('<<ListboxSelect>>',claseHorario.Item_ListaHorario)
    

    cadena_horario=StringVar()
    cadena_horario="3:30","5:40"
    

    d=claseDic.getDic()

    dhorario=list( list( d.values() )[0][0].values() )[0][0]
    
    reg_horario=list(dhorario.keys())
    
    print(reg_horario)



    

    for i in range(len(reg_horario)):
        lstHorario.insert(END,reg_horario[i])
    lstHorario.grid(row=1,column=2,pady=10,padx=10)

    def esconder():
        txt_horario.grid(pady=10)
        btnAgregarItemHorario.grid(pady=10)
        btnNuevoHorario.grid_remove()


    btnNuevoHorario=Button(frameListas,text="Nuevo Horario",padx=2,pady=2,font=("Tw Cen MT Condensed",14),bg="#83b5b4",bd=0 ,foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnNuevoHorario.configure(command=esconder)
    btnNuevoHorario.grid(row=2,column=2,pady=10)
    
    btnAgregarItemHorario=Boton(horario,lstHorario,txt_horario,frameListas,text="Agregar Horario",bg="#83b5b4",bd=0,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnAgregarItemHorario.configure(command=btnAgregarItemHorario.get)
    btnAgregarItemHorario.grid(row=4,column=2,padx=10,pady=10)
    btnAgregarItemHorario.grid_remove()    
    
    
    #------------------Agregar Asientos--------------------------------

    lblAsientos=Label(frameListas,text="AGREGAR ASIENTOS",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblAsientos.grid(row=0,column=4)
    class Seleccionar_Item_Asientos():
        VariableAsientos=""
        def verificar_cantidad(self):
            var_asientos=0
            try:
                print(type(asientos))
                var_asientos=str(asientos.get())
                var_asientos=int(var_asientos)
                if 0 <= var_asientos <= 160:
                    print("Correcto")
                    self.VariableAsientos=var_asientos
                    print(self.VariableAsientos)
                else:
                    print("No cumple rango, debe ser de 0 a 159")
                    messagebox.showwarning("Retro Cinema", "No cumple rango\n NOTA: Recuerde debe ser de 0 a 159")
            except:
                messagebox.showwarning("Retro Cinema", "No cumple tipo de valor\n NOTA: Recuerde debe ser de 0 a 159")
                print("Debe ser un entero, entre 0 y 159")
        def getVariable(self):
            if self.VariableAsientos != "":
                return(self.VariableAsientos)
            else:
                return(False)



    
    asientos=StringVar()
    asientos.set(0)
    spn_asientos=Entry(frameListas,textvariable=asientos,bd=0,font=("Tw Cen MT Condensed",14),width=6)
    
    
    spn_asientos.grid(row=1,column=4,pady=10)


    claseAsientos = Seleccionar_Item_Asientos()
    btnNuevoAsientos=Button(frameListas,text="Confirmar Cantidad",padx=2,pady=2,bd=0,bg="#d55534",font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f")
    btnNuevoAsientos.configure(command=claseAsientos.verificar_cantidad)
    btnNuevoAsientos.grid(row=2,column=4,pady=10)
    
    
    
    class BotonAgregarTodo(Button,Diccionario,claseMatriz):
        pass
        
        def __init__(self,cine,peli,horario,asientos,parent,**kw): #variable es el texto agragado
            Button.__init__(self,parent,kw)
            self.Cine=cine
            self.Peli=peli
            self.Horario=horario
            self.Asientos=asientos
            
        def ValidarTodo(self):
            print(type(self.Cine))
            print(type(self.Peli))
            print(type(self.Horario))
            print(type(self.Asientos))
            print(self.Cine)
            print(self.Peli)
            print(self.Horario)
            print(self.Asientos)
            
           
            if isinstance(self.Cine,bool) == True or isinstance(self.Peli,bool) == True or isinstance(self.Horario,bool) == True or isinstance(self.Asientos,bool) == True:
                print("Falta algun campo")
                
                print(type(self.Cine))
                print(type(self.Peli))
                print(type(self.Horario))
                print(type(self.Asientos))
                messagebox.showwarning("Retro Cinema", "Falta campos por seleccionar\n NOTA: Recuerde confirmar el número de asientos")

                self.destroy()
                btnConfirmarCampos.grid()
            else:
                print("Funciona correctamente")
                self.definir_cuantos_disponibles(self.Asientos)
                
                self.verificar_disponibles()
                self.agregarDic(self.Cine,self.Peli,self.Horario,self.getMatriz())
                #Agregar y cerrar
                self.destroy()
                cerrar_con_equis()
            
            
            
            
    frameBtnConfirm=Frame(ventana_modo_admin)
    frameBtnConfirm.grid()
    frameBtnConfirm.configure(bg="#262626")
    frameBtnConfirm.place(x=600,y=500)
    
    def LlamarBoton():
        
        btnConfirmarCampos.grid_remove()
        
        btnAgregarTodo = BotonAgregarTodo(claseCine.getVariable(),clasePeli.getVariable(),claseHorario.getVariable(),claseAsientos.getVariable(),ventana_modo_admin,text="AGREGAR TODOS",bg="#83b5b4",bd=0,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
        btnAgregarTodo.configure(command=btnAgregarTodo.ValidarTodo)
        btnAgregarTodo.place(x=600,y=500)

        ventana_modo_admin.mainloop()

    btnConfirmarCampos=Button(frameBtnConfirm,text="CONFIRMAR CAMPOS",padx=2,pady=2,bd=0,bg="#d55534",font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f")
    btnConfirmarCampos.configure(command=LlamarBoton)
    btnConfirmarCampos.grid(row=0,column=0)

    

    
    def cerrar_con_equis():
        ventana_modo_admin.destroy()
        v.update()
        v.deiconify()

    ventana_modo_admin.protocol('WM_DELETE_WINDOW', cerrar_con_equis)



    

#-----Fin Funcion modo admin----    






#-----Form Modo Usuario (Selección de asientos)-----
def ventana_modo_usuario():
    v.withdraw()
    v_modo_usuario = Toplevel()
    

##    matriz_cine.llenar_con_ceros()
##    matriz_cine.verificar_disponibles()
#########################################################################################################################################   
##    matriz_cine.definir_cuantos_disponibles(150)
##    matriz_cine.verificar_disponibles()


    
    
    #-----Clase Botones-----
    
    class ButtonFuncion ( Button ):
        bandera=False
        def __init__ ( self, asientos, parent,  **kw ):
                Button.__init__ ( self, parent, kw )
                self.Asientos = asientos
                
        def launch ( self ):

            n_row=0
            
            if self.bandera==False:
                self.configure(bg="#9adb5a")
                if self.Asientos < 10:
                    n_row=0
                    n_column=self.Asientos
                elif self.Asientos >=10:
                    n_row=int(self.Asientos//10)
                    n_column=self.Asientos%10
                print("Fila: ",n_row,"Columna: ",n_column,"Valor: ",1)
                self.bandera=True
                
            else:
                self.configure(bg="#d55534")
                if self.Asientos < 10:
                    n_row=0
                    n_column=self.Asientos
                elif self.Asientos >=10:
                    n_row=int(self.Asientos//10)
                    n_column=self.Asientos%10
                print("Fila: ",n_row,"Columna: ",n_column,"Valor: ",0)
                self.bandera=False

    #-----Fin clase Botones-----
    def Validar():
        messagebox.showinfo("Validar","Desea esos asientos")

    def Atras():
        v_modo_usuario.destroy()
        v.update()
        v.deiconify()

    def cerrar_con_equis():
        v_modo_usuario.destroy()
        v.update()
        v.deiconify()
    #-----Inicio-----
    v_modo_usuario.geometry("800x600+%d+%d" %((v.winfo_screenwidth() - 800) / 2,(v.winfo_screenheight() - 600) / 2))
    
    v_modo_usuario.configure(bg="#262626")
    imgPantalla=imgTitulo
    lblPatalla=Label(v_modo_usuario,image=imgPantalla,bd=0,bg="#262626").place(x=150,y=0)

    #-----btnFrame-----
        
    btnFrame=Frame(v_modo_usuario)
    btnFrame.configure(bg="#262626")
    btnFrame.grid()
    btnFrame.place(x=60,y=125)



    #-----creación_de_botones(primera columna de izq a der)-----
    
    b={}
    for i in range(80):#En vez de 80 va la cantidad de asientos
            b[i] = ButtonFuncion ( i, btnFrame, text=str(i),padx=2,pady=2,height=0,width=3,bd=0,bg="#d55534",font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f" )
            b[i].configure ( command=b[i].launch )
            if i < 10: #10 es la cantidad de columnas
                n_fila=0
                b[i].grid(row=n_fila,column=i,padx=1,pady=1)
            elif i >= 10:
                n_fila=int(i//10)
                n_columna=i%10
                b[i].grid(row=n_fila,column=n_columna,padx=1,pady=1)

    
    #-----btnFrame2-----
    btnFrame2=Frame(v_modo_usuario)
    btnFrame2.configure(bg="#262626")
    btnFrame2.grid()
    btnFrame2.place(x=400,y=125)
    
    #-----creación_de_botones(segunda columna de izq a der)-----
    otros=0
    for i in range(100):
        otros=i
        otros+=80
        
        b[otros] = ButtonFuncion ( otros, btnFrame2, text=str(otros),padx=2,pady=2,height=0,width=3,bd=0,bg="#d55534",font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f" )
        b[otros].configure ( command=b[otros].launch )
        if otros < 10: #10 es la cantidad de columnas
            n_fila=0
            b[otros].grid(row=n_fila,column=otros,padx=1,pady=1)
        elif otros >= 10:
            n_fila=int(otros//10)
            n_columna=otros%10
            b[otros].grid(row=n_fila,column=n_columna,padx=1,pady=1)


    print(b[0].cget("text"))
    
    #-----ultimos_botones-----
    
    btnAtras=Button(v_modo_usuario,text="VOLVER",bg="#83b5b4",bd=0 , command=Atras,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white").place(x=15,y=500)
    btnConfirmar=Button(v_modo_usuario,text="CONFIRMAR",bg="#83b5b4",bd=0 , command=matriz_cine,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white").place(x=700,y=500)
                                                                            #command llamar a def de la clase matriz_cine
                                
    v_modo_usuario.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

#-----Fin Funcion Modo Usuario-----

##################################
##################################
##################################
##################################
##################################
##################################    
##################################
##################################
##################################
###################################-----Fin Funcion Modo Usuario (Elegir )-----
    
def ventana_modo_usuario_v1():
    v.withdraw()
    ventana_modo_usuario_v1 = Toplevel()

           
            
    ventana_modo_usuario_v1.geometry("1024x768+%d+%d" %((ventana_modo_usuario_v1.winfo_screenwidth() - 1024) / 2,(ventana_modo_usuario_v1.winfo_screenheight() - 768) / 2))
    ventana_modo_usuario_v1.configure(bg="#262626")

    
    frameListas=Frame(ventana_modo_usuario_v1)
    frameListas.grid()
    frameListas.configure(bg="#262626")
    frameListas.place(x=30,y=90)


    #------------------Agregar Cines--------------------------------
    lblCine=Label(frameListas,text="SELECCIONAR CINE",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblCine.grid(row=0,column=0)


##    cadena=StringVar()
    lstCines=Listbox(frameListas,width=30,height=10,bd=0,exportselection=0,selectbackground="#83b5b4",selectforeground="#2f2f2f",font=("Tw Cen MT Condensed",12))

    class Seleccionar_Item_Cine():
        VariableCine=""
        
        def Item_ListaCine(self,event):
            try:
                valor=str(lstCines.get(lstCines.curselection()))
                
                self.VariableCine=valor
                
                indice=lstCines.curselection()[0]
                print(valor,"Indice:",indice)
            except:
                print("No hay elemento seleccionado")

        def getVariable(self):
            if self.VariableCine != "":
                return(self.VariableCine)
            else:
                return(False)

    claseCine = Seleccionar_Item_Cine()
    lstCines.bind('<<ListboxSelect>>',claseCine.Item_ListaCine)
    

##    cadena_combo=StringVar()
##    cadena_combo="Cinemark","Magaly"
    
    d=claseDic.getDic()
    reg_cines=list(d.keys())
   
    print(reg_cines)
    

    for i in range(len(reg_cines)):
        lstCines.insert(END,reg_cines[i])
    lstCines.grid(row=1,column=0,pady=5,padx=10)

        
    
    #------------------Agregar Peliculas--------------------------------
    lblPeli=Label(frameListas,text="SELECCIONAR PELICULAS",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblPeli.grid(row=0,column=1)
    



    
    lstPelis=Listbox(frameListas,width=30,height=10,bd=0,exportselection=0,selectbackground="#83b5b4",selectforeground="#2f2f2f",font=("Tw Cen MT Condensed",12))


    class Seleccionar_Item_Peli():
        VariablePeli=""
        def Item_ListaPelis(self,event):
            try:
                valor=str(lstPelis.get(lstPelis.curselection()))
                self.VariablePeli=valor
                indice=lstPelis.curselection()[0]
                print(valor,"Indice:",indice)
            except:
                print("No hay elemento seleccionado")

        def getVariable(self):
            if self.VariablePeli != "":
                return(self.VariablePeli)
            else:
                return(False)

    clasePeli = Seleccionar_Item_Peli()
    lstPelis.bind('<<ListboxSelect>>',clasePeli.Item_ListaPelis)
    #print(lstPelis.curselection())
    

##    cadena_pelis=StringVar()
##    cadena_pelis="Capitan America","God's Not Dead"
###########################################-------------------------------------------------------------------------------------------------------------------------------    
    d=claseDic.getDic()
    
    new_d=list(d.values())
    
    dpelis=new_d[0][0]
    
    reg_pelis=list(dpelis.keys())
    
    print(reg_pelis)


    for i in range( len(reg_pelis) ):
        lstPelis.insert( END,reg_pelis[i] )
    lstPelis.grid( row=1,column=1,pady=10,padx=5 )


    #------------------Agregar Horario--------------------------------
    lblHorario=Label(frameListas,text="SELECCIONAR HORARIO",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblHorario.grid(row=0,column=2)



    
    lstHorario=Listbox(frameListas,width=30,height=10,bd=0,exportselection=0,selectbackground="#83b5b4",selectforeground="#2f2f2f",font=("Tw Cen MT Condensed",12))



    class Seleccionar_Item_Horario():
        VariableHorario=""
        def Item_ListaHorario(self,event):
            try:
                valor=str(lstHorario.get(lstHorario.curselection()))
                
                self.VariableHorario=valor

                indice=lstHorario.curselection()[0]
                print(valor,"Indice:",indice)
            except:
                print("No hay elemento seleccionado")

        def getVariable(self):
            if self.VariableHorario != "":
                return(self.VariableHorario)
            else:
                return(False)

    claseHorario = Seleccionar_Item_Horario()
    lstHorario.bind('<<ListboxSelect>>',claseHorario.Item_ListaHorario)
    

##    cadena_horario=StringVar()
##    cadena_horario="3:30","5:40"
    

    d=claseDic.getDic()

    dhorario=list( list( d.values() )[0][0].values() )[0][0]
    
    reg_horario=list(dhorario.keys())
    
    print(reg_horario)



    

    for i in range(len(reg_horario)):
        lstHorario.insert(END,reg_horario[i])
    lstHorario.grid(row=1,column=2,pady=10,padx=10)

 

    

    
    
    #------------------Agregar Asientos--------------------------------
    


    
    frameSpin=Frame(ventana_modo_usuario_v1)
    frameSpin.grid()
    frameSpin.configure(bg="#262626")
    frameSpin.place(x=700,y=250)
    
    
    lblVIP=Label(frameSpin,text="VIP",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblVIP.grid(row=0,column=0)
    varVIP=StringVar()
    varVIP.set(0)
    spnVIP=Spinbox(frameSpin,textvariable=varVIP,font=("Tw Cen MT Condensed",14))
    spnVIP.configure(from_=0,to=5,width=5)
    spnVIP.grid(row=0,column=1,pady=5,padx=10)

    lblRegular=Label(frameSpin,text="Regular",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblRegular.grid(row=1,column=0)
    varRegular=StringVar()
    varRegular.set(0)
    spnRegular=Spinbox(frameSpin,textvariable=varRegular,font=("Tw Cen MT Condensed",14))
    spnRegular.configure(from_=0,to=5,width=5)
    spnRegular.grid(row=1,column=1,pady=5,padx=10)

    lblGraderia=Label(frameSpin,text="Graderia",font=("Tw Cen MT Condensed",14),foreground="#f6edd8",bg="#262626")
    lblGraderia.grid(row=2,column=0)
    varGraderia=StringVar()
    varGraderia.set(0)
    spnGraderia=Spinbox(frameSpin,textvariable=varGraderia,font=("Tw Cen MT Condensed",14))
    spnGraderia.configure(from_=0,to=5,width=5)
    spnGraderia.grid(row=2,column=1,pady=5,padx=10)
    
    d=claseDic.getDic()
    class BotonVerificarEspacio(Button):
        def __init__(self,cine,peli,horario,entradas,parent,**kw): #variable es el texto agragado
            
            Button.__init__(self,parent,kw)
            self.Cine=cine
            self.Peli=peli
            self.Horario=horario
            self.Entradas=entradas
        def get_espacio(self):
            print(type(self.Cine))
            print(type(self.Peli))
            print(type(self.Horario))
            
            print(self.Cine)
            print(self.Peli)
            print(self.Horario)
            print(self.Entradas)
            
            try:
                f =  d[self.Cine][0][self.Peli][0][self.Horario][0] #[claseAsientos.getVariable()]
                print(f)

                matriz_asien=f['asien']
                
                disponibles=0
                d_n={}
                indices=0
                for i in range(20):#16 filas
                    for j in range(10):#10 columnas
                        if matriz_asien[i][j]==2: #2 significa disponible
                            disponibles+=1
                            d_n[indices]=(i,j)
                            indices+=1
                
                print("Cuantos Disponibles: ",len( d_n.keys() ),"Indices Disponibles: ",list( d_n.values() ) )


                
                btnConfirmarCampos.grid()
                self.grid_remove()
            except:
                messagebox.showwarning("Retro Cinema", "Incorrecto")
        
##def verificar_disponibles(self):
##        self.disponibles=0
##        d={}
##        indices=0
##        for i in range(16):#16 filas
##            for j in range(10):#10 columnas
##                if self.m_matriz[i][j]==2: #2 significa disponible
##                    self.disponibles+=1
##                    d[indices]=(i,j)
##                    indices+=1
##        
##        return(print("Cuantos Disponibles: ",len(d.keys()),"Indices Disponibles: ",list(d.values())))    

    
    
    def LlamarBoton():
        
        btnConfirmarCampos.grid_remove()
        try:
            if btnAgregarSpin.get_entradas() ==('0','0','0'):
                btnConfirmarCampos.grid()
                messagebox.showwarning("Retro Cinema", "Seleccione al menos una entrada")
            else:
                btnVerificarEspacio=BotonVerificarEspacio(lstCines.get(lstCines.curselection()[0]),lstPelis.get(lstPelis.curselection()[0]),lstHorario.get(lstHorario.curselection()[0]),btnAgregarSpin.get_entradas(),frameSpin,text="VERIFICAR",font=("Tw Cen MT Condensed",14),bg="#83b5b4",bd=0 ,foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
                btnVerificarEspacio.configure(command=btnVerificarEspacio.get_espacio)
                btnVerificarEspacio.grid(row=5,column=4,pady=5,padx=10)
                
                ventana_modo_usuario_v1.mainloop()
        except:
            btnConfirmarCampos.grid()
            messagebox.showwarning("Retro Cinema", "Seleccione Todos los campos")

    btnConfirmarCampos=Button(frameSpin,text="CONFIRMAR CAMPOS",padx=2,pady=2,bd=0,bg="#d55534",font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f")
    btnConfirmarCampos.configure(command=LlamarBoton)
    btnConfirmarCampos.grid(row=4,column=4)
    btnConfirmarCampos.grid_remove()

    
    class BotonAgregarSpin(Button):

        
        def __init__(self,vip,regular,graderia,parent,**kw): #variable es el texto agragado
            Button.__init__(self,parent,kw)
            self.VIP=vip
            self.Regular=regular
            self.Graderia=graderia

        def verificar_entradas(self):
            vip=int(self.VIP.get())
            regular=int(self.Regular.get())
            graderia=int(self.Graderia.get())
            if (vip+regular+graderia) > 5:
                print("No se puede mayor a 5")
                messagebox.showwarning("Retro Cinema", "No se puede mayor a 5\n NOTA: Solo se admiten 5 entradaspor ingreso a sys")

            elif (vip+regular+graderia) ==0:
                print("Debe Ingresar al menos una entrada")
                messagebox.showwarning("Retro Cinema", "Debe seleccionar las entradas que desea")
            else:
                
                print("VIP",self.VIP.get(),"Regular",self.Regular.get(),"Graderia",self.Graderia.get())
                tupla_entradas=(self.VIP.get(),self.Regular.get(),self.Graderia.get())
                btnConfirmarCampos.grid()
                return(print(tupla_entradas))
        def get_entradas(self):
            tupla_entradas=(self.VIP.get(),self.Regular.get(),self.Graderia.get())
            return(tupla_entradas)
           
    
    btnAgregarSpin = BotonAgregarSpin( varVIP,varRegular,varGraderia,frameSpin,text="Agregar Entradas",font=("Tw Cen MT Condensed",14),bg="#83b5b4",bd=0 ,foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
    btnAgregarSpin.configure(command=btnAgregarSpin.verificar_entradas)
    btnAgregarSpin.grid(row=3,column=1,pady=5,padx=10)
    btnAgregarSpin.get_entradas()

    

    
    btnAtras=Button(ventana_modo_usuario_v1,text="VER ASIENTOS",bg="#83b5b4",bd=0 , command=ventana_modo_usuario,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white").place(x=500,y=500)





##    class BotonAgregarTodo(Button,Diccionario,claseMatriz):
##        pass
##        
##        def __init__(self,cine,peli,horario,asientos,parent,**kw): #variable es el texto agragado
##            Button.__init__(self,parent,kw)
##            self.Cine=cine
##            self.Peli=peli
##            self.Horario=horario
##            self.Asientos=asientos
##            
##        def ValidarTodo(self):
##            print(type(self.Cine))
##            print(type(self.Peli))
##            print(type(self.Horario))
##            print(type(self.Asientos))
##            print(self.Cine)
##            print(self.Peli)
##            print(self.Horario)
##            print(self.Asientos)
##            
##           
##            if isinstance(self.Cine,bool) == True or isinstance(self.Peli,bool) == True or isinstance(self.Horario,bool) == True or isinstance(self.Asientos,bool) == True:
##                print("Falta algun campo")
##                
##                print(type(self.Cine))
##                print(type(self.Peli))
##                print(type(self.Horario))
##                print(type(self.Asientos))
##                messagebox.showwarning("Retro Cinema", "Falta campos por seleccionar\n NOTA: Recuerde confirmar el número de asientos")
##
##                self.destroy()
##                btnConfirmarCampos.grid()
##            else:
##                print("Funciona correctamente")
##                self.definir_cuantos_disponibles(self.Asientos)
##                
##                self.verificar_disponibles()
##                self.agregarDic(self.Cine,self.Peli,self.Horario,self.getMatriz())
##                #Agregar y cerrar
##                self.destroy()
##                cerrar_con_equis()
##            
##            
##            
##            
##    frameBtnConfirm=Frame(ventana_modo_usuario_v1)
##    frameBtnConfirm.grid()
##    frameBtnConfirm.configure(bg="#262626")
##    frameBtnConfirm.place(x=600,y=500)
##    
##    def LlamarBoton():
##        
##        btnConfirmarCampos.grid_remove()
##        
##        btnAgregarTodo = BotonAgregarTodo(claseCine.getVariable(),clasePeli.getVariable(),claseHorario.getVariable(),claseAsientos.getVariable(),ventana_modo_usuario_v1,text="AGREGAR TODOS",bg="#83b5b4",bd=0,font=("Tw Cen MT Condensed",14),foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white")
##        btnAgregarTodo.configure(command=btnAgregarTodo.ValidarTodo)
##        btnAgregarTodo.place(x=600,y=500)
##
##        ventana_modo_usuario_v1.mainloop()
##
##    btnConfirmarCampos=Button(frameBtnConfirm,text="CONFIRMAR CAMPOS",padx=2,pady=2,bd=0,bg="#d55534",font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f")
##    btnConfirmarCampos.configure(command=LlamarBoton)
##    btnConfirmarCampos.grid(row=0,column=0)

    

    
    def cerrar_con_equis():
        ventana_modo_usuario_v1.destroy()
        v.update()
        v.deiconify()

    ventana_modo_usuario_v1.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

##########################################
##########################################
########################################## 
##################
##########################################
##########################################
##########################################  

##########################################
##########################################
########################################## 
##################
##########################################
##########################################
##########################################    

#-----Fin Funcion modo admin----



#----------Boton para ingresar modo admin----------
btnIngresar=Button(v,text="INGRESAR",bg="#d55534",bd=0,command=ventana_modo_admin,font=("Tw Cen MT Condensed",14),foreground="white",activebackground="#d55534",activeforeground="#2f2f2f").place(x=275, y=300)

#-----Boton Modo Usuario del programa 'main'-----
imgMUsuario=PhotoImage(file="btnModoUsuario.png")
#v.attributes("-alpha", 0.5) volver formulario transparente
lblMUsuario=Label(v,image=imgMUsuario,bd=0,bg="#262626").place(x=400,y=310)
btnModo_Usuario=Button(v,text="MODO USUARIO", command=ventana_modo_usuario_v1,font=("Tw Cen MT Condensed",14),bg="#83b5b4",bd=0 ,foreground="#2f2f2f",activebackground="#83b5b4",activeforeground="white").place(x=433,y=363)




v.mainloop()
