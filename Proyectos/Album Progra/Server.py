import socketserver
import threading
import time
import pickle
import os


class MiTcpHandler(socketserver.BaseRequestHandler):
    
        
        
    def handle(self):
        dato=False
        while dato != True:
            try:
                dato = self.request.recv(1024) #Strip quita los espacios demas de lo que recibe
                
                dato = pickle.loads(dato)#Decodificando el tipo bytes
                print(type(dato))

                if dato == "userServer":
                    bandera=True
                    bandera=pickle.dumps(bandera)
                    self.request.send(bandera)
                    usuario = self.request.recv(1024)
                    
                    usuario = pickle.loads(usuario)
                    
                    f = open("username.txt","wb")
                    pickle.dump(usuario,f)
                    f.close()
                    print("Correcto",usuario,type(usuario))

                elif dato == "getusername":
                    file = open("username.txt","rb")
                    usuario = pickle.load(file)
                    file.close()
                    #os.remove("username.txt")
                    
                    usuario = pickle.dumps(usuario)
                    self.request.send(usuario)

                    

                elif dato == "newuser":
                    
                    print("bien")
                    
                    usuario = self.request.recv(1024)
                    
                    print("bien")
                    usuario = pickle.loads(usuario)
                    print(usuario)
                    print("bien")
                    file = open("Usuarios/Registrados/user_"+usuario+".txt","rb")
                    ce = pickle.load(file)
                    cb = pickle.load(file)
                    postales = pickle.load(file)
                    primerpaquete = pickle.load(file)
##                    print("Pasócsjkvsaj")
                    
                    file.close()
                    
                    ce = pickle.dumps(ce)
                    cb = pickle.dumps(cb)
                    postales = pickle.dumps(postales)
                    primerpaquete = pickle.dumps(primerpaquete)
                    
                    self.request.send(cb)
                    self.request.recv(1024)
                    self.request.send(postales)
                    self.request.recv(1024)
##                    print("Pasócsjkvsaj")
                    self.request.send(primerpaquete)
                    os.remove("username.txt")
                

                time.sleep(0.1)
            except:
                
                dato=True


        
class ThreadServer (socketserver.ThreadingMixIn, socketserver.ForkingTCPServer):
    pass



def main():
    print("Servidor")
    host = "localhost"
    port = 9999


    server = ThreadServer( (host,port) ,MiTcpHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print("Server corriendo")
    

main()
    
    
        
