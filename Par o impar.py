def calculo_Par():
    numero = int(input("Por favor, coloque el numero que deseas saber si es par o impar: "))
    calculo = numero % 2
    
    if calculo == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
        
        
calculo_Par()