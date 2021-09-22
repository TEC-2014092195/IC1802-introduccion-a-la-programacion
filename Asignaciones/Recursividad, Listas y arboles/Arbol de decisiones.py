class Arbol:
    def __init__(self, v=None):
      self.izq = None
      self.der = None
      self.val = v

    def __str__(self):
      return "[%s,%s,%s]" %(self.izq, str(self.val), self.der)

    def isEmpty(self):
      return self.izq == self.der == self.val == None

    def insert(self):
      
          self.val = "¿Cuantas patas tiene (2 o 4)? :"
      
          self.izq = Arbol("2")
          
          self.izq.izq = Arbol("¿Tiene alas?")
          self.izq.der = Arbol("no alas")

          self.izq.izq.izq = Arbol("¿Vuela?")
          self.izq.izq.der = Arbol("no vuela")
          
          self.izq.izq.izq.izq = Arbol("es un águila")
          self.izq.izq.der.izq = Arbol("es una gallina")

          self.izq.izq.izq.der = Arbol("Especie: Mamifero")
          self.izq.izq.der.der = Arbol("Especie: Mamifero")

          self.izq.der.izq = Arbol("salvaje")
          self.izq.der.der = Arbol("domestico")
          
          self.izq.der.izq.izq = Arbol("Canguro")
          self.izq.der.izq.der = Arbol("Especie: Mamifero")
          self.izq.der.der.izq = Arbol("Mono")
          self.izq.der.izq.der = Arbol("Especie: Mamifero")
          
      
          self.der = Arbol("4")
      
          self.der.izq = Arbol("¿Tiene alas?")
          self.der.der = Arbol("no alas")

          self.der.izq.izq = Arbol("¿Vuela?")
          self.der.izq.der = Arbol("no vuela")
          
          self.der.izq.izq.izq = Arbol("es un dragón")
          self.der.izq.der.izq = Arbol("es una lagartija australiana")

          self.der.izq.izq.der = Arbol("Especie: Mamifero")
          self.der.izq.der.der = Arbol("Especie: Mamifero")

          self.der.der.izq = Arbol("salvaje")
          self.der.der.der = Arbol("domestico")
          
          self.der.der.izq.izq = Arbol("Leopardo")
          self.der.der.izq.der = Arbol("Especie: Mamifero")
          self.der.der.der.izq = Arbol("Perro")
          self.der.der.izq.der = Arbol("Especie: Mamifero")

          


    def preguntar(self):
        elec=input(self.val)
        if elec == self.izq.val:
            elec=input(self.izq.izq.val+"(s/n):")
            if elec != "s":
                elec=input(self.izq.der.izq.val+" o "+self.izq.der.der.val+"(s/d):")
                if elec == "s":
                    print(self.izq.der.izq.izq.val)
                    print(self.izq.der.izq.der.val)
                    elec="n"
                elif elec != "s":
                    print(self.izq.der.der.izq.val)
                    print(self.izq.der.izq.der.val)
                    
            
            if elec == "s":
                elec=input(self.izq.izq.izq.val+"(s/n):")
                if elec == "s":
                    print(self.izq.izq.izq.izq.val)
                    print(self.izq.izq.izq.der.val)
                if elec != "s":
                    print(self.izq.izq.der.izq.val)
                    print(self.izq.izq.der.der.val)

        if elec == self.der.val:
            elec=input(self.der.izq.val+"(s/n):")
            if elec != "s":
                elec=input(self.der.der.izq.val+" o "+self.der.der.der.val+"(s/d):")
                if elec == "s":
                    print(self.der.der.izq.izq.val)
                    print(self.der.der.izq.der.val)
                    elec="n"
                elif elec != "s":
                    print(self.der.der.der.izq.val)
                    print(self.der.der.izq.der.val)
                    
            
            if elec == "s":
                elec=input(self.der.izq.izq.val+"(s/n):")
                if elec == "s":
                    print(self.der.izq.izq.izq.val)
                    print(self.der.izq.izq.der.val)
                if elec != "s":
                    print(self.der.izq.der.izq.val)
                    print(self.der.izq.der.der.val)
            
            
        


    def imprimir(self):
         print(self.izq,self.val,self.der)


          
            





def Main():
    
    arbol.insert()
##    arbol.imprimir()
    arbol.preguntar()

                
arbol = Arbol()
salir="n"
while salir != "s":
    Main()
    salir=input("Desea salir(s/n): ")
    
