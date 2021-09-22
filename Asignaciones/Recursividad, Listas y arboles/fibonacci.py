def fib(num,anterior=0,sucesor=1,t=0):
    if num == 1:
        return t
    else:
        t=anterior+sucesor
        anterior=sucesor
        sucesor=t
        return fib(num-1,anterior,sucesor,t)
        



print(fib(7))
