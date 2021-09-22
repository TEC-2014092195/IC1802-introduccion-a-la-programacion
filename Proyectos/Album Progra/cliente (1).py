import socket
import pickle

print("Cliente")

host = "localhost"

port = 9999

sock = socket.socket()

sock.connect((host,port))

oracion = input("Ingrese una oración...")
oracion = pickle.dumps(oracion)
try:
    sock.send(oracion)
except:
    print("hubo un error en el server")

##numero = sock.recv(1024)
##
##numero = numero.decode('utf-8')
##print("La oracion ", oracion, " tiene caracteres ", numero)
##timepo = input("presione enter para salir")

sock.close()
