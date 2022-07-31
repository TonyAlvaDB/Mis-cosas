#mostrar los numeros del 1 al 100. Si el numero es divisible entre 3 sustituir por la palabra fizz. Si es divisible entre 5 buzz, y si es divibisible entre 3 y 5 fizzbuzz

def fizzbuzz():
    
    number_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    contador = 0
    
    while contador < 100:
        
        #Aqui estoy colocando variables para revisar si hay sobrante al dividir
        divisible_3 = number_List[contador] % 3
        divisible_5 = number_List[contador] % 5

        if divisible_3 == 0 and divisible_5 == 0:
            number_List[contador] = 'Fizzbuzz'

        elif divisible_3 == 0:
            number_List[contador] = 'Fizz'
        
        elif divisible_5 == 0:
            number_List[contador] = 'Buzz'
        
        contador = contador + 1
        
    print(number_List)
    
fizzbuzz()

