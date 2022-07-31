#Fibonacci. El resultado es la suma de los dos anteriores. 0, 1, 1, 2, 3, 5, 8, 13.
nu1 = 0
nu2 = 1

def Fibonacci(nu1, nu2):
    contador = 0
    acumulador = [0, 1]
    
    while contador < 50:
        fib = nu1 + nu2
        nu1 = nu2
        nu2 = fib
        acumulador.append(fib)
        contador = contador + 1
    print(acumulador)

Fibonacci(nu1, nu2)