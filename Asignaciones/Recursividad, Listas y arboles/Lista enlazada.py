class Nodo: # en clase nodo definio el dato..y el apuntador al siguiente nodo "" sig""
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        
    def  __str__(self):#esta funcion me sirve para poder meter cualquier dato a la lista
        return str(self.dato)
        
class ListaEnlazada:#esta clase me ayuda a manejar la lista enlazada identificando la cabeza y el ultimo elemento
    def __init__(self): 
        self.cabeza =  None
        self.cola = None
        
    def agregarFinal(self, dato):  # funcion agregar al final
        nodo_nuevo = Nodo(dato)
        if self.cabeza == None: # aqui si no hay cabezera el elemento se vuelve la cabezera
            self.cabeza = nodo_nuevo
            
        if self.cola != None: # si si hay entonces se va a la cola.sig y esta apuntara a nodo nuevo
            self.cola.sig = nodo_nuevo
                    
        self.cola = nodo_nuevo

    def agregarInicio(self, dato):#aqui agregamos al inicio
        nodo_nuevo = Nodo(dato)
        if self.cabeza == None: # si no habia cabeza este se vuelve la cabeza
            self.cabeza = nodo_nuevo
        
        if self.cola != None: #cuando si habia mas datos entonces el nuevo elemento apuntara ala cabeza
            nodo_nuevo.sig = self.cabeza 
            self.cabeza =  nodo_nuevo # y la cabeza es el nuevo elemento(nodo nuevo)

    def eliminar(self, d):#para eliminar
        nodo = self.cabeza
        anterior = nodo#usamos anterior como auxiliar
        if self.cabeza.dato == d:  #si el dato a eliminar esta en la cabezera se elimina la cabeza y el cabeza.sig se vuelve la cabeza
            self.cabeza = self.cabeza.sig
        else:#si no se busca en el resto
            while nodo != None: 
                if nodo.dato == d:
                    anterior.sig = nodo.sig
                anterior = nodo
                nodo = nodo.sig


    def buscar(self, d):
        nodo = self.cabeza
        anterior = nodo#usamos anterior como auxiliar
        bandera=False
        if self.cabeza.dato == d:
            bandera = True
        else:
            while nodo != None: 
                if nodo.dato == d:
                    bandera = True
                anterior = nodo
                nodo = nodo.sig

        if bandera == True:
            print("Si se encuentra en la lista")
        else:
            print("No se encuentra en la lista")

                       
    def imprimir(self):#aqui la funcion imprimir me ayuda a imprimir mientras haya elementos en la lista
        nodo = self.cabeza
        while nodo != None: 
            print (nodo.dato)
            nodo=nodo.sig#aqui se recorre


lista = ListaEnlazada()#creo un objeto nuevo que llamo lista
salir="n"
while salir != "s":
    opc = input("----------------\na.Agregar valor\nb.Agregar al inicio de la lista\nc.Buscar elemento en la lista\nd.Impirmir lista\ne.Eliminar de la lista\nQue desea hacer:\n>")

    if opc == "a":
        
        dato = input("Digite el valor a agregar:")
        lista.agregarFinal(dato)
        
    elif opc == "b":
        
        dato = input("Digite el valor a agregar al inicio de la lista:")
        lista.agregarInicio(dato)
        
    elif opc == "c":
        
        dato = input("Digite el elemento a buscar:")
        lista.buscar(dato)
        
    elif opc == "d":
        
        lista.imprimir()
        
    elif opc == "e":
        
        dato = input("Digite el elemento que desea eliminar:")
        lista.elimimar(dato)
        
    elif opc == "s":
        
        salir="s"
        print("Programa cerrado")
        
    else:
        print("opcion incorrecta")
    
    
    
######    lista.agregarFinal(1)
######    lista.agregarFinal(2)
######    lista.agregarFinal(3)
######    lista.agregarInicio(7)
######    lista.agregarFinal(4)
######    lista.agregarFinal(5)
######    lista.agregarFinal(6)
######    lista.agregarInicio(11)
######    lista.buscar(10)
    
