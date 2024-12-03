# Verifica que el barco a ubicar no sea adyacente a otro ya ubicado
def adyacente_horizontal(barco, tablero, fila, pos_ini, n, m):
    if pos_ini > 0 and (tablero[fila][pos_ini - 1] == 1 or (fila > 0 and tablero[fila - 1][pos_ini - 1] == 1) or
                        (fila < n - 1 and tablero[fila + 1][pos_ini - 1] == 1)):
        return False
    if pos_ini + barco < m and (tablero[fila][pos_ini + barco] == 1 or
                                (fila > 0 and tablero[fila - 1][pos_ini + 1] == 1) or
                                (fila < n - 1 and tablero[fila + 1][pos_ini + 1] == 1)):
        return False

    for i in range(pos_ini, pos_ini + barco):  # O(L) con L el largo del barco actual
        if (fila > 0 and tablero[fila - 1][i] == 1) or (fila < n - 1 and tablero[fila + 1][i] == 1):
            return False

    return True


def adyacente_vertical(barco, tablero, columna, pos_ini, n, m):
    if pos_ini > 0 and (tablero[pos_ini - 1][columna] == 1 or
                        (columna > 0 and tablero[pos_ini - 1][columna - 1] == 1) or
                        (columna < m - 1 and tablero[pos_ini - 1][columna + 1] == 1)):
        return False
    if pos_ini + barco < n and (tablero[pos_ini + barco][columna] == 1 or
                                (columna > 0 and tablero[pos_ini + barco][columna - 1] == 1) or
                                (columna < m - 1 and tablero[pos_ini + barco][columna + 1] == 1)):
        return False

    for i in range(pos_ini, pos_ini + barco):
        if (columna > 0 and tablero[i][columna - 1] == 1) or (columna < m - 1 and tablero[i][columna + 1] == 1):
            return False
    return True


def asignar_barco_horizontal(barco, tablero, fila, pos_ini, acumulados_columna):
    for i in range(pos_ini, pos_ini + barco):
        tablero[fila][i] = 1
        acumulados_columna[i] += 1


def asignar_barco_vertical(barco, tablero, columna, pos_ini, acumulados_fila):
    for i in range(pos_ini, pos_ini + barco):
        tablero[i][columna] = 1
        acumulados_fila[i] += 1


# Ubica un barco de forma horizontal en el tablero
def ubicar_barco_horizontal(barco, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    for i in range(n):  # O(m x n)
        if acum_fila[i] + barco > demandas_filas[i]:
            continue

        pos_primer_cero = -1
        for j in range(m):  # O(m)
            if tablero[i][j] == 1 or (acum_columna[j] + 1 > demandas_columnas[j]):
                pos_primer_cero = -1
                continue
            if pos_primer_cero == -1:
                pos_primer_cero = j
            if j - pos_primer_cero == barco - 1:
                if not adyacente_horizontal(barco, tablero, i, pos_primer_cero, n, m):
                    pos_primer_cero = -1
                    continue
                asignar_barco_horizontal(barco, tablero, i, pos_primer_cero, acum_columna)
                acum_fila[i] += barco
                return True

    return False


def ubicar_barco_vertical(barco, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    for i in range(m):
        if acum_columna[i] + barco > demandas_columnas[i]:
            continue

        pos_primer_cero = -1
        for j in range(n):
            if tablero[j][i] == 1 or (acum_fila[j] + 1 > demandas_filas[j]):
                pos_primer_cero = -1
                continue
            if pos_primer_cero == -1:
                pos_primer_cero = j
            if j - pos_primer_cero == barco - 1:
                if not adyacente_vertical(barco, tablero, i, pos_primer_cero, n, m):
                    pos_primer_cero = -1
                    continue
                asignar_barco_vertical(barco, tablero, i, pos_primer_cero, acum_fila)
                acum_columna[i] += barco
                return True
    return False


# Solucion es una lista de tuplas (fila_ini, columna_ini, fila_fin, columna_fin) con las posiciones de cada barco
def validador_naval(demandas_filas, demandas_columnas, solucion):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    acumulados_fila = [0] * len(demandas_filas)
    acumulados_columna = [0] * len(demandas_columnas)
    tablero = [[0] * m for _ in range(n)]
    for barco in solucion:  # O(k)
        if (barco[0] != barco[2] and barco[1] != barco[3]) or (barco[0] == barco[2] and barco[3] < barco[1] or
                                                               barco[1] == barco[3] and barco[2] < barco[0]):
            return False

        # O(n x m)
        if barco[0] == barco[2] and not ubicar_barco_horizontal(barco[3] - barco[1] + 1, tablero, demandas_filas,
                                                                demandas_columnas, acumulados_fila, acumulados_columna):
            return False

        # O(n x m)
        if barco[1] == barco[3] and not ubicar_barco_vertical(barco[2] - barco[0] + 1, tablero, demandas_filas,
                                                              demandas_columnas, acumulados_fila, acumulados_columna):
            return False
    return True
