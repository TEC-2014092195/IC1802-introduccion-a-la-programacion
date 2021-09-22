def casa_cambio():
    
    salir=""
    while salir!="s":
        nombre_mon= ["Dolares","Euros"]
        compra_moneda= [0,0]
        venta_moneda= [0,0]
        continuar= False
        while continuar != True:
            try:
                print("Digite el Tipo de Cambio")
                for i in range(0,2,1):
                    compra_moneda[i]=float(input("Compra "+nombre_mon[i]+": "))
                    venta_moneda[i]=float(input("Venta "+nombre_mon[i]+": "))
                continuar=True
            except:
                print("\nDigite una cantidad valida\n")
        compradas=[0,0]
        vendidas=[0,0]
        t_compradas=[0,0]
        t_vendidas=[0,0]
        ganancia=[0,0]
        terminar=""
        print("\n1.Comprar Dolares\t3.Comprar Euros\n2.Vender Dolares\t4.Vender Euros")

        while terminar!="n":
            try:
                opcion=input("\nDigite la opcion que desee: ")
                if opcion == "1":
                    compradas[0]+=int(input("Cuantos Dolares desea comprar: "))
                elif opcion == "2":
                    vendidas[0]+=int(input("Cuantos Dolares desea vender: "))
                elif opcion == "3":
                    compradas[1]+=int(input("Cuantos Euros desea comprar: "))
                elif opcion == "4":
                    vendidas[1]+=int(input("Cuantos Euros desea vender: "))
                else:
                    print("Opcion no es Valida\n")
                    
                terminar=input("Desea realizar otra transaccion(s/n): ")
            except:
                print("No es Valido, verifique la cantidad\n")
        print("\n")
        
        for i in range(0,2,1):
            if compradas[i]!=0:
                t_compradas[i]+=compradas[i]*compra_moneda[i]
            if vendidas[i]!=0:
                t_vendidas[i]+=vendidas[i]*venta_moneda[i]
            ganancia[i]+=t_vendidas[i]-t_compradas[i]
        for i in range(0,2,1):
            if compradas[i]!=0:
                print("Cantidad Compra en",nombre_mon[i],": ",compradas[i],"\tMonto Total de Compra en",nombre_mon[i],": ",format(t_compradas[i],'.2f'))
            if vendidas[i]!=0:
                print("Cantidad Venta en",nombre_mon[i],": ",vendidas[i],"\tMonto Total de Venta en",nombre_mon[i],":",format(t_vendidas[i],'.2f'))
            if ganancia[i]>0:
                print("La ganancia obtenida en ",nombre_mon[i],"fue: ",format(ganancia[i],'.2f')," colones")
                print("\n")
            elif ganancia[i]<0:
                print("Hubo una perdida en ",nombre_mon[i],"de: ",format(ganancia[i],'.2f')," colones")
                print("\n")
        salir=input("Desea salir del programa(s/n): ")
        
casa_cambio()
        
    
