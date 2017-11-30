numero = int(raw_input("Ingrese un numero para hallar su correspondiente Fibonnacci: "))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print map(fib, range(numero+1))

print ("El fibonacci de " + str(numero) + " es " + str(fib(numero)))
