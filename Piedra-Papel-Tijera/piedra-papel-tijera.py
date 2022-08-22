import numpy as np
import time

def piedra_papel_tijera():

    opciones = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}

    jugador = input('\nElige piedra, papel o tijera: ')

    while jugador not in {'piedra', 'papel', 'tijera'}:

        print('Opcion no valida. ¡Intente de nuevo!')
        jugador = input('Elige piedra, papel o tijera: ')

    computadora = np.random.choice(['piedra', 'papel', 'tijera'])

    time.sleep(.5)
    print('\nHas seleccionado:', jugador)
    print('La computadora ha seleccionado:', computadora, '\n')

    if opciones[jugador] == computadora:
        print('¡Has ganado!\n')
    elif opciones[computadora] == jugador:
        print('¡Has perdido!\n')
    else:
        print('¡Empate!\n')

piedra_papel_tijera()
