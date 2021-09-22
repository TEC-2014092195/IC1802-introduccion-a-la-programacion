n = 3

contrasena = "pass"
s=False
while n != 0 and s==False:
    ingresar= input("Ingrese contraseña: ")
    def validacion(ingresar):
        fondos = 10000
        while ingresar == contrasena:
            tipo=input("1. Para Retiro \n2. Para Consulta\n0. Para Salir\nQue desea hacer?")
            if tipo=="1":
                cantidad=int(input("Ingrese cantidad: "))
                if cantidad < fondos:
                    autorizar=input("Seguro del retiro? s/n: ")
                    if autorizar == "s":
                        fondos-=cantidad
                        print("Transacción procesada:",cantidad)
                else:
                    
                    print("Fondos insuficientes")
            elif tipo=="2":
                print("Su fondo es de:",fondos)
            elif tipo=="0":
                ingresar=""
                print("Gracias por visitar nuestro banco")
                
            else:
                print("Opcion incorrecta")
    if ingresar==contrasena:
        validacion(ingresar)
        s= True
    else:
        n=n-1
        if n==0:
            print("Contraseña Incorrecta")
        else:
            print("Contraseña Incorrecta\nQuedan ",n," intentos")
print("Expulsar tarjeta")
