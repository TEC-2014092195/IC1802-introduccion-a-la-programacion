import pickle
import random

file = open("user_kevin.txt","rb")

ce = pickle.load(file)
cb = pickle.load(file)
postales = pickle.load(file)
primerpaquete = pickle.load(file)
file.close()

print(ce)
print(cb)
print(postales)
print("\n")
print(primerpaquete)

e=input()

