import random


def jugar():
    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, o 'ti' para tijera.\n ").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    
    if usuario == computadora:
        return 'Empate!'
    
    if gano_el_jugador (usuario, computadora):
        return 'Ganaste!'
    
    return 'Perdiste!'


def gano_el_jugador(jugador, oponente):
    #Retornar el valor true si gana el jugador.
    #Piedra gana a Tijera
    #Tijera gana a Papel
    #Papel gana a Piedra
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente =='pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())