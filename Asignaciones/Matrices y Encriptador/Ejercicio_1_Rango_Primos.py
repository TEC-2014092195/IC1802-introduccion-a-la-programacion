##1.Defina un programa que reciba un n e imprima todos los numeros primos entre el 0 y el n
cont="s"
while cont=="s":
    try:
        rango=[]
        primos=[]
        
        n=int(input("Digite número para calcular un rango de numeros primos: "))
        if n < 0:
            import math
            n=int(math.fabs(n))
            for i in range(n+1):
                rango.append(i)
        
            cant=0
            for i in range(len(rango)):
                cant=0
                for j in range(i+1):
                    if j > 0:
                        if (rango[i] % rango[j]) == 0:
                            cant+=1
                if cant <= 2 and cant > 0:
                    if rango[i] != 1:
                        primos.append(-(rango[i]))
                            
                        
            for i in range(len(primos)):
                print(primos[i])
            
            cont=input("Digite s para calcular otro rango: ")
        else:
            for i in range(n+1):
                rango.append(i)
            
            cant=0
            for i in range(len(rango)):
                cant=0
                for j in range(i+1):
                    if j > 0:
                        if (rango[i] % rango[j]) == 0:
                            cant+=1
                if cant <= 2 and cant > 0:
                    if rango[i] != 1:
                        primos.append(rango[i])
                            
                        
            for i in range(len(primos)):
                print(primos[i])
            
            cont=input("Digite s para calcular otro rango: ")
    except:
        print("Numero Invalido")
        cont=input("Digite s para calcular otro rango: ")
