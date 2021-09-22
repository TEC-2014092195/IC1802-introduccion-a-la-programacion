def tartaglia2(num):   # wrapper de tartaglia2Aux() 
	print ([1])
	nivel = [1,1]
	tartaglia2Aux(nivel,num) # la variable 'nivel' hace referencia 
			     # a los niveles del triangulo
	
def tartaglia2Aux(nivel,num):
	if len(nivel) < num:  # se define la altura del triangulo
		print (nivel)
		aux = []
		for a in range(len(nivel) -1):
			aux.append(nivel[a] + nivel[a+1])
		aux = [1] + aux + [1]
		tartaglia2Aux(aux,num)

num=int(input("Digite la altura del triangulo de pascal: "))
tartaglia2(num)




