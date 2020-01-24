#Recursividad
def fib(n):
    if n>=2:
        return fib(n-1) + fib(n-2)
    elif n==1 or n==2:
        return 1
    elif n==0:
        return 0    
    elif n<0:
        return 1
print (fib(6))               