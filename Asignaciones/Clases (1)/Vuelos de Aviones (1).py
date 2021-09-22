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
#                    1.    Salida de un vuelo: debe crear un objeto de vuelo con  toda la informacion que require
#                    2.    Llegada de un vuelo: debe eliminar un vuelo determinado de acuerdo con su identificador de vuelo
#                    3.    Cantidad de vuelos en el aire: debe obtener la cantidad de vuelos que se encuentran en ese momento en el aire
#                    4.    Primer vuelo: obtiene el vuelo que va a llegar de primero, aparte debe mostrar tambien el aeropuerto al que va a llegar,
#                          mas toda la informacion que posee de el
#                    5.    Vuelos al mismo aeropuerto: debe devolver, por cada aeropuerto, los vuelos que van dirigidos hacia el y los tiempos en que deben aterrizar

class Bienvenida():
    def __init__(self):
        print("a.Salida de un vuelo \nb.Llegada de un vuelo\nc.Cantidad de vuelos en el aire\nd.Primer vuelo\ne.Vuelos al mismo aeropuerto\ns.Salir")


class Vuelo(Bienvenida):
    m_vuelos=[]
    c_vuelos=[]

    def buscar_vuelos(self,idvuelo):
        
    def Aire(self,idvuelo):
        self.c_vuelos.append(idvuelo)

    def getV(self):
        print(self.c_vuelos)

    
        
            

inicio=Vuelo()
cont="s"
while cont=="s":
    idvuelo=input("Ingrese Id: ")
    inicio.Aire(idvuelo)
    inicio.getV()
    



