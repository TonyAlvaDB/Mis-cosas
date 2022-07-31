print("Bienvenido al calculador de areas!")
print("Primero debo saber que tipo de poligono tienes")
tipo_Poligono = input("Si tienes un triangulo, ingresa (t), para un cuadrado ingresa (c), y para un rectangulo ingresa (r): ").lower()


def area(x):
    if x == "t":
        b = int(input("Cual es la base del triangulo?: "))
        h = int(input("Cual es la altura del triangulo?: "))
        a = (b*h)/2
        print(f"El area del triangulo es {a}")
    elif x == "c":
        l = int(input("Cual es el lado del cuadrado?: "))
        a = l * l
        print(f"El area del cuadrado es {a}")
    elif x == "r":
        b = int(input("Cual es la base de tu rectangulo?: "))
        h = int(input("Cual es la altura de tu rectangulo?: "))
        a = b * h
        print(f"El area del rectangulo es {a}")
        
area(tipo_Poligono)
