##4. Encryptador:  Julio Cesar enviaba mensajes a sus legiones encriptando los mensajes mediante el siguiente algoritmo:
##  Se escogia un numero n como clave, y se sumaba a cada letra en el alfabeto n posiciones.  
##Asi la clave escogida fuese de 0 a 5, la a pasaria a ser la f, mientras que la f seria la k.  
##Se debe poder encryptar y desencriptar.  La clave puede ser numeros negativos
cont="s"
while cont=="s":
    try:
        alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]##26 letras
        l_pal=[]
        pos=0
        
        opcion=""
        opcion=input("\tDigite e para encriptar\n\tDigite d para desencriptar\n¿Cuál opcion desea?:")
        if opcion=="e":
            n=int(input("Ingrese número de clave: "))
            pos=n%26
            palabra=input("Digite la palabra que desea encriptar: ")
            
            for i in range(len(palabra)):##Almacenar palabra
                l_pal.append(palabra[i])
            
            for i in range(len(palabra)):
                for j in range(len(alfabeto)):
                    if palabra[i]==alfabeto[j]:
                        if (j+pos)<26:
                            l_pal[i]=alfabeto[j+pos]
                        else:
                            limite=0
                            limite=(j+pos)-25
                            l_pal[i]=alfabeto[limite-1]
            palabra=""
            for i in range(len(l_pal)):
                palabra+=l_pal[i]

            print("La palabra encriptada es: "+palabra)
        elif opcion=="d":
            n=int(input("Ingrese número de clave: "))
            pos=n%26
            palabra=input("Digite la palabra que desea desencriptar: ")
            for i in range(len(palabra)):
                l_pal.append(palabra[i])
            
            for i in range(len(palabra)):
                for j in range(len(alfabeto)):
                    if palabra[i]==alfabeto[j]:
                        if (j-pos)>=0: ##
                            l_pal[i]=alfabeto[j-pos]
                        else:
                            limite=0
                            limite=(j-pos)+25
                            l_pal[i]=alfabeto[limite+1]
            palabra=""
            for i in range(len(l_pal)):
                palabra+=l_pal[i]

            print("La palabra desencriptada es: "+palabra)
        
        cont=input("Digite s para continuar: ")
    except:
        print("\nIngreso Invalido, intente de nuevo")
        cont=input("Digite s para continuar: ")




