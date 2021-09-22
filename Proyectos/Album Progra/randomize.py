import pickle
import random

file = open("EnVenta.txt","wb")
enventa = []
pickle.dump(enventa,file)
file.close()
##r=pickle.load(file)
##print(r)

##ce = pickle.load(file)
##cb = pickle.load(file)
##postales = pickle.load(file)
##file.close()
##
##newt=[]
##for i in range(2):
##    
##    t=random.sample(postales,  9)
##    newt.extend(t)
##random.shuffle(newt)
##primerpaquete=[]
##for i in range(9):
##    primerpaquete.append(random.choice(newt))
##print(primerpaquete)
##
##e=input()

