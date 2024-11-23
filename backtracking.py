'''Condicion de barco:
-si no hay ni un barco.
-si la cant de fil y col se pasan de la cant pedida.
-las filas y cols pedidas sean adyacentes. '''


def es_valido(uicacion_barco, tablero, fila, columna):
    #el barco debe ocupar la cant de fia y columnas que indica el barco:
    for i in len(tablero):
        for j in len(tablero):
            if tablero[i][j] == 1:
                return False


#debo poder poner un barco en una ubicacion valida
def solucion_backtracking(barco, tablero, pos_barco = -1):
    if pos_barco == barco:
        return True
    for i in range(10):
        for j in range(10):
            if es_valido((i, j), tablero):
                tablero[i][j] = 1
                if solucion_backtracking(barco, tablero, pos_barco + 1):
                    return True
                tablero[i][j] = 0
    return False


def main():
    tablero = [[0 for i in range(10)] for j in range(10)]
    barco = 5
    solucion_backtracking(barco, tablero)
    for i in range(10):
        print(tablero[i])

main()