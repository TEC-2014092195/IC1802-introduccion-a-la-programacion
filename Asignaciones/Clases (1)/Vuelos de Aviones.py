#Un centro que controla los vuelos de los aviones debe conocer la cantidad de vuelos que posee en cada momento,
#a parte del primer vuelo en llegar y los vuelos por aeropuesto que todavia faltan por aterrizar: por lo que se
#require de las siguientes funciones e informacion:
#
#Informacion:
#    
#                    1.    Vuelo en el aire, debe tener identificador de vuelo, tiempo de salida, tiempo de llegada,
#                          aeropuerto de salida y de llegada, ademas del avion que realiza el vuelo
#                    2.    Aeropuertos: deben tener nombre y pais en que se encuentran
#                    3.    Aviones: deben tener la capacidad del avion y tipo de avion
#Funciones:
#                Cree un menu que permita:
#                    a.    Salida de un vuelo: debe crear un objeto de vuelo con  toda la informacion que require
#                    b.    Llegada de un vuelo: debe eliminar un vuelo determinado de acuerdo con su identificador de vuelo
#                    c.    Cantidad de vuelos en el aire: debe obtener la cantidad de vuelos que se encuentran en ese momento en el aire
#                    d.    Primer vuelo: obtiene el vuelo que va a llegar de primero, aparte debe mostrar tambien el aeropuerto al que va a llegar,
#                          mas toda la informacion que posee de el
#                    e.    Vuelos al mismo aeropuerto: debe devolver, por cada aeropuerto, los vuelos que van dirigidos hacia el y los tiempos en que deben aterrizar

class Tiempo():
    pass

    def validar_time(self,v_time):
        if len(v_time)==5:
            for i in range(len(v_time)):
                if i < 2:
                    try:
                        int(v_time[i])
                    except:
                        return False #print("HOras Invalidas")
                elif i == 2:
                    if not v_time[i]==":":
                        return False #print("Faltan dos puntos")
                elif i > 2:
                    try:
                        int(v_time[i])
                    except:
                        return False #print("Min Invalidas")
        else:
            return False #print("len invalido")


            
##-----------------------------------------------------------------------
class Vuelo(Tiempo):
    pass ##Para heredar de Tiempo

    vuelos=[]
    m_vuelos=[]
    texto=["Id de Vuelo: ","Tiempo de Salida: ","Tiempo de Llegada: "
           ,"Aeropuerto de Salida: ","Aeropuerto de Llegada: "
           ,"Nombre del Avión: ","Nombre del Aeropuerto: "
           ,"País del Aeropuerto: ","Capacidad del Avión: "
           ,"Tipo de Avión: "] ##Len es 10
    def menu(self):
        print("---------------Menú---------------\na.Salida de un vuelo \nb.Llegada de un vuelo\nc.Cantidad de vuelos en el aire\nd.Primer vuelo\ne.Vuelos al mismo aeropuerto\ns.Salir")
    def validarId(self,idvuelo):
        for i in range(len(self.m_vuelos)):
            for j in range(len(self.m_vuelos[i])):
                if idvuelo==self.m_vuelos[i][0]:
                    return True #Si encontro uno duplicado
                    break
                else:
                    return False
    
    def verificar_lista(self):
        if not self.m_vuelos:
            return False
        else:
            return True



        
    def crearVuelos(self):
        idvuelo=input("Ingese Id del Vuelo \n> ")
        while self.validarId(idvuelo)==True:
            print("Id Duplicado, Ingrese de nuevo")
            idvuelo=input("Ingese Id del Vuelo \n> ")
        self.vuelos.append(idvuelo)
        
                
        
        
        time_salida=input("Tiempo de Salida (formato: 24h)\n> ")
        while self.validar_time(time_salida)==False: ##funcion heredad de class Tiempo
            print("Formato Incorrecto\nNota:\n\t-extrictamente  utilice los dos puntos\n\t-recuerde el formato 24h (e.j 05:40)\n")
            time_salida=input("Tiempo de Salida (formato: 24h)\n> ")
        
        self.acu_time(time_salida)
        time_llegada=input("Tiempo de Llegada (formato: 24h)\n> ")
        while self.validar_time(time_llegada)==False:
           print("Formato Incorrecto\nNota:\n\t-extrictamente  utilice los dos puntos\n\t-recuerde el formato 24h (e.j 05:40)\n")
           time_llegada=input("Tiempo de Llegada (formato: 24h)\n> ")
        self.acu_time(time_llegada)
        
        self.vuelos.append(input("Aeropuerto de Salida \n> "))
        self.vuelos.append(input("Aeropuerto de Llegada \n> "))
        self.vuelos.append(input("Nombre del avión \n> "))
        self.vuelos.append(input("Nombre del Aeropuerto donde se encuentra \n> "))
        self.vuelos.append(input("País del Aeropuerto \n> "))
        self.vuelos.append(input("Capacidad del Avión \n> "))
        self.vuelos.append(input("Tipo de Avión \n> "))
        
        self.m_vuelos.append(self.vuelos)
        self.vuelos=[]

        
    
    def eliminarVuelos(self):
        bandera=False
        
        while bandera==False:
            idvuelo=input("ID \n> ")
            for i in range(len(self.m_vuelos)):
                for j in range(len(self.m_vuelos[i])):
                    if idvuelo==self.m_vuelos[i][0]:
                        self.m_vuelos.pop(i)
                        print("Se elimino corectamente") 
                        bandera=True
                        break
            if bandera==False:
                print("Id no existe")
            
            
    def acu_time(self,v_time):
        temp=""
        for i in range(len(v_time)):
            if i < 2:
                temp+=v_time[i]
            elif i == 2:
                self.vuelos.append(int(temp))
                temp=""
            elif i > 2:
                temp+=v_time[i]
        self.vuelos.append(int(temp))

    def primer_Vuelo(self):
        menor_hrs=0
        menor_min=0
        temp=0
        for i in range(len(self.m_vuelos)):
            for j in range(len(self.m_vuelos[i])):
                if i == 0:
                    temp=self.m_vuelos[i][3]
                if self.m_vuelos[i][3] < temp:
                    temp=self.m_vuelos[i][3]
        menor_hrs=temp
        temp=self.m_vuelos[0][4]
        indice=0
        for i in range(len(self.m_vuelos)):
            for j in range(len(self.m_vuelos[i])):
                if self.m_vuelos[i][3]==menor_hrs:
                    if self.m_vuelos[i][4] < temp:
                        temp=self.m_vuelos[i][4]
                        indice=i
        menor_min=temp
        
