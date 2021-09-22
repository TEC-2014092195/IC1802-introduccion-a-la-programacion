class Miembro_Comunidad():
    Cedula=""
    Nombre=""
    def setCedula(self,cedula,nombre):
        self.Cedula=cedula
        self.Nombre=nombre


class Empleado(Miembro_Comunidad):
    Puesto=""
    
    def setPuesto(self,puesto):
        self.Puesto=puesto

    def getEmpleado(self):
        print(self.Cedula,self.Nombre,self.Puesto)


class Administrador(Empleado):
    Tareas=""

    def setTareas(self,tareas):
        self.Tareas=tareas

    def getTareas(self):
        print(self.Cedula,self.Nombre,self.Puesto,self.Tareas)


class Profesor(Empleado):
    Grado=""

    def setGrado(self,grado):
        self.Grado=grado

    def getGrado(self):
        print(self.Cedula,self.Nombre,self.Puesto,self.Grado)

class Prof_Admin(Profesor,Administrador):
    Funciones=""

    def setFunciones(self,funciones):
        self.Funciones=funciones

    def getFunciones(self):
        print(self.Cedula,"\n",self.Nombre,"\n",self.Puesto,"\n",self.Tareas,"\n",self.Grado,"\n",self.Funciones)
    


#--------------------------
class Estudiante(Miembro_Comunidad):
    Carrera=""
    
    def setCarrera(self,carrera):
        self.Carrera=carrera

    def getCarrera(self):
        print(self.Cedula,self.Nombre,self.Carrera)

class Alumno(Miembro_Comunidad):
    Notas=""

    def setNotas(self,notas):

        self.Notas=notas

    def getNotas(self):
        print(self.Cedula,self.Nombre,self.Notas)


profesor=Prof_Admin()

profesor.setCedula("115980484","Kevin Hernández")
profesor.setPuesto("Profe Compu")
profesor.setTareas("Actualizar todos los días")
profesor.setGrado("Ingeniero")
profesor.setFunciones("Verificar todo este bien")
profesor.getFunciones()
