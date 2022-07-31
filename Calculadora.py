import math

def calculadora():
    operacion = input("Elige que tipo de operacion de dos digitos quieres hacer: +, -, *, / \n")
    primer_Digito = int(input("Cual es tu primer digito?: "))
    segundo_Digito = int(input("Cual es tu segundo digito?: "))
    
    if operacion == "+":
        resultado = primer_Digito + segundo_Digito
        print(f"El resultado de tu suma es {resultado}")

    if operacion == "-":
        resultado = primer_Digito - segundo_Digito
        print(f"El resultado de tu resta es {resultado}")

    if operacion == "*":
        resultado = primer_Digito * segundo_Digito
        print(f"El resultado de tu multiplicacion es {resultado}")
    
    if operacion == "/":
        resultado = primer_Digito / segundo_Digito
        print(f"El resultado de tu division es {resultado}")
        

calculadora()