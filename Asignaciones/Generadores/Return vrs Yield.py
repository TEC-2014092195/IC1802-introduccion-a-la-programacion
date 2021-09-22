##RETURN se utiliza para devolver el valor una vez
##YIELD se utiliza para generadores en los que se devuelve el primer valor después otro, o sea que se pueden iterar, es como devolver el valor donde dejé a la función y NO iniciarla nuevamente
def suma(num):
    for i in range(num):
        num+=i
        yield num

for e in suma(5):
    print(e)


