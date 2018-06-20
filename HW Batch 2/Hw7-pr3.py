#Sara D'Alessandro
#PROBLEM #3:

n = int(input("Type 1 or 0: "))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(n-1) + fib(n-2))

