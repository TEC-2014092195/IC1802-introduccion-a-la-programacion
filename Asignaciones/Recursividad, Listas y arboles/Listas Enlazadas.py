#Listas enlazadas
class Nodo:
    def __init__(self, carga= None, siguiente = None):
        self.carga = carga
        self.siguiente = siguiente
    def __str__(self):
        return str(self.carga)
n1 = Nodo("hola")
print(n1)
n2 = Nodo(" Como ")
print(n2)
n3 = Nodo( " estas")
print(n3)
n1.siguiente=n2
n2.siguiente=n3
n3.siguiente = Nodo( " todo bien")
print(n3.siguiente)


lista=[]

cont="s"
inicio=0
palabra=Nodo()
c_palabras=int(input("Digite cantidad palabras>"))


for i in range(c_palabras):
    
    if palabra.carga == None:
        palabra =Nodo(input("Digite palabra>"))
        lista.append(palabra)
    else:
        limite=len(lista)
        listarrr
        palabra.siguiente = input("Digite palabra>")
        
        
        
##    inicio+=1
##    else:
##        #palabra.siguiente(input("Digite palabra>"))
##        lista[inicio-1].siguiente=(input("Digite palabra>"))
##        cont=input("Desea seguir>")

for i in range(len(lista)):
    print(lista[i])

##print(n2.siguiente)




























