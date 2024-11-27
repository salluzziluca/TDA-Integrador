from csv_casos import procesar_archivo

def calcular_demanda_incumplida(filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
    """Calcula la demanda que no se ha cumplido en filas y columnas."""
    fila_incumplida = sum(max(0, demandas_filas[i] - filas_cumplidas[i]) for i in range(n))
    columna_incumplida = sum(max(0, demandas_columnas[j] - columnas_cumplidas[j]) for j in range(m))
    return fila_incumplida + columna_incumplida

def verificar_adyacencia(tablero, fila, columna, n, m):
    """Verifica si una casilla está adyacente a un barco ya colocado."""
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nf, nc = fila + df, columna + dc
            if 0 <= nf < n and 0 <= nc < m and tablero[nf][nc] == 1:
                return False
    return True

def verificar_posicion(tablero, barco, fila, columna, orientacion, filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
    """Verifica si un barco se puede colocar en una posición dada considerando todas las restricciones."""
    if orientacion == "H":
        if columna + barco > m or filas_cumplidas[fila] + barco > demandas_filas[fila]:
            return False
        for col in range(barco):
            if (tablero[fila][columna + col] == 1 or 
                columnas_cumplidas[columna + col] + 1 > demandas_columnas[columna + col] or not verificar_adyacencia(tablero, fila, columna + col, n, m)):
                return False
    else:  # orientacion == "V"
        if fila + barco > n  or columnas_cumplidas[columna] + barco > demandas_columnas[columna]:
            return False
        for f in range(barco):
            if (tablero[f + fila][columna] == 1 or 
                filas_cumplidas[f + fila] + 1 > demandas_filas[f + fila] or not verificar_adyacencia(tablero, f + fila, columna, n, m)):
                return False
    return True

def colocar_barco(tablero, barco, fila, columna, orientacion, valor):
    """Coloca o retira un barco del tablero."""
    if orientacion == "H":
        for col in range(barco):
            tablero[fila][columna + col] = valor
    else:  # orientacion == "V"
        for f in range(barco):
            tablero[f + fila][columna] = valor

def actualizar_cumplidos(tablero, m, n):
    filas_cumplidas = [sum(tablero[i]) for i in range(n)]
    columnas_cumplidas = [sum(tablero[i][j] for i in range(n)) for j in range(m)]
    return filas_cumplidas, columnas_cumplidas

def backtrack(idx, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos):
    estado = (idx, tuple(map(tuple, tablero)))
    if estado in memo:
        return memo[estado]

    demanda_incumplida_actual = calcular_demanda_incumplida(filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m)
    if demanda_incumplida_actual >= mejor_solucion[0]:
        return float("inf")

    if idx == len(barcos):
        if demanda_incumplida_actual < mejor_solucion[0]:
            mejor_solucion[0] = demanda_incumplida_actual
            mejor_solucion[1] = [row[:] for row in tablero]
            mejor_solucion[2] = posiciones_barcos[:]
        return demanda_incumplida_actual

    barco = barcos[idx]
    for fila in range(n):
        for columna in range(m):
            for orientacion in ["H", "V"]:
                if verificar_posicion(tablero, barco, fila, columna, orientacion, filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
                    colocar_barco(tablero, barco, fila, columna, orientacion, 1)
                    posiciones_barcos[idx] = (
                        fila,
                        columna,
                        fila if orientacion == "H" else fila + barco - 1,
                        columna + barco - 1 if orientacion == "H" else columna
                    )
                    nuevas_filas, nuevas_columnas = actualizar_cumplidos(tablero, m, n)
                    backtrack(idx + 1, tablero, nuevas_filas, nuevas_columnas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos)
                    colocar_barco(tablero, barco, fila, columna, orientacion, 0)
                    posiciones_barcos[idx] = None

    # Asegurarse de que incluso los barcos más pequeños (tamaño 1) sean considerados.
    resultado = backtrack(idx + 1, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos)
    memo[estado] = resultado
    return resultado

def resolver_tablero(n, m, barcos, demandas_filas, demandas_columnas):
    barcos.sort(reverse=True)  # Intentamos colocar primero los barcos grandes

    tablero = [[0] * m for _ in range(n)]
    filas_cumplidas, columnas_cumplidas = actualizar_cumplidos(tablero, m, n)
    mejor_solucion = [float("inf"), [], []]  # [demanda_incumplida, tablero_optimo, posiciones_barcos]
    memo = {}
    posiciones_barcos = [None] * len(barcos)

    backtrack(0, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos)

    tablero_optimo = mejor_solucion[1]
    tablero_formateado = [["-" if cell == 0 else "1" for cell in row] for row in tablero_optimo]

    return {
        "tablero_optimo": tablero_formateado,
        "demanda_cumplida": sum(demandas_filas) + sum(demandas_columnas) - mejor_solucion[0],
        "demanda_total": sum(demandas_filas) + sum(demandas_columnas),
        "posiciones_barcos": mejor_solucion[2],
    }


def main():
#30_25_25 deberia dar 202 pero da 150
#20_20_20 deberia dar 104 pero da 96
#12_12_21 deberia dar 46 pero da 40
#10_10_10 deberia dar 40 pero da 36
    n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("10_10_10.txt")
    solucion = resolver_tablero(n, m, barcos, demandas_filas, demandas_columnas)

    tablero = solucion["tablero_optimo"]
    demanda_cumplida = solucion["demanda_cumplida"]
    demanda_total = solucion["demanda_total"]
    posiciones_barcos = solucion["posiciones_barcos"]

    print("Tablero óptimo:")
    for fila in tablero:
        print(" ".join(fila))
    print("\nDemanda cumplida:", demanda_cumplida)
    print("Demanda total:", demanda_total)
    print("\nPosiciones de los barcos:")
    for idx, pos in enumerate(posiciones_barcos):
        if pos is not None:
            print(f"Barco {idx + 1}: ({pos[0]},{pos[1]}) -> ({pos[2]},{pos[3]})")
        else:
            print(f"Barco {idx + 1}: No colocado")
        

main()



