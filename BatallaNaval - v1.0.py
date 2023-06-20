import random
from math import ceil

tablero = []
filaAbajo = ''
listatablero = ['3', '4', '5', '6', '7', '8', '9', '10']

# Determinar tamaño del tablero
tamañoElegido = False
while tamañoElegido == False:
    tamanioDelTablero = input("Ingrese el tamaño del tablero (Entre 3 y 10): ")
    if tamanioDelTablero in listatablero:
        tamanioDelTablero = int(tamanioDelTablero)
        tamañoElegido = True
    else:
        print("Valor no valido")


# Crear el tablero
for x in range(tamanioDelTablero):
    tablero.append(["-"] * tamanioDelTablero)
    filaAbajo += str(x) + ' '
filaAbajo += '▛'

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    t = 0
    for fila in tablero:
        print(" ".join(fila) + ' ' +str(t))
        t += 1
    print(filaAbajo)
    print()

# Función para colocar los barcos en posiciones aleatorias
def colocar_barcos(tablero, num_barcos):
    Lista = []
    for _ in range(num_barcos):
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero[0]) - 1)
        tablero[fila][columna] = "-"
        filacolumna=str(fila)+str(columna)
        Lista.append(filacolumna)
    return Lista

#Funcion para elegir dificultad

def dificultad(tablerototal):
    print("Elija la dificultad")
    CantidadTurnos = 0
    difiElegida = False
    while difiElegida == False:
        Difi=input("Ingrese 1 para facil, 2 para normal y 3 para dificil: ")
        if Difi == '1': # Dificultad Fácil
            CantidadTurnos=tablerototal*0.7
            difiElegida = True
        elif Difi == '2': # Dificultad Intermedia
            CantidadTurnos=tablerototal*0.5
            difiElegida = True
        elif Difi == '3': # Dificultad Difícil
            CantidadTurnos=tablerototal*0.3
            difiElegida = True
        else:
            print("No valido")
    return CantidadTurnos


# Iniciar el juego
print("\n¡Bienvenido a Batalla Naval! \n─────█ █ █───────── \n───████████─────── \n▀████████████████▀\n")
mostrar_tablero(tablero)

# Colocar barcos en el tablero
tablerototal=tamanioDelTablero*tamanioDelTablero
n = False
listabarcos = []
tamanioDelTableroOtro = int(tamanioDelTablero)
while n == False:
    CantidadBarcos = input("Ingrese la cantidad de barcos: ")
    while tamanioDelTableroOtro != 0:
        listabarcos.append(str(tamanioDelTableroOtro))
        tamanioDelTableroOtro -= 1
    if CantidadBarcos in listabarcos:
        colocar_barcos(tablero, int(CantidadBarcos))
        n = True
        CantidadBarcos = int(CantidadBarcos)
    else:
        print("Ese valor no es valido")

CantidadTurno = ceil(dificultad(tablerototal))
CantidadTurno = int(CantidadTurno)

ListaFilaColumna=colocar_barcos(tablero, CantidadBarcos)

# Jugar

barcosHundidos = 0
disparos = 0
listaDisparos = []

for turno in range(CantidadTurno):
    print("Turno", turno + 1)
    listaFilascolumnas=[]
    for i in range(tamanioDelTablero):
        listaFilascolumnas.append(str(i))
    w=0
    while w!=1:
        adivina_fila = (input("Adivina la fila: "))
        if adivina_fila in listaFilascolumnas:
            adivina_columna = (input("Adivina la columna: "))
            if adivina_columna in listaFilascolumnas:
                adivina_fila_int=int(adivina_fila)
                adivina_columna_int=int(adivina_columna)
                AfilaAcolumna=adivina_fila+adivina_columna
                disparoHecho = adivina_fila + adivina_columna
                listaDisparos.append(disparoHecho)
                w=w+1
            else:
                print("Columna no valida")
        else:
            print("Fila no valida")

    espacioAdivinado = adivina_fila + adivina_columna

    if AfilaAcolumna in ListaFilaColumna:
        print("¡Felicitaciones! ¡Hundiste un barco!")
        tablero[adivina_fila_int][adivina_columna_int] = "X"
        barcosHundidos += 1
        disparos += 1
        ListaFilaColumna.remove(espacioAdivinado)
    else:
        if adivina_fila_int < 0 or adivina_fila_int > (tamanioDelTablero-1) or \
           adivina_columna_int < 0 or adivina_columna_int > (tamanioDelTablero-1):
            print("Oops, esa posición no es válida.")
            turno=turno-1
        elif tablero[adivina_fila_int][adivina_columna_int] == "X":
            print("Ya has adivinado esa posición.")
            turno=turno-1
            disparos += 1
        elif tablero[adivina_fila_int][adivina_columna_int] == "O":
            print("Ya has dado a esa posición.")
            turno=turno-1
            disparos += 1
        elif adivina_fila_int > 0 or adivina_fila_int < (tamanioDelTablero-1) or \
            adivina_columna_int > 0 or adivina_columna_int < (tamanioDelTablero-1):
            print("¡Oops! ¡No has dado en el blanco!")
            tablero[adivina_fila_int][adivina_columna_int] = "O"
            disparos += 1
        else:
            print("Oops, esa posición no es válida.")
            turno=turno-1
        

    if ListaFilaColumna == []:
        break

    mostrar_tablero(tablero)
    
print()
if ListaFilaColumna == []:
    print('Felicidades! Has ganado!')
else:
    print('Qué lastima, te han faltado barcos...')
print(f'Has hundido {barcosHundidos} barcos, en {disparos} disparos.')
print(f'Tus disparos fueron: {listaDisparos}')

print("\n¡Fin del juego!\n \n▀▀▀▄░▄▄░░▄▀▀▄▄▄░░░░ \n▄▀▀▄█▄░▀░▄▀▄█▄░▀▄░░ \n░░░░█░▀░▀░░ █░▀▄░░░░ \n░░░▐▌░░░░░░▐▌░░░░██ \n██████▄▄▄██████▄███")
