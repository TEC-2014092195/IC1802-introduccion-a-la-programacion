##Utiliza una matriz por ejemplo 3x3
## [[1, 0, 0], [5, 4, 0], [2, 8, 7]]
## donde en forma piramidal cuenta que haya ceros recorriendola
##de abajo hacia arriba
##corridas:
##        1-- [2, 8, 7]
##        2-- [5, 4, 0]
##        3-- [1, 0, 0]
##para que sea superior debe cumplir el ejemplo de arriba con ceros
##como forma de piramide


fila=[]
matriz=[]
n=int(input("long: "))
for i in range(n):
        for j in range(n):
                num=int(input("num: "))
                fila.append(num)
        matriz.append(fila)
        fila=[]

##Imprimir
        
texto=""
for i in range(n):
        for j in range(n):
                texto+=str(matriz[i][j])+"  "
        print(" ",texto)
        texto=""

##evaluar Superior e Inferior
def Inferior(n,matriz):
        m=n
        bandera=[]
        for i in range(n-1,-1,-1):
                for j in range(n-1,m-1,-1):
                        if matriz[i][j]==0:
                                bandera.append(True)
                        else:
                                bandera.append(False)
                #print(bandera)
                m-=1
        if bandera.count(False)==0:
                return True #print("Inferior")
        else:
                return False #print("No cumple con Inferior")

def Superior(n,matriz):
        m=0
        bandera=[]
        for i in range(n):
                for j in range(0,m,1):
                        if matriz[i][j]==0:
                                bandera.append(True)
                        else:
                                bandera.append(False)
                #print(bandera)
                m+=1
        if bandera.count(False)==0:
                return True #print("Superior")
        else:
                return False #print("No cumple con Superior")


if Inferior(n,matriz)==True:
        print("Inferior")
elif Superior(n,matriz)==True:
        print("Superior")
else:
        print("No cumple ninguna de las dos")


                        
        


