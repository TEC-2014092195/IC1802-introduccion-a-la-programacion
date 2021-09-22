salir="s"
while salir=="s":
    try:
        n=0
        total=0
        y=int(input("Ingrese la base a convertir: "))
        cantidad=input("Ingrese el número a convertir: ")
        for i in range(len(cantidad),0,-1):
            total=total+(int(cantidad[i-1])*(y**n))
            n=n+1
        print("Total: ",total)
        salir=input("\nDesea continuar con una nueva conversión (s/n): ")
    except ValueError:
        print("\nSolo se permiten números enteros")
        salir=input("\nDesea continuar con una nueva conversión (s/n): ")
