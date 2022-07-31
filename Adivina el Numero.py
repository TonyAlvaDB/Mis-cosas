#el usuario adivinara un numero y le vamos a decir si el numero es mayor o mejor que el que tenemos

import random


def adivina_el_numero(x):
    print("========================")
    print("  Bienvenido al juego!  ")
    print("========================")
    print("Tu meta es adivinar el numero generado por la computadora")
    
    numero_aleatorio = random.randint(1, x) # numero aleatoriop entre 1 y x inclusive
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un nunero entre 1 y {x}: "))
        
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy bajo.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy alto.")
    print(f"Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)