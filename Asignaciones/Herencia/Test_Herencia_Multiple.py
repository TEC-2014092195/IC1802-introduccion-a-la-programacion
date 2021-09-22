class Humano():
    
    def nombre(self,nom):
        self.nom = nom
        print("Mi nombre es: "+ self.nom)


class IngSis(Humano):
    def __init__(self):
        print("Hola mi class inicial es IngSis")
        
    def programar(self,lenguaje):
        self.lenguaje=lenguaje
        print("Voy a programar en: "+ lenguaje)

class LicDerecho(Humano):
    def __init__(self,escuela):
        print("Lic. en derecho egresado de: "+escuela)
        
    def estudiarCaso(self,de):
        print("Resolviendo caso de: "+de)

class Estudioso(IngSis,LicDerecho): 
    pass

##-------------------------------------
##En class Estudioso:
## La prioridad de __init__ será para
## class IngSis porque está de primero
## y la otra __init__ no va a importar
##-------------------------------------

pepe = Estudioso()

pepe.nombre("Pepe")
pepe.programar("C++")
pepe.estudiarCaso("Alfonso")
