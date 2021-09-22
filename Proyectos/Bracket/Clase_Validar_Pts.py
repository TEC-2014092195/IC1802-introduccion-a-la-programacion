from tkinter import messagebox

def validar(id_bracket,maximo):
    file = open("Ganador.txt","r")
    l = file.readlines()
    #################################
    file2 = open(("Usuarios/Registrados/user_"+id_bracket+".txt"), 'r')
    l2 = file2.readlines()
    file.close()
    
    a=[]
    b=[]
    for i in range(len(l)):
        a.append( l[i].split(",") )
        b.append( l2[i].split(",") )
    
    m=""
    pts=0
    for i in range(len(a)):
        f= set(a[i]).intersection(b[i])
        f=list(f)
        f.remove("\n")
        
        if f != [] and i < (len(a)-1):
            
            ganados=len(f)
            pts+=ganados
            m+=("          Fase "+str(i+1)+"\nPuntos: "+str(ganados)+"\nEquipos acertados: \n")
            for j in range(len(f)):
                if j == (len(f)-1):
                    m+=f[j]
                else:
                    m+=f[j]+"--"
            m+="\n"
            
        elif f != [] and i < len(a):
            
            ganados=len(f)
            
            pts+=ganados
            m+=("           Final\nPuntos: "+str(ganados)+"\nEquipos acertados: \n")
            for j in range(len(f)):
                m+=f[j]
            m+="\n"

    m+="\n-------------------\n"
    m+="Puntos obtenidos: "+str(pts)+"/"+maximo

    
    messagebox.showinfo("BM",m)
    if pts == int(maximo):
        messagebox.showinfo("BM","Felicidades Ganaste el juego!!!")
