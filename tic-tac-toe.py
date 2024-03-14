import random
import os

def inicializar_juego():
    # Función que inicializa los valores del juego
    juego_en_curso = True
    jugadores = [[input("Jugador 1: "), "X"], [input("Jugador 2: "), "O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    return juego_en_curso, jugadores, jugador_actual, tablero

def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    # Actualiza el tablero con la acción del jugador actual
    tablero_actual[coordenada_fila][coordenada_columna] = jugador[1]
    return tablero_actual

def tablero_completo(tablero_actual):
    # Comprueba si el tablero está completo, devuelve True o False
    for fila in tablero_actual:
        if "-" in fila:
            return False
    return True

def comprobar_ganador(jugador, tablero_actual):
    # Comprueba si ha ganado el jugador actual, devuelve True o False
    # Comprobar por filas y columnas
    for i in range(3):
        if all(tablero_actual[i][j] == jugador[1] for j in range(3)) or \
           all(tablero_actual[j][i] == jugador[1] for j in range(3)):
            return True

    # Comprobar por diagonales
    if all(tablero_actual[i][i] == jugador[1] for i in range(3)) or \
       all(tablero_actual[i][2 - i] == jugador[1] for i in range(3)):
        return True

    return False

# Inicializar juego
juego_en_curso, jugadores, jugador_actual, tablero = inicializar_juego()

# Bucle principal del juego
while juego_en_curso:
    if tablero_completo(tablero):
        juego_en_curso = False
        print("Fin del juego, no hay ganador")
        break
    
    # Nuevo turno
    print("Turno de:", jugadores[jugador_actual][0])
    
    # Dibujar tablero
    print("  0 1 2")
    for i, fila in enumerate(tablero):
        print(i, " ".join(fila))

    # Selección de casilla
    coordenada_fila, coordenada_columna = map(int, input("Elige coordenadas (fila columna): ").split())

    # Actualizar tablero
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero)

    # Comprobamos si ha ganado
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False
        
        # Dibujar tablero
        print("  0 1 2")
        for i, fila in enumerate(tablero):
            print(i, " ".join(fila))
        
        print("¡Ganador:", jugadores[jugador_actual][0], "!")
    
    # Cambio de jugador
    jugador_actual = 1 - jugador_actual  # Alternar entre 0 y 1