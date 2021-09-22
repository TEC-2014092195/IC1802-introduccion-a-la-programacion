lista=[0,6,3,2,1,-2]

def burbuja(lista):
    for1(lista)
    print(lista)

def for1(lista,i=0):
    if i < len(lista):
        return for2(lista,i,i)
    else:
        return lista

def for2(lista,i,j):
    if j < len(lista):
        if lista[i]>=lista[j]:
            temp=lista[i]
            lista[i]=lista[j]
            lista[j]=temp
        return for2(lista,i,j+1)
    else:
        return for1(lista,i+1)

burbuja(lista)
