class Arbol:
     def __init__(self, v=None):
          self.izq = None
          self.der = None
          self.val = v

     def __str__(self):
          return "[%s,%s,%s]" %(self.izq, str(self.val), self.der)

     def isEmpty(self):
          return self.izq == self.der == self.val == None

     def insert(self, val):
          if self.isEmpty():
               self.val = val
          elif val <  self.val:
               if self.izq is None:
                    self.izq = Arbol(val)
               else:
                    self.izq.insert(val)
          else:
               if self.der is None:
                    self.der = Arbol(val)
               else:
                    self.der.insert(val)

     def buscar(self,val):
          if val == self.val:
               return True
          elif self.izq != None:
               if self.izq.buscar(val):
                    return True
          if self.der != None:
               if self.der.buscar(val):
                    return True
          return False
     
     def borrar(self,val):
          if self.val == val:
               if self.izq == None or self.der == None or self.izq.isEmpty() or self.der.isEmpty():
                    self.val = None
                    
               elif self.der == None or self.der.isEmpty():
                    self.val = self.izq.val
                    if self.izq.der != None:
                         self.der = self.izq.der
                    if self.izq.izq != None:
                         self.izq = self.izq.izq
                   
                    
               elif self.izq == None or self.izq.isEmpty():
                    self.val = self.der.val
                    if self.der.izq != None:
                         self.izq = self.der.izq
                    if self.der.der != None:
                         self.der = self.der.der
               
               else:
                    if self.der.izq==None or self.der.izq.isEmpty():
                         self.val = self.der.val
                         self.der=self.der.der
                    else:
                         self.val=self.der.izq.val
                         self.der.izq.borrar(val)
               return True 
          elif self.izq != None and self.izq.borrar(val):
               return True
          if self.der!=None:
               return self.der.borrar(val)
          return False


def Main():
     opcion=int(input("-----Menu----- \n1 - Insertar Variable\n2 - Buscar y Eliminar\n3 - Salir\n"))
     
     if opcion == 1:
               variable = input("Digite la variable:\n")
               arbol.insert(variable)
                
     elif opcion == 2:
               variable = input("Digite la variable que desee buscar: ")
               if arbol.buscar(variable):
                    print("Sí se encuentra en el árbol")            
                    eliminar = input("Desea eliminar la variable? (s/n): ")
                    if eliminar == "s":
                         arbol.borrar(variable)
                         print("Eliminado")
               else:
                         print("No está tal variable")

     elif opcion == 3:
               return

     else:
                print("No se encuentra la opcion en el menu")
     Main()
arbol = Arbol()     
Main()

     

          
               
               








          

