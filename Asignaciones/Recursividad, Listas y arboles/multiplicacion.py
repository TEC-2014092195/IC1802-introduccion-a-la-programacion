def multi(num1,num2,t=0):
    if num2 == 0:
        return t
    else:
        t+=num1
        return multi(num1,num2 - 1,t)



print(multi(4,100))
