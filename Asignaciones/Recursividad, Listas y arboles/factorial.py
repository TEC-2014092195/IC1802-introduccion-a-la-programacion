def factorial(num,r=1):
    if num > 0:
        r=r*num
        return factorial(num-1,r)
    else:
        return r

print(factorial(5))
