
def asignar_barco_horizontal(barco, tablero, fila, pos_ini, acumulados_columna):
    for i in range(pos_ini, pos_ini + barco):
        tablero[fila][i] = 1
        acumulados_columna[i] += 1


def asignar_barco_vertical(barco, tablero, columna, pos_ini, acumulados_fila):
    for i in range(pos_ini, pos_ini + barco):
        tablero[i][columna] = 1
        acumulados_fila[i] += 1


def remover_barco_horizontal(barco, tablero, fila, pos_ini, acumulados_fila, acumulados_columna):
    for i in range(pos_ini, pos_ini + barco):
        tablero[fila][i] = 0
        acumulados_columna[i] -= 1
    acumulados_fila[fila] -= barco


def remover_barco_vertical(barco, tablero, columna, pos_ini, acumulados_fila, acumulados_columna):
    for i in range(pos_ini, pos_ini + barco):
        tablero[i][columna] = 0
        acumulados_fila[i] -= 1
    acumulados_columna[columna] -= barco
    return False


def ubicar_barco_horizontal(barco, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna, pos):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    for i in range(n):
        if acum_fila[i] + barco > demandas_filas[i]:
            continue

        pos_primer_cero = -1
        for j in range(m):
            if tablero[i][j] == 1 or (acum_columna[j] + 1 > demandas_columnas[j]):
                pos_primer_cero = -1
                continue
            if pos_primer_cero == -1:
                pos_primer_cero = j
            if j - pos_primer_cero == barco - 1:
                asignar_barco_horizontal(barco, tablero, i, pos_primer_cero, acum_columna)
                pos[0] = i
                pos[1] = pos_primer_cero
                acum_fila[i] += barco
                return True

    return False


def ubicar_barco_vertical(barco, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna, pos):
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
                asignar_barco_vertical(barco, tablero, i, pos_primer_cero, acum_fila)
                pos[0] = pos_primer_cero
                pos[1] = i
                acum_columna[i] += barco
                return True
    return False


def bt_naval_r(barcos, ini, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna, incumplidas):
    incumplidas_min = incumplidas
    for i in range(ini, len(barcos)):
        pos = [0, 0]  # [FILA, COLUMNA]
        if ubicar_barco_horizontal(barcos[i], tablero, demandas_filas, demandas_columnas, acum_fila,
                                   acum_columna, pos):
            bt_naval_r(barcos, ini + 1, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna,
                       incumplidas_min)
            incumplidas = sum(demandas_filas) + sum(demandas_columnas) - (sum(acum_fila) + sum(acum_columna))
            if incumplidas < incumplidas_min:
                incumplidas_min = incumplidas
            remover_barco_horizontal(barcos[i], tablero, pos[0], pos[1], acum_fila, acum_columna)
        if ubicar_barco_vertical(barcos[i], tablero, demandas_filas, demandas_columnas, acum_fila,
                                 acum_columna, pos):
            bt_naval_r(barcos, ini + 1, tablero, demandas_filas, demandas_columnas, acum_fila, acum_columna,
                       incumplidas_min)
            incumplidas = sum(demandas_filas) + sum(demandas_columnas) - (sum(acum_fila) + sum(acum_columna))
            if incumplidas < incumplidas_min:
                incumplidas_min = incumplidas
            remover_barco_vertical(barcos[i], tablero, pos[1], pos[0], acum_fila, acum_columna)
    return incumplidas_min


def bt_naval(barcos, demandas_filas, demandas_columnas):
    n = len(demandas_filas)
    m = len(demandas_columnas)
    incumplidas = sum(demandas_filas) + sum(demandas_columnas)
    tablero = [[0] * m for _ in range(n)]
    acumulados_fila = [0] * n
    acumulados_columna = [0] * m
    incumplidas_min = bt_naval_r(barcos, 0, tablero, demandas_filas, demandas_columnas, acumulados_fila,
                                 acumulados_columna, incumplidas)
    print(tablero)
    print(acumulados_fila)
    print(acumulados_columna)
    print(incumplidas_min)
