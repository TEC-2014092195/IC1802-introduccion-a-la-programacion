##----------------------------------------------------------------------------------------------------
##Un banco requiere un programa que controle cuentas con los siguientes datos:
##    -Cuenta: #Cuenta,cantidad,tipo(ahorros, corriente, moneda 'dolar|colon' ), Cliente, Sucursal
##    -Cliente: nom, ape,nacimiento, dirección,telefono, correo
##    -Sucursal: lugar y nom de sucursal
##Debe poder:
##    a. Asignar cuentas por persona
##    b. Depositar a una cuenta
##    c. Retirar de una cuenta
##    Restricciones:
##        -Si es el día de cumpleaños agregar un 2% de saldo a lo que ya tiene
##        -Si trata de Retirar 3 veces antes de Depositar (al menos una vez) cobrar un 1%
##----------------------------------------------------------------------------------------------------


class Cliente:
    c_cliente=[]
    cuenta=[]
    interes=0
    m_cuenta=[]
    texto=["Id: ","Nombre: ","Apellido: ","Dia_Nac: ","Mes_Nac: ","Año_Nac: ","Dirección: ","Telefono: ","Correo: ","Tipo Cuenta: ","Moneda: ","Fondos: ","Lugar: ","Nom_Sucu: ","Regalia: ","Interes: "]
    
##getFondos-----------------------------------------------------
    def getFondos(self,idcuenta1):
        for i in range(len(self.m_cuenta)):
            if idcuenta1==self.m_cuenta[i][0]:
                return print(self.texto[0]+str(self.m_cuenta[i][0])+"\n"+self.texto[11]+str(self.m_cuenta[i][11]))
            
                    
##getCuenta-----------------------------------------------------
    def getCuenta(self):
        for i in range(len(self.m_cuenta)):
            for j in range(len(self.m_cuenta[i])):
                    print(self.texto[j]+str(self.m_cuenta[i][j]))
    
##setCuenta-----------------------------------------------------
    def setCuenta(self,c_cuenta):
        self.m_cuenta.append(c_cuenta)
        
##setDepositar--------------------------------------------------
    def setDepositar(self,idcuenta1,cantidad1):
        bandera=False
        for i in range(len(self.m_cuenta)):
            if idcuenta1==self.m_cuenta[i][0]:
                self.m_cuenta[i][11]+=cantidad1
                self.m_cuenta[i][15] = 1 # Indica que si he hecho algún deposito
                bandera=True
        if bandera==False:
            print("No existe cuenta")
        else:
            print("satisfactorio")
            
##setRetirar-----------------------------------------------------
    def setRetirar(self,idcuenta1,cantidad1):
        bandera=False
        for i in range(len(self.m_cuenta)):
            if idcuenta1==self.m_cuenta[i][0]:
                bandera=True
                if cantidad <= self.m_cuenta[i][11]:
                    self.m_cuenta[i][11]-=cantidad1
                    if self.m_cuenta[i][14]==2 and self.m_cuenta[i][15]==0:
                        self.m_cuenta[i][11]-=(self.m_cuenta[i][11]*0.01)
                        self.m_cuenta[i][14]=0
                    elif self.m_cuenta[i][14] == 2:
                        self.m_cuenta[i][14]=1
                    else:
                        self.m_cuenta[i][14] += 1
                        self.m_cuenta[i][15] = 0 #Indica que no he hecho deposito 
                    bandera=True
                else:
                    print("Cantidad mayor a sus fondos")
        if bandera==False:
            print("No existe cuenta")
        else:
            print("satisfactorio")

##Programa Principal----------------------------------------------
            
