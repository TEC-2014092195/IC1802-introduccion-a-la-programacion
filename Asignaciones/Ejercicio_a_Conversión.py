salir="s"
while salir == "s":
    try:
        euros=[500,200,100,50,20,10,5,2,1]
        acum=[0,0,0,0,0,0,0,0,0]
        cantidad=int(input("Ingrese cantidad de euros que desea desglosar: "))
        if cantidad < 1:
            print("\nNo tenemos monedas o billetes de: ",cantidad," euros")
        for i in range(0,9,1):
            while cantidad >= euros[i]:
                acum[i]+=1
                cantidad-=euros[i]
                
        for i in range(0,9,1):
            if acum[i] != 0 and euros[i] >= 5:
                print("\t",acum[i]," Billetes de ",euros[i]," euros")
            elif acum[i] != 0 and euros[i] < 5:
                print("\t",acum[i]," Monedas de ",euros[i]," euros")
        salir=input("\nDesea continuar con una nueva conversión (s/n): ")
    except ValueError:
        print("El programa solo admite numeros enteros")
        salir=input("\nDesea continuar con una nueva conversión (s/n): ")
