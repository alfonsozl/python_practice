
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Ingrese el numero del que quiere calcular su factorial: "))

print(factorial(n))

######################################
"""
def fib(n):
    a, b = 0,1
    while a < n:                      #for n in range(20):
        print(a)
        a, b = b, a+b
                                      #m = int(input("Ingresa límite máximo de la sucesión: "))
fib(100)#fib(m)
"""
######################################

"""
def countdown(n):
    if n <= 0:
        print('GO!')
    else:
        print(n)
        countdown(n-1)
countdown(3)
"""
#####################################