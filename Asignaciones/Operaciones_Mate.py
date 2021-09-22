def suma(a,b):
    t=a+b
    print("Resultado Suma= ",t,"\n")
def resta(a,b):
    t=a-b
    print("Resultado Resta= ",t,"\n")
def multiplicacion(a,b):
    t=a*b
    print("Resultado Multiplicación= ",t,"\n")
def division(a,b):
    t=a/b
    print("Resultado División= ",t,"\n")
def potencia(a,b):
    t=pow(a,b)
    print("Resultado Potencia= ",t,"\n")
x=""
while x!="s":
    a=int(input("Ingrese el primer digito"))
    b=int(input("Ingrese el segundo digito"))
    x=input("a. Sumar\nb.Restar\nc.Multiplicar\nd.Dividir\ne.Potencia\ns.Salir\nDigite la opcion: ")
    
    def area(opcion):
        if opcion=="a":
            suma(a,b)
        elif opcion=="b":
            resta(a,b)
        elif opcion=="c":
            multiplicacion(a,b)
        elif opcion=="d":
            division(a,b)
        elif opcion=="e":
            potencia(a,b)
        elif opcion=="s":
            print("Gracias por usar nuestro programa")
        else:
            print("Ingrese opcion valida")
    area(x)
