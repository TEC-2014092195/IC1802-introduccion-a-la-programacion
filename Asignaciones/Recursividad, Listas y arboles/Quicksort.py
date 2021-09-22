def quicksort(lista):
    if lista == []:
        return []
    else:
    
        pivote = lista[0]

        menor, igual, mayor = ordenar1(lista[1:],[],[pivote],[])

        return quicksort(menor) + igual + quicksort(mayor)

def ordenar1(lista,menor,igual,mayor):
    if lista == []:
        return (menor,igual,mayor)
    else:
        cabeza = lista[0]
        if cabeza < igual[0]:
            return ordenar1(lista[1:], menor + [cabeza] , igual, mayor)
        elif cabeza > igual[0]:
            return ordenar1(lista[1:], menor, igual, mayor + [cabeza])
        else:
            return ordenar1(lista[1:], menor, igual + [cabeza], mayor)

lista=[6,-1,56,3,3,32,2,3]

print(quicksort(lista))
