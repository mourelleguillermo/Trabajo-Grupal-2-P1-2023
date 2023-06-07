import random
from math import ceil

tablero = []
a=0
while a==0:
    tamanioDelTablero=int(input("ingrese el tamaño del tablero "))
    if tamanioDelTablero>=3 and tamanioDelTablero<=10:
        a=+1
    else:
        print("Valor no valido")


# Crear el tablero
for x in range(tamanioDelTablero):
    tablero.append(["-"] * tamanioDelTablero)

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función para colocar los barcos en posiciones aleatorias
def colocar_barcos(tablero, num_barcos):
    Lista=[]
    for _ in range(num_barcos):
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero[0]) - 1)
        tablero[fila][columna] = "-"
        str(fila)
        str(columna)
        filacolumna=fila+columna
        Lista.append(filacolumna)

#Funcion para elegir dificultad

def dificultad(tablerototal):
    print("Elija la dificultad")
    CantidadTurnos=0
    Difi=input("Ingrese 1 para facil, 2 para normal y 3 para dificil ")
    if Difi=='1':
        CantidadTurnos=tablerototal*0.7
    elif Difi=='2':
        CantidadTurnos=tablerototal*0.5
    elif Difi=='3':
        CantidadTurnos=tablerototal*0.3
    return CantidadTurnos




# Iniciar el juego
print("¡Bienvenido a Batalla Naval!")
mostrar_tablero(tablero)

# Colocar barcos en el tablero
tablerototal=tamanioDelTablero*tamanioDelTablero
n=0
while n==0:
    CantidadBarcos = int(input("Ingrese la cantidad de barcos "))
    if CantidadBarcos <= tablerototal:
        colocar_barcos(tablero, CantidadBarcos)
        n=+1
    else:
        print("Ese valor no es valido")

CantidadTurno=ceil(dificultad(tablerototal))
CantidadTurno = int(CantidadTurno)

# Jugar
for turno in range(CantidadTurno):
    print("Turno", turno + 1)
    adivina_fila = int(input("Adivina la fila: "))
    adivina_columna = int(input("Adivina la columna: "))

    if tablero[adivina_fila][adivina_columna] == "B":
        print("¡Felicitaciones! ¡Hundiste un barco!")
        tablero[adivina_fila][adivina_columna] = "X"
    else:
        if adivina_fila < 0 or adivina_fila > 4 or \
           adivina_columna < 0 or adivina_columna > 4:
            print("Oops, esa posición no es válida.")
        elif tablero[adivina_fila][adivina_columna] == "X":
            print("Ya has adivinado esa posición.")
        else:
            print("¡Oops! ¡No has dado en el blanco!")
            tablero[adivina_fila][adivina_columna] = "O"

    mostrar_tablero(tablero)

print("¡Fin del juego!")
