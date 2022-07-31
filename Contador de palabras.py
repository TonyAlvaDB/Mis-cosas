print("Bienvenido al contador de palabras!")

frase = input("Coloca tu frase aqui: ").lower()
palabra_A_Buscar = input("Cual palabra deseas buscar dentro de la frase? ").lower()

def buscador (a, b):
    a_Split = a.split()
    a_Counter = a_Split.count(b)
    print(f"La palabra {b} se dice {a_Counter} veces")

buscador(frase, palabra_A_Buscar)
    
