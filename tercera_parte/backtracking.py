from csv_casos import procesar_archivo

def calcular_demanda_incumplida(filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
        fila_incumplida = sum(max(0, demandas_filas[i] - filas_cumplidas[i]) for i in range(n))
        columna_incumplida = sum(max(0, demandas_columnas[j] - columnas_cumplidas[j]) for j in range(m))
        return fila_incumplida + columna_incumplida
    
def verificar_posicion(tablero, barco, fila, columna, orientacion, filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
    if orientacion == "H":
        if columna + barco > m:
            return False
        # Verificar que no haya barcos en el camino y no exceda las demandas de filas/columnas
        for col in range(barco):
            if tablero[fila][columna + col] == 1 or columnas_cumplidas[columna + col] + 1 > demandas_columnas[columna + col]:
                return False
        if filas_cumplidas[fila] + barco > demandas_filas[fila]:
            return False
    else:  # orientacion == "V"
        if fila + barco > n:
            return False
        # Verificar que no haya barcos en el camino y no exceda las demandas de filas/columnas
        for f in range(barco):
            if tablero[f + fila][columna] == 1 or filas_cumplidas[f + fila] + 1 > demandas_filas[f + fila]:
                return False
        if columnas_cumplidas[columna] + barco > demandas_columnas[columna]:
            return False
    return True

    
def colocar_barco(tablero, barco, fila, columna, orientacion, valor):
        if orientacion == "H":
            for col in range(barco):
                tablero[fila][col + columna] = valor
        else:  # orientacion == "V"
            for f in range(barco):
                tablero[f + fila][columna] = valor
                
def actualizar_cumplidos(tablero, m, n):
        filas_cumplidas = [sum(tablero[i]) for i in range(n)]
        columnas_cumplidas = [sum(tablero[i][j] for i in range(n)) for j in range(m)]
        return filas_cumplidas, columnas_cumplidas

def backtrack(idx, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas):
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
        return demanda_incumplida_actual

    barco = barcos[idx]
    for fila in range(n):
        for columna in range(m):
            for orientacion in ["H", "V"]:
                if verificar_posicion(tablero, barco, fila, columna, orientacion, filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
                    colocar_barco(tablero, barco, fila, columna, orientacion, 1)
                    nuevas_filas, nuevas_columnas = actualizar_cumplidos(tablero, m, n)
                    backtrack(idx + 1, tablero, nuevas_filas, nuevas_columnas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas)
                    colocar_barco(tablero, barco, fila, columna, orientacion, 0)

    resultado = backtrack(idx + 1, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas)
    memo[estado] = resultado
    return resultado

    
def resolver_tablero(n, m, barcos, demandas_filas, demandas_columnas):
    # Ordenar barcos por tamaño decreciente para reducir opciones
    barcos.sort(reverse=True)

    # Inicialización
    tablero = [[0] * m for _ in range(n)]
    filas_cumplidas, columnas_cumplidas = actualizar_cumplidos(tablero, m, n)
    mejor_solucion = [float("inf"), []]  # [demanda_incumplida, tablero_optimo]
    memo = {}

    # Llamada inicial al backtracking
    backtrack(0, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas)

    return {
        "tablero_optimo": mejor_solucion[1],
        "demanda_cumplida": sum(demandas_filas) + sum(demandas_columnas) - mejor_solucion[0],
        "demanda_total": sum(demandas_filas) + sum(demandas_columnas)
    }
    
    
def main():
    # Dimensiones del tablero
    n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("30_25_25.txt")
    # Resolver
    solucion = resolver_tablero(n, m, barcos, demandas_filas, demandas_columnas)

    # Imprimir resultados
    for key, value in solucion.items():
        print(f"{key}: {value}")

main()
#5_5_6 tiene que dar 18 y da 14
#12_12_21 tiene que dar 46 y da 40
#30_25_25 tiene que dar 202 y da 150


