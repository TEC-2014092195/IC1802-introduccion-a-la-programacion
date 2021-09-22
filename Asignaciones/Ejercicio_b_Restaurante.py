salir="s"
while salir!="Salir":
    try:
        seguir_ordenando="s"
        cantidad_total_producto=[0,0,0]
        cantidad_producto=[0,0,0]
        producto=["Papas","Hamburguesas","Tacos"]
        total=0
        print("Bienvenido al Restaurante Rapi-Comidas\nEl menú de hoy es: \n\t1. Papas \t\tValor: 600 colones\n\t2. Hamburguesas \tValor: 1200 colones\n\t3. Tacos \t\tValor: 800")
        while seguir_ordenando=="s":
            opcion=int(input("\nPor favor digite el número de platillo: "))
            if opcion==1:
                cantidad_producto[0]=int(input("Cuantas papas desea: "))
                cantidad_total_producto[0]+=cantidad_producto[0]
                total+=(cantidad_producto[0]*600)
            elif opcion==2:
                cantidad_producto[1]=int(input("Cuantas hamburguesas desea: "))
                cantidad_total_producto[1]+=cantidad_producto[1]
                total+=(cantidad_producto[1]*1200)
            elif opcion==3:
                cantidad_producto[2]=int(input("Cuantos tacos desea: "))
                cantidad_total_producto[2]+=cantidad_producto[2]
                total+=(cantidad_producto[2]*800)
            elif opcion < 1 or opcion > 3:
                print("Esa opcion no está dentro del menú")
                break
            seguir_ordenando=input("\nDesea ordenar otro platillo (s/n): ")
        print("\n")
        for i in range(0,3,1):
            if cantidad_producto[i] != 0:
                print("\tCantidad de ",producto[i],"es de: ",cantidad_total_producto[i])
        print("\tTotal a pagar: ",total)
        salir=input("\nDigite 'Salir' para finalizar o presione 'enter' para una nueva orden: ")
    except ValueError:
        print("\nSolo se aceptan valores enteros")
        salir=input("\nDigite 'Salir' para finalizar o presione 'enter' para una nueva orden: ")