##        print(menor_hrs)
##        print(menor_min)
        print("El primer Vuelo en llegar es: \nEl vuelo con Id: ",self.m_vuelos[indice][0]," que llega a las: ",self.m_vuelos[indice][3],":",self.m_vuelos[indice][4])
        self.imprimir_primer_Vuelo(indice)


    def imprimir_primer_Vuelo(self,indice):
            acu=""
            for j in range(len(self.m_vuelos[indice])):
                if j==0:
                    print(self.texto[j]+str(self.m_vuelos[indice][j]))
                elif j == 1:
                    acu+=str(self.m_vuelos[indice][j])+":"
                elif j==2:
                    acu+=str(self.m_vuelos[indice][j])
                elif j == 3:
                    print(self.texto[j-2]+acu)
                    acu=""
                    acu+=str(self.m_vuelos[indice][j])+":"
                elif j ==4:
                    acu+=str(self.m_vuelos[indice][j])
                    print(self.texto[j-2]+acu)
                else:
                    print(self.texto[j-2]+str(self.m_vuelos[indice][j]))

    def getAeropuerto(self):

        elementos=[]

        for i in range(len(self.m_vuelos)):
            elementos.append(i)


        for i in range(len(self.m_vuelos)):
            acu=0
            for j in range(len(self.m_vuelos)):
                if self.m_vuelos[i][6] == self.m_vuelos[j][6] and elementos.count(j) == 1:
                    elementos.remove(j)
                    
                    if acu<1:
                        acu+=1
                        nom_puerto=self.m_vuelos[i][6]
                        print("El Aeropuerto ",nom_puerto,"\nRecibe el Vuelo con el Id: ",self.m_vuelos[j][0]," y su hora de aterrizaje es: ",self.m_vuelos[j][3],":",self.m_vuelos[j][4])
                    else:
                        print("Recibe el Vuelo con el Id: ",self.m_vuelos[j][0]," y su hora de aterrizaje es: ",self.m_vuelos[j][3],":",self.m_vuelos[j][4])
        
    def getVuelos(self):
        print(self.m_vuelos)
        acu=""
        for i in range(len(self.m_vuelos)):
            acu=""
            for j in range(len(self.m_vuelos[i])):
                
                if j==0:
                    print(self.texto[j]+str(self.m_vuelos[i][j]))
                elif j == 1:
                    acu+=str(self.m_vuelos[i][j])+":"
                elif j==2:
                    acu+=str(self.m_vuelos[i][j])
                elif j == 3:
                    print(self.texto[j-2]+acu)
                    acu=""
                    acu+=str(self.m_vuelos[i][j])+":"
                elif j ==4:
                    acu+=str(self.m_vuelos[i][j])
                    print(self.texto[j-2]+acu)
                else:
                    print(self.texto[j-2]+str(self.m_vuelos[i][j]))

                    
                
    def getVuelos_Aire(self):
        print("La cantidad de vuelos en el aire es: "+str(len(self.m_vuelos)))

vuelo=Vuelo()

cont="s"
while cont=="s":
    vuelo.menu()
    opc=input("Digite opcion que desee\n> ")
    if opc=="a":
        vuelo.crearVuelos()
        print("Vuelo se almacenó correctamente.")##vuelo.getVuelos()

        #cont="s" 
    elif opc=="b":
        if vuelo.verificar_lista()==True:            
            vuelo.eliminarVuelos()
            ##vuelo.getVuelos()
            #cont="s" 
        else:
            print("No hay elemento en la lista, Ingrese al menos un elemento")
            #cont="s" 
    elif opc=="c":

        if vuelo.verificar_lista()==True:            
            vuelo.getVuelos_Aire()
            #cont="s" 
        else:
            print("No hay elemento en la lista, Ingrese al menos un elemento")
            #cont="s" 
    elif opc=="d":
        if vuelo.verificar_lista()==True:            
            vuelo.primer_Vuelo()
            ##vuelo.getVuelos()
            #cont="s" 
        else:
            print("No hay elemento en la lista, Ingrese al menos un elemento")
            #cont="s" 
    elif opc=="e":
        if vuelo.verificar_lista()==True: 
            vuelo.getAeropuerto()
            #cont="s" 
        else:
            print("No hay elemento en la lista, Ingrese al menos un elemento")
            #cont="s" 
    elif opc=="s":
        print("Gracias por utilizar nuestro software")
        cont="n"
    else:
        print("La opción no se encuentra en el menú\nPor Favor ingrese una opcion valida")
        

        

        

    




