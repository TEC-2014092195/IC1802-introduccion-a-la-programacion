archivo = open("Hola.txt")
linea=archivo.readline()
lista=linea.split(" , ")
print(lista)
archivo.close()

archivo = open("Hola.txt","a")
var=",Nuevo,Registro"
archivo.write(var)

archivo = open("Hola.txt")
linea=archivo.readline()
lista=linea.split(",")
print(lista)
archivo.close()
##for line in archivo:
##    valores = line.split()
##    print(line)
