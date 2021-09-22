#---------------Burbuja
def burbuja(lista):
    if lista == []:
        return []
    else:
        return orden1(lista)


def orden1(lista,i=0):
    if i == len(lista):
        return lista
    
    if i < len(lista):
        lista = orden2(lista,i)
        return orden1(lista,i+1)
    

def orden2(lista,i,j=0):
    if j == len(lista):
        return lista
    if j < len(lista):
        if lista[i] < lista[j]:
            temp=lista[i]
            lista[i]=lista[j]
            lista[j]=temp
        return orden2(lista,i,j+1)
#--------------QuickSort
    
def quicksort(lista):
    
    if lista == []: 
        return []
    else:
        pivote = lista[0]
        menor, igual, mayor = ordenq(lista[1:], [], [pivote], [])
        return quicksort(menor) + igual + quicksort(mayor)

def ordenq(lista, menor, igual, mayor):
    if lista == []:
        return (menor, igual, mayor)
    else:
        cabeza = lista[0]
        if cabeza < igual[0]: # igual en la primera corrida es pivote
            return ordenq(lista[1:], menor + [cabeza], igual, mayor)
        elif cabeza > igual[0]:
            return ordenq(lista[1:], menor, igual, mayor + [cabeza])
        else:
            return ordenq(lista[1:], menor, igual + [cabeza], mayor)






s="n"
lista = []
while s!="s":
    opc=input("\n\n---Menu---\na.Ingresar lista\nb.Orden Burbuja\nc.Orden Quick Sort\ns.Salir\nDigite la opcion: ")

    if opc == "a":
        lista = []
        con="s"
        while con == "s":
            try:
                num=int(input("\nDigite un valor: "))
                lista.append(num)
                con=input("Desea añadir más(s/n): ")
            except:
                print("Valor incorrecto")
    elif opc == "b":
        print( burbuja(lista) )
    elif opc == "c":
        print( quicksort(lista) )
    elif opc == "s":
        s="s"
    else:
        print("La opcion no es válida\n")
            