cont="s"
dia_h=0
mes_h=0
ano_h=0
while cont=="s":
    try:
        print("Digite fecha dde hoy")
        dia_h=int(input("Día hoy:\n>"))
        mes_h=int(input("Mes hoy:\n>"))
        ano_h=int(input("Año hoy:\n>"))
        while cont=="s":

            c_cuenta=[]
            nom=""
            ape=""
            nac=""
            direc=""
            tel=""
            correo=""
            idcuenta=""
            interes=0
            tipo_cuenta=""
            moneda=""
            cantidad=0
            
            #variables para nacimiento
            dia_n=0
            mes_n=0
            ano_n=0
            regalo=False ##Si mes y dia coinciden se cambia a True
            
            opc=""
            cliente=Cliente()
            opc=input("\na. asig \nb. Depositar\nc. Retirar \ns. Salir \nDigite opc: \n>")

##Asignar Cuentas----------------------
            if opc=="a":
                c_cuenta=[]
                c_cuenta.append(input("Digite id cuenta: \n>"))
                c_cuenta.append(input("Digite nombre del cliente: \n>"))
               
                c_cuenta.append(input("Digite apellido del cliente: \n>"))
                
                dia_n=int(input("Día nac: \n>"))
                c_cuenta.append(dia_n)
                mes_n=int(input("Mes nac: \n>"))
                c_cuenta.append(mes_n)
                ano_n=int(input("Año nac: \n>"))
                c_cuenta.append(ano_n)
                if dia_n == dia_h and mes_n == mes_h:
                    regalo=True
                else:
                    regalo=False
                c_cuenta.append(input("Digite dirección: \n>"))
                c_cuenta.append(input("Digite telefono: \n>"))
                c_cuenta.append(input("Digite correo: \n>"))
                tipo_cuenta=input("\na. ahorros\nb. corriente\ningrese tipo\n>")
                if tipo_cuenta=="a":
                    tipo_cuenta="ahorros"
                    c_cuenta.append(tipo_cuenta)
                elif tipo_cuenta=="b":
                    tipo_cuenta="corriente"
                    c_cuenta.append(tipo_cuenta)
                else:
                    c_cuenta.append("cuenta no definida")
                
                moneda=input("\na. dolar \nb. colon\ningrese tipo\n>")
                if moneda=="a":
                    moneda="dolares"
                    c_cuenta.append(moneda)
                elif moneda=="b":
                    moneda="colon"
                    c_cuenta.append(moneda)
                else:
                    c_cuenta.append("moneda no definida")
                cantidad=int(input("Digite cantidad inicial: "))
                if regalo == True:
                    
                    cantidad=(cantidad+(cantidad*0.02))
                c_cuenta.append(cantidad)
                c_cuenta.append(input("digite lugar: "))
                c_cuenta.append(input("Digite nombre sucursal :"))
                c_cuenta.append(0) #contador de interes cunado llegue a 2 se cobrará el 1%
                c_cuenta.append(0) #contador para saber si ha hecho algún deposito (para no cobrar el 1%) 
                cliente.setCuenta(c_cuenta)
                cliente.getCuenta()
            
                cont=input("Desea continuar (s/n): \n>")
                
##Depositar---------------------------
            elif opc=="b":
                idcuenta=input("Digite id cuenta: ")
                cantidad=int(input("Digite cantidad a depositar: "))
                cliente.setDepositar(idcuenta,cantidad)
                cliente.getFondos(idcuenta)
                cont=input("Desea continuar (s/n): \n>")

##Retirar-----------------------------
            elif opc=="c":
                idcuenta=input("Digite id cuenta: ")
                cantidad=int(input("Digite cantidad a retirar: "))
                cliente.setRetirar(idcuenta,cantidad)
                cliente.getFondos(idcuenta)
                cont=input("Desea continuar (s/n): \n>")

##Salir-------------------------------
            elif opc=="s":
                print("Gracia por preferirnos")
                cont="n"

##Opción Inválida---------------------
            else:
                print("Opción Inválida")
                cont=input("Desea continuar (s/n): \n>")
                
    except:
        print("Entrada Inválida")
        cont=input("Desea continuar (s/n): \n>")
