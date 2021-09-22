class Humano():
    
    def hablar(self,nom):
        self.nom = nom
        print("Mi nobre es: "+ self.nom)


class IngSis(Humano):
    def __init__(self,edad):
        self.edad=edad
        print("Mi edad es: "+self.edad)
        
    def programar(self,lenguaje):
        self.lenguaje=lenguaje
        print("voy a programar en: "+ lenguaje)



pedro = IngSis("25") ##Este lo uso para el metodo __init__ (inicializar mi class IngSis)


pedro.hablar("pedro") ##pedro esta heredando de la class Humano
pedro.programar("Python") ##pedro solo usa el metodo de class IngSis NORMAL(sin heredar)
