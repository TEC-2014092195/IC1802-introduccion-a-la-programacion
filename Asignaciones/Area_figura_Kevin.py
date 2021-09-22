def circulo():
    r=int(input("Ingrese radio"))
    import math
    t=math.pi*pow(r,2)
    print("Área= ",t,"\n")

def triangulo():
    a=int(input("Ingrese Base"))
    b=int(input("Ingrese altura"))
    t=(a*b)/2
    print("Área= ",t,"\n")
def rectangulo():
    a=int(input("Ingrese Largo"))
    b=int(input("Ingrese Ancho"))
    t=a*b
    print("Área= ",t,"\n")

x=""
while x!="s":
    x=input("a. Circulo\nb.Triangulo\nc.Rectangulo\ns.Salir\nDigite la opcion: ")
    def area(opcion):
            
                if opcion=="a":
                    circulo()
                elif opcion=="b":
                    triangulo()
                elif opcion=="c":
                    rectangulo()
                elif opcion=="s":
                    print("Gracias por usar nuestro programa")
                else:
                    print("Ingrese opcion valida")
    area(x)

