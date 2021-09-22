##3. Escriba un programa que busque todos los numeros divisibles por 7 pero que no son multiplos de 5, 
##entre un numero n y m, inclusives. Imprima los numeros obtenidos en lineas de 5 en 5, separados por coma
cont="s"
while cont=="s":
    try:
        n=int(input("Digite el primer número: "))
        m=int(input("Digite el segundo número: "))
        lista=[]
        if n > m:
            for i in range(m,n+1,1):
                if (i % 7) == 0 and (i % 5) != 0:
                    lista.append(i)
        else:
            for i in range(n,m+1,1):
                if (i % 7) == 0 and (i % 5) != 0:
                    lista.append(i)

        texto=""
        for i in range(len(lista)):
            if i % 5 == 0:
                texto+="\n"
            if i == len(lista)-1:
                texto+=str(lista[i])
            else:
                texto+=str(lista[i])+" , "
        print(texto)
        cont=input("Digite s para asignar otro rango: ")
    except:
        print("\nRango Invalido")
        cont=input("Digite s para asignar otro rango: ")
        print("\n")
        
