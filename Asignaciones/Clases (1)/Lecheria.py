class Ingresar():
    matrizCompleta=[]
    matriz=[]
    def setProductos(self,nombre,precio,stock):
        self.matriz=[]
        self.matriz.append(nombre)
        self.matriz.append(precio)
        self.matriz.append(stock)
        self.matriz.append(0)
        self.matrizCompleta.append(self.matriz)

    def getProductos(self):
        return self.matrizCompleta

class Compra(Ingresar):
    
    def setPedido(self,nombre,cantidad):
        sihay=False
        for i in range(len (self.matrizCompleta)):
            if nombre == self.matrizCompleta[i][0]:
                sihay=True
                if cantidad <= self.matrizCompleta[i][2]:
                    self.matrizCompleta[i][3]=cantidad
                    self.matrizCompleta[i][2]-=cantidad
                    return print("Usted ha comprado ",self.matrizCompleta[i][0],"la cantidad que compro fue ", self.matrizCompleta[i][3],"\nSu total a pagar es de ",self.matrizCompleta[i][1]*self.matrizCompleta[i][3])
                else:
                    print("No hay suficientes en stock")
        if sihay == False:
            print("No hay produtos con el nombre",nombre)
            

claseLecheria=Compra()
salir=""
while salir!="s":
    opc=input("\n-----Menu-----\na. Agregar al Stock\nb. Consultar Productos\nc. Cobrar Pedido a cliente\ns. Salir\nDigite la opcion\n>")
    if opc=="a":
        print ("Bienvenido, por favor agrege productos al inventario.... ")
        cicloIngreso="s"
        while cicloIngreso=="s":
            try:
                nombreProducto=input("Ingrese el nombre del producto ")
                precioProducto=int (input ("Ingrese el precio del producto "))
                stockProducto=int (input ("Ingrese la cantidad en stock "))
                claseLecheria.setProductos(nombreProducto,precioProducto,stockProducto)
                print ("")
            except:
                print("ERROR solo se permiten numeros enteros")
            cicloIngreso=input ("Desea continuar agregando productos al inventario (s/n)? ")
        print ("")
                
    elif opc=="b": 
        if claseLecheria.getProductos()== []:
            print("No hay productos agregados")
        else:
            print("Los productos son:")
            lista=claseLecheria.getProductos()
            for i in range(len(lista)):
                print(lista[i][0]," en stock: ",lista[i][2])
    elif opc=="c":
        print ("----------Bienvenido a la lecheria KP----------\nIndique que producto desea.... ")
        cicloIngreso="s"
        while cicloIngreso=="s":
            nombreProducto=input("Ingrese el producto ")
            try:
                cantidadProducto=int (input ("Ingrese la cantidad que desea "))
                claseLecheria.setPedido(nombreProducto,cantidadProducto)
            except:
                print("ERROR solo se permiten numeros enteros")
            
            cicloIngreso=input ("Desea seguir comprando? ")
    elif opc=="s":
        salir="s"
print ("Gracias por comprar con la lecheria KP! ")
    
        
        
        
    
    
