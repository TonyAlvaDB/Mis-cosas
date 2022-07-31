print("Aqui te daras cuenta si tu numero es primo o no.")
numero = int(input("Cual es tu numero?: "))

def primos(numero):
    
    if numero < 1:
        print("Este numero no es primo")
        
    for i in range(2, numero):
        if numero % i == 0:
            print(f"Tu numero {numero} no es primo")
            break
    else:
        print(f"Tu numero {numero} es primo")

        
primos(numero)