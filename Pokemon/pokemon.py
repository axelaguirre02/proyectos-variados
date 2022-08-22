import time
import numpy as np
import sys

# Imprimir con demora
def imprimir_con_retraso(s):

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:

    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
        
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20

    def impresa(self, Pokemon2):

        print('-----BATALLA DE POKEMON-----')
        print(f'\n{self.nombre}')
        print('tipo/', self.tipos)
        print('ataque/', self.ataque)
        print('defensa/', self.defensa)
        print('Nv./', 3*(1+np.mean([self.ataque, self.defensa])))
        print('\nVS')
        print(f'\n{Pokemon2.nombre}')
        print('tipo/', Pokemon2.tipos)
        print('ataque/', Pokemon2.defensa)
        print('defensa/', Pokemon2.defensa)
        print('Nv./', 3*(1+np.mean([Pokemon2.ataque, Pokemon2.defensa])))
        time.sleep(2)

    def ventaja(self, Pokemon2):

        version = ['fuego', 'agua', 'planta']

        for i,k in enumerate(version):
            
            if self.tipos == k:

                # Son el mismo tipo
                if Pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\nNo es muy efectivo...'

                # Pokemon1 es mas fuerte
                if Pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    cadena_1_ataque = '\n¡Es muy eficaz!'
                    cadena_2_ataque = '\nNo es muy efectivo...'

                # Pokemon2 es mas fuerte
                if Pokemon2.tipos == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo...'
                    cadena_2_ataque = '\n¡Es muy eficaz!'

            return cadena_1_ataque, cadena_2_ataque

    def turno(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):

        while (self.barras > 0) and (self.Pokemon2.barras > 0):

            # Imprimir los puntos de salud de cada Pokemon
            print(f'\n{self.nombre}\t\tPS\t{self.puntos_de_salud}')
            print(f'{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}')

            # POKEMON 1
            print(f'¡Adelante {self.nombre}!')
            for i, x in enumerate(self.movimientos):
                print(f'{i+1}.', x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f'\n¡{self.nombre} usó {self.movimientos[index-1]}!')
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            # Determinar el daño
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud = ""

            # Agregar barras adicionales mas defensa boost
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="

            time.sleep(1)
            print(f'\n{self.nombre}\t\tPS\t{self.puntos_de_salud}')
            print(f'{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}')
            time.sleep(.5)

            # Comprobar si Pokemon se debilitó 
            if Pokemon2.barras <= 0:
                imprimir_con_retraso('\n...' + Pokemon2.nombre + ' se debilitó.')
                break

            # POKEMON 2
            print(f'¡Adelante {Pokemon2.nombre}!')
            for i, x in enumerate(Pokemon2.movimientos):
                print(f'{i+1}.', x)
            index = int(input('Elige un movimiento: '))
            imprimir_con_retraso(f'\n¡{Pokemon2.nombre} usó {Pokemon2.movimientos[index-1]}!')
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # Determinar el daño
            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""

            # Agregar barras adicionales mas defensa boost
            for j in range(int(self.barras+.1*self.defensa)):
                self.puntos_de_salud += "="

            time.sleep(1)
            print(f'\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}')
            print(f'{self.nombre}\t\tPS\t{self.puntos_de_salud}')
            time.sleep(.5)

            # Comprobar si Pokemon se debilitó 
            if self.barras <= 0:
                imprimir_con_retraso('\n...' + self.nombre + ' se debilitó.')
                break

    def lucha(self, Pokemon2):
        
        # Imprimir informacion de lucha
        self.impresa(Pokemon2)

        # Considerar la ventaja de tipo
        cadena_1_ataque, cadena_2_ataque = self.ventaja(Pokemon2)

        # Continua mientras Pokemon aun tenga puntos de salud
        self.turno(Pokemon2, cadena_1_ataque, cadena_2_ataque)

        # Recibir puntos
        money = np.random.choice(5000)
        imprimir_con_retraso(f'\nEl oponente te pagó ${money}.\n')


if __name__ == '__main__':

    # Crear objeto Pokemon
    Charizard = Pokemon('Charizard', 'Fuego', ['Lanzallamas', 'Pirotecnia', 'Giro Fuego', 'Ascuas'], {'ataque': 12, 'defensa': 8})
    Blastoise = Pokemon('Blastoise', 'agua', ['Pistola Agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque': 10, 'defensa': 10})
    Venusaur = Pokemon('Venusaur', 'planta', ['LatiAdelante Cepa', 'Hoja Afilada', 'Rayo Solar', 'Abatidoras'], {'ataque': 8, 'defensa': 12})

