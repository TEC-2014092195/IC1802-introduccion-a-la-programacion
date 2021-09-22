def dividir(num,divisor,acu):
    if num == 0:
        print("Resultado:",acu)
    elif num < 0:
        print("Fin")
    else:
        dividir(num-divisor,divisor,acu+1)
    

num=int(input("Digite dividendo: "))
divisor=int(input("Digite divisor: "))
dividir(num,divisor,0)

    
