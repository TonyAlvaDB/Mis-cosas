print("Bienvenido al revisor de anagramas")
palabra_1 = input("Cual es la primer palabra?: ").lower()
palabra_2 = input("Cual es la primer palabra?: ").lower()

def anagrama(palabra_1, palabra_2):
    
    palabra_Lista_1 = sorted(list(palabra_1))
    palabra_Lista_2 = sorted(list(palabra_2))
    
    if palabra_1 == palabra_2:
        print("Ambas palabras son la misma!")
    elif palabra_Lista_1 == palabra_Lista_2:
        print(f"Las palabras {palabra_1} y {palabra_2} son anagramas!")
    else:
        print(f"Las palabras {palabra_1} y {palabra_2} no son anagramas!")
        
anagrama(palabra_1, palabra_2)
