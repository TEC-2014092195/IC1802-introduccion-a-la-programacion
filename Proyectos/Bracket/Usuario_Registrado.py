from tkinter import *
from tkinter import messagebox
import Clase_Usuario_Registrado
import Clase_Validar_Pts

class ClaseUsuarioRegistrado():
    def VentanaUsuarioRegistrado(v_main,nom_usuario,id_bracket):
        v_ganador=Toplevel()

        v_ganador.wm_state('zoomed')
        v_ganador.resizable(0,0)
        v_ganador.title("Bracket de Torneos")
        v_ganador.configure(bg="#4faa2b")


        v_ganador.title("Bracket Mundial")


        frm=Frame(v_ganador)
        frm.grid()
        frm.configure(bg="#4faa2b")
        frm.place(relx=.5,rely=.5,anchor="c")

        btn={}
        btn2={}
        btn3={}
        btn4={}
        btn5={}
        btn6={}
        g=('GrupoA','GrupoB','GrupoC','GrupoD','GrupoE','GrupoF',
                   'GrupoG','GrupoH','GrupoI','GrupoJ','GrupoK','GrupoL','GrupoM','GrupoN')

        c_grupos=""
        file = open("Template.txt","r")
        c_grupos = file.readlines()
        c_grupos = len(c_grupos)
        file.close()

        can_grupos=c_grupos #Cantidad de equipos heredado

        columnas=can_grupos+3
        if can_grupos == 4 or can_grupos == 2:
            columnas=can_grupos+4
        c=0
        f=0
        fb=0
        f2=0
        for i in range(can_grupos):

            if i < can_grupos/2:
                lbl=Label( frm,text=(g[i]) )
                lbl.configure(fg="white",bg="#4faa2b")
                lbl.grid(pady=10)
                f+=1
                for j in range(4):
                    btn[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                    btn[ "btn"+str(fb) ].configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                    btn[ "btn"+str(fb) ].grid(row=f,column=0,pady=1,padx=1)
                    f+=1
                    fb+=1
            else:
                lbl=Label( frm,text=(g[i]) )
                lbl.configure(fg="white",bg="#4faa2b")
                lbl.grid(row=f2,column=columnas,pady=10)
                f2+=1
                for j in range(4):
                    btn[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                    btn[ "btn"+str(fb) ].configure(bg="#0b2532",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                    btn[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1)
                    f2+=1
                    fb+=1

        #######################################
        def Fase_1():
            can=can_grupos//2
            c=0
            f=0
            fb=0
            f2=0
            for i in range(can):
                
                if i < can//2:
                    f+=1
                    for j in range(4):
                        if j==0:
                            f+=1
                        if j==0 and i==1:
                            f+=1
                        if j < 2:
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f,column=1,pady=1,padx=1)
                            f+=1
                            fb+=1
                            
                        elif j==2:
                            f+=3
                            
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f,column=1,pady=1,padx=1)
                            f+=1
                            fb+=1
                        else:
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f,column=1,pady=1,padx=1)
                            f+=1
                            fb+=1
                else:
                    f2+=1
                    for j in range(4):
                        if j==0:
                            f2+=1
                            
                        if j==0 and i==3:
                            f2+=1
                        
                        if j < 2:
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f2,column=columnas-1,pady=1,padx=1)
                            f2+=1
                            fb+=1
                            
                        elif j==2:
                            f2+=3
                            
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f2,column=columnas-1,pady=1,padx=1)
                            f2+=1
                            fb+=1
                        else:
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f2,column=columnas-1,pady=1,padx=1)
                            f2+=1
                            fb+=1

        def Fase_2():
            can=can_grupos//2
            can=can//2
            columnas=can_grupos+3
            columnas=columnas-2
            c=2
            f=0
            fb=0
            f2=0

            for i in range(can):
                
                if i < can//2:
                    f+=1
                    for j in range(4):
                        
                        if j < 2:
                            f+=1
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1,rowspan=2)
                            f+=4
                            fb+=1
                            
                        elif j==2:
                            f+=1
                            
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1,rowspan=2)
                            f+=5
                            fb+=1
                        else:
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1,rowspan=2)
                            f+=1
                            fb+=1
                else:
                    f2+=1
                    for j in range(4):
                        
                        if j < 2:
                            f2+=1
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1,rowspan=2)
                            f2+=4
                            fb+=1
                            
                        elif j==2:
                            f2+=1
                            
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1,rowspan=2)
                            f2+=5
                            fb+=1
                        else:
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1,rowspan=2)
                            f2+=1
                            fb+=1

        def Fase_3():
            can=can_grupos//2
            can=can//2
            can=can//2
            columnas=can_grupos+3
            columnas=columnas-3
            c=3
            f=0
            fb=0
            f2=0

            for i in range(can):
                
                    f+=5
                    for j in range(4):
                        
                        if j < 2:
                            btn4[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn4[ "btn"+str(fb) ].configure(bg="#0a4c2c",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn4[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1)
                            f+=10
                            fb+=1
                            
                        elif j==2:
                            f2+=5
                            
                            btn4[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn4[ "btn"+str(fb) ].configure(bg="#0a4c2c",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn4[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1)
                            f2+=10
                            fb+=1
                        else:
                            btn4[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn4[ "btn"+str(fb) ].configure(bg="#0a4c2c",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn4[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1)
                            fb+=1

        def Fase_4():
            can=can_grupos//2
            can=can//2
            can=can//2
            columnas=can_grupos+3 #NO Cambiar
            columnas=columnas-4
            c=4
            f=0
            fb=0
            f2=0

            for i in range(can):
                
                    f+=10
                    for j in range(4):
                        
                        if j < 2:
                            btn5[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn5[ "btn"+str(fb) ].configure(bg="#da3800",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn5[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1)                    
                            c=columnas
                            fb+=1
                            

        def Fase_5():
            can=can_grupos//2
            can=can//2
            can=can//2
            columnas=can_grupos+3 #NO Cambiar
            columnas=columnas-4
            c=5
            f=0
            fb=0
            f2=0
            
            for i in range(can):
                
                    f+=10
                    for j in range(4):
                        
                        if j < 1:
                            btn6[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn6[ "btn"+str(fb) ].configure(bg="white",bd=0,relief=FLAT,fg="#121f0a",font=("Calibri",11),width=13)
                            btn6[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1)                    
                            fb+=1
        ############################################################################

        def Fase_2_4():
            can=can_grupos//2
            can=can//2
            columnas=can_grupos+4
            columnas=columnas-2
            c=2
            f=0
            fb=0
            f2=0

            for i in range(can):
                    f+=1
                    f2+=1
                    for j in range(4):
                        
                        if j < 2:
                            f+=1
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1,rowspan=2)
                            f+=4
                            fb+=1
                            
                        elif j==2:
                            f2+=1
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1,rowspan=2)
                            f2+=5
                            fb+=1
                        else:
                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f2,column=columnas,pady=1,padx=1,rowspan=2)
                            f2+=1
                            fb+=1

        def Fase_3_4():
            can=can_grupos//2
            can=can//2
            columnas=can_grupos+4

            columnas=columnas-3

            c=3
            f=0
            fb=0
            f2=0

            for i in range(can):
                    f+=5
                    for j in range(4):
                        
                        if j < 2:
                            print(c)
                            btn4[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn4[ "btn"+str(fb) ].configure(bg="#0a4c2c",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn4[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1)

                            c=columnas
                            
                            fb+=1
                            

        def Fase_4_4():
            can=can_grupos//2
            can=can//2
            columnas=can_grupos+4

            c=4
            f=0
            fb=0

            for i in range(can):
                    f+=5
                    for j in range(4):
                        
                        if j < 1:
                            btn5[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn5[ "btn"+str(fb) ].configure(bg="white",bd=0,relief=FLAT,fg="#121f0a",font=("Calibri",11),width=13)
                            btn5[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1)

        ########################################################################################

        def Fase_1_2():
            can=can_grupos//2
            c=1
            f=0
            fb=0
            f2=0
            for i in range(can):
                    f+=2
                    f2+=2
                    for j in range(4):
                        
                        
                        if j < 2:
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f,column=c,pady=1,padx=1)
                            f+=1
                            fb+=1
                            
                        elif j==2:
                            
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f2,column=columnas-1,pady=1,padx=1)
                            f2+=1
                            fb+=1
                        else:
                            btn2[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn2[ "btn"+str(fb) ].configure(bg="#f8b101",bd=0,relief=FLAT,fg="#592d12",font=("Calibri",11),width=13)
                            btn2[ "btn"+str(fb) ].grid(row=f2,column=columnas-1,pady=1,padx=1)
                            f2+=1
                            fb+=1

        def Fase_2_2():
            can=can_grupos//2
            columnas=can_grupos+4
            columnas=columnas-2
            c=2
            f=0
            fb=0
            f2=0

            for i in range(can):
                
                    f2+=2
                    for j in range(4):
                        
                        if j < 2:

                            btn3[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn3[ "btn"+str(fb) ].configure(bg="#692a37",bd=0,relief=FLAT,fg="white",font=("Calibri",11),width=13)
                            btn3[ "btn"+str(fb) ].grid(row=f2,column=c,pady=1,padx=1,rowspan=2)

                            c=columnas
                            fb+=1
                            

        def Fase_3_2():
            can=can_grupos//2
            columnas=can_grupos+4
            columnas=columnas-3
            c=3
            f=0
            fb=0
            f2=0
            for i in range(can):
                
                    f2+=2
                    for j in range(4):
                        
                        if j < 1:
                            btn4[ "btn"+str(fb) ] = Button(frm,text="btn"+str(fb))
                            btn4[ "btn"+str(fb) ].configure(bg="white",bd=0,relief=FLAT,fg="#121f0a",font=("Calibri",11),width=13)
                            btn4[ "btn"+str(fb) ].grid(row=f2,column=c,pady=1,padx=1,rowspan=2)
                            

        ######################################################
        ######################################################
        ######################################################
        

        Clase_Usuario_Registrado.Grupos.LlenarGrupos(btn)


        if can_grupos == 8:
            Fase_1()
            Fase_2()
            Fase_3()
            Fase_4()
            Fase_5()
            Clase_Usuario_Registrado.Grupos.LlenarBotones8(btn2,btn3,btn4,btn5,btn6,id_bracket,v_ganador,v_main)

            maximo="31"
            Clase_Validar_Pts.validar(id_bracket,maximo)
        elif can_grupos== 4:
            Fase_1()
            Fase_2_4()
            Fase_3_4()
            Fase_4_4()
            
            Clase_Usuario_Registrado.Grupos.LlenarBotones4(btn2,btn3,btn4,btn5,id_bracket,v_ganador,v_main)

            maximo="15"
            Clase_Validar_Pts.validar(id_bracket,maximo)
        elif can_grupos == 2:
            Fase_1_2()
            Fase_2_2()
            Fase_3_2()
            
            Clase_Usuario_Registrado.Grupos.LlenarBotones2(btn,btn2,btn3,btn4,id_bracket,v_ganador,v_main)


            maximo="7"
            Clase_Validar_Pts.validar(id_bracket,maximo)
            
            



        #Frame nombre de usuario
        frmUsuario=Frame(v_ganador)
        frmUsuario.grid()
        frmUsuario.configure(bg="#186518")
        frmUsuario.place(in_=v_ganador,relx=.5,y=0,anchor="n")
        
        lbluser=Label(frmUsuario,text="Nombre de Usuario",bg="#186518",fg="white")
        lbluser.grid(row=0,column=0)
        lblnom=Label(frmUsuario,text=nom_usuario,bg="#186518",fg="white")
        lblnom.grid(row=1,column=0)

        def cerrar_con_equis():
            v_ganador.destroy()
            v_main.update()
            v_main.deiconify()
                
        v_ganador.protocol('WM_DELETE_WINDOW', cerrar_con_equis)

        v_ganador.mainloop()
