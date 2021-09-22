class Tiempo:
    hrs=0
    mins=0
    segs=0
    bandera = True
    def setDatos(self, hrs1, mins1, segs1):
        self.hrs=hrs1
        self.mins=mins1
        self.segs=segs1

    def setResta(self, hrs1, mins1, segs1):
        
        if hrs1 <= self.hrs:
            self.hrs-=hrs1
        else:
            self.bandera=False
        if mins1 <= self.mins:
            self.mins-=mins1
        else:
            self.bandera=False
        if segs1 <= self.segs:
            self.segs-=segs1
        else:
            self.bandera=False
        
        
    def getDatos(self):
        if self.bandera == False:
            return ("No se puede")
        else:
            return (self.hrs, self.mins, self.segs)

tiempovar=Tiempo()

horas=int(input("Horas: "))
minutos=int(input("Mins: "))
segundos=int(input("Segs: "))

tiempovar.setDatos(horas,minutos,segundos)

horas=int(input("Horas: "))
minutos=int(input("Mins: "))
segundos=int(input("Segs: "))

tiempovar.setResta(horas,minutos,segundos)

print("resultado: ",tiempovar.getDatos())



        
        
