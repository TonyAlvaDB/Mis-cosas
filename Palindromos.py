word = input("Elige la palabra que quieres saber si es palindromo: ")

def palindromo(word):

    length_string = len(word)

    sliced_back = word[length_string::-1]

    if sliced_back == word:
        print(f"Tu palabra {word} es un palindromo!")
    else:
        print(f"Tu palabra {word} no es un palindromo")


palindromo(word)
