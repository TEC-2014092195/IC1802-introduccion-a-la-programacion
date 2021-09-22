# 2. Para calcular la nota final en un curso se tienen los siguientes valores: 1er examen 25%, 
# 2do examen 35%, 3er examen 40%. Pida las calificaciones de n alumnos del curso, ingreselos en una matriz, 
# calcule la nota final de cada estudiante, y la media de cada evaluacion

cont="s"
while cont == "s":
    try:
        alumnos=[]
        c_alumnos=[]
        porcentaje=[25,35,40]
        can_alum=0
        confirm="s"
        nota=0
        nota_final=0
        media_nota=0
        while confirm == "s":
            
            print("Ingrese las notas del alumno",(len(alumnos)+1))
            for i in range(3):
                nota=int(input("Ingrese nota del "+str(i+1)+" examen: "))
                media_nota+=nota
                nota=((nota*porcentaje[i]/100))
                c_alumnos.append(nota)
            c_alumnos.append(media_nota)
            alumnos.append(c_alumnos)
            confirm=input("Digite s para añadir otro estudiante: ")
            c_alumnos=[]
            media_nota=0

        media_nota=0
        for i in range(len(alumnos)):
            for j in range(len(alumnos[i])-1):
                nota_final+=alumnos[i][j]
            media_nota=alumnos[i][3]//(len(alumnos[i])-1)
            print("Notas del alumno "+str(i+1))
            print("Nota final: ",format(nota_final,'.2f')," media: ",format(media_nota,'.2f'))
            nota_final=0
        cont=input("Desea reiniciar el programa (s/n): ")
    except:
        print("Entrada Invalida")
        cont=input("Desea reiniciar el programa (s/n): ")
            



