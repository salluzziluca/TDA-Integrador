from csv_casos import procesar_archivo
import time
def ordenar_barcos_con_posicion(barcos):
    barcos_indexados = []
    for i in range(len(barcos)):
        barcos_indexados.append([barcos[i], i])
    # Ordeno los barcos de mayor a menor
    return sorted(barcos_indexados, key= lambda x:x[0],reverse=True)
    
    prioridades = []
    for barco in barcos:
        prioridad_filas = sum(1 for i in range(n) if demandas_filas[i] > filas_cumplidas[i] and demandas_filas - filas_cumplidas >= barco)
        prioridad_columnas = sum(1 for j in range(m) if demandas_columnas[j] > columnas_cumplidas[j] and demandas_columnas[j] - columnas_cumplidas[j] >= barco)
        prioridades.append(barco, prioridad_filas + prioridad_columnas)
    
    prioridades.sort(key=lambda x: (-x[1], -x[0]))
    return [barco for barco, _ in prioridades]

def actualizar_cumplidos(tablero, m, n):
    filas_cumplidas = [sum(tablero[i]) for i in range(n)]
    columnas_cumplidas = [sum(tablero[i][j] for i in range(n)) for j in range(m)]
    return filas_cumplidas, columnas_cumplidas

def calcular_demanda_incumplida(filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m, tablero, barcos_colocados):
    fila_incumplida = sum(abs(demandas_filas[i] - filas_cumplidas[i]) for i in range(n))
    columna_incumplida = sum(abs(demandas_columnas[j] - columnas_cumplidas[j]) for j in range(m))
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
            if (tablero[fila][columna + col] == 1 or columnas_cumplidas[columna + col] + 1 > demandas_columnas[columna + col] or not verificar_adyacencia(tablero, fila, columna + col, n, m)):
                return False
    else:  # orientacion == "V"
        if fila + barco > n  or columnas_cumplidas[columna] + barco > demandas_columnas[columna]:
            return False
        for f in range(barco):
            if (tablero[f + fila][columna] == 1 or filas_cumplidas[f + fila] + 1 > demandas_filas[f + fila] or not verificar_adyacencia(tablero, f + fila, columna, n, m)):
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

def backtrack(idx, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos, barcos_colocados):
    estado = (idx, tuple(map(tuple, tablero)))
    if estado in memo:
        return memo[estado]
    
    if mejor_solucion[0] == 0:
        return mejor_solucion[0]
    
    demanda_incumplida_actual = calcular_demanda_incumplida(filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m, tablero, barcos_colocados)

    if demanda_incumplida_actual - (sum(barcos[idx:]) * 2)  > mejor_solucion[0]:
        return float("inf")

    if idx == len(barcos):
        if demanda_incumplida_actual < mejor_solucion[0]:
            mejor_solucion[0] = demanda_incumplida_actual
            mejor_solucion[1] = [row[:] for row in tablero]
            mejor_solucion[2] = posiciones_barcos.copy()
        return demanda_incumplida_actual

    barco = barcos[idx]
    for fila in range(n):
        for columna in range(m):
            for orientacion in ["H", "V"]:
                if verificar_posicion(tablero, barco, fila, columna, orientacion, filas_cumplidas, columnas_cumplidas, demandas_filas, demandas_columnas, n, m):
                    colocar_barco(tablero, barco, fila, columna, orientacion, 1)
                    posiciones_barcos[idx] = (fila, columna, fila if orientacion == "H" else fila + barco - 1, columna + barco - 1 if orientacion == "H" else columna)
                   # if orientacion == "H":
                    #    suma_columnas_nueva = suma_columnas + barco
                     #   suma_filas_nueva = suma_filas + 1
                      #  nuevas_filas[fila] =  filas_cumplidas[fila] + 1
                       # for col in range(barco):
                        #    nuevas_columnas[columna + col] = columnas_cumplidas[columna + col] + 1
                            
                    #else:  # orientacion == "V"
                       # suma_columnas_nueva = suma_columnas + 1
                        #suma_filas_nueva = suma_filas + barco
                        #nuevas_columnas[fila] = columnas_cumplidas[fila] + 1
                        #for f in range(barco):
                         #   nuevas_filas[fila + f] = filas_cumplidas[fila + f] + 1
                    nuevas_filas, nuevas_columnas = actualizar_cumplidos(tablero, m, n)
                    backtrack(idx + 1, tablero, nuevas_filas, nuevas_columnas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos, barcos_colocados)
                    colocar_barco(tablero, barco, fila, columna, orientacion, 0)
                    posiciones_barcos[idx] = None

    # Considera no colocar el barco actual
    resultado = backtrack(idx + 1, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos, barcos_colocados)
    # Guarda el resultado en la tabla de memoización
    memo[estado] = resultado
    return resultado

def resolver_tablero(n, m, barcos, demandas_filas, demandas_columnas):
    barcos.sort(reverse=True)
    #ordenar_barcos_con_posicion(barcos)

    tablero = [[0] * m for _ in range(n)]
    filas_cumplidas, columnas_cumplidas = actualizar_cumplidos(tablero, m, n)
   # nuevas_filas, nuevas_columnas = actualizar_cumplidos(tablero, m, n)
    #suma_filas = 0
    #suma_columnas = 0
    demanda_total = sum(demandas_filas) + sum(demandas_columnas)
    mejor_solucion = [float("inf"), [], []]  # [demanda_incumplida, tablero_optimo, posiciones_barcos]
    memo = {}
    posiciones_barcos = {i: None for i in range(len(barcos))}
    barcos_colocados = set()

    backtrack(0, tablero, filas_cumplidas, columnas_cumplidas, memo, mejor_solucion, barcos, n, m, demandas_filas, demandas_columnas, posiciones_barcos, barcos_colocados)

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
#12_12_21 deberia dar 46 pero da 40 demanda_filas = [3, 6, 1, 2, 3, 6, 5, 2, 0, 3, 0, 3], barcos = [4, 3, 7, 4, 3, 2, 2, 5, 5, 5, 4, 4, 5, 5, 7, 6, 4, 1, 7, 7, 4], demanda_columnas = [3, 0, 1, 1, 3, 1, 0, 3, 3, 4, 1, 4]
#10_10_10 deberia dar 40 pero da 36 demanda_filas = [2, 4, 2, 1, 1, 2, 3, 0], barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1], demanda_columnas = [1, 2, 1, 3, 2, 2, 3, 1, 5, 0]

    n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("12_12_21.txt")
    start = time.time()
    solucion = resolver_tablero(n, m, barcos, demandas_filas, demandas_columnas)
    end = time.time()
    

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
    for idx, pos in posiciones_barcos.items():
        if pos is not None:
            print(f"Barco {idx + 1}: ({pos[0]},{pos[1]}) -> ({pos[2]},{pos[3]})")
        else:
            print(f"Barco {idx + 1}: No colocado")
            
    print(end - start)
        

main()



