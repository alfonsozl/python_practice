
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
x = int(input('Cual numero de Fibonacci desea conocer?'))
print(fibo(x))

###########################################################



"""
F(n) = F(n-1) + F(n-2)
{
         0    1    1    2    3    5    8    13
    n = (0), (1), (2), (3), (4), (5), (6), (7)

    3 = 

    F(4) = F(n-1) + F(n-2)
    F(4) =   1    +   2    =    3
}
"""