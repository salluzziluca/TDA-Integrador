
import copy
from csv_casos import procesar_archivo
import time

CELDA_DISPONIBLE = -1

def backtrack(matriz, barcos, idx, demanda_filas, demanda_columnas, suma_filas, suma_columnas, mejor_solucion, posiciones_por_fila, posiciones_por_columna, demanda_restante, visitados, posiciones_barcos):
    if (idx >= len(barcos) or suma_columnas == 0 or suma_filas == 0 or 
        barcos[-1][0] > suma_columnas or barcos[-1][0] > suma_filas):
        
        if suma_columnas + suma_filas < mejor_solucion[1]:
            mejor_solucion[0] = copy.deepcopy(matriz)
            mejor_solucion[1] = suma_columnas + suma_filas
            mejor_solucion[2] = copy.deepcopy(posiciones_barcos)
        return mejor_solucion

    barco = barcos[idx][0]
    estado_actual = (tuple(demanda_filas), tuple(demanda_columnas), barco)

    if estado_actual in visitados:
        return visitados[estado_actual]

    # Si no hay posiciones disponibles para este barco
    if not posiciones_por_fila[barco] and not posiciones_por_columna[barco]:
        return backtrack(
            matriz, barcos, idx + 1, demanda_filas, demanda_columnas, 
            suma_filas, suma_columnas, mejor_solucion, posiciones_por_fila, 
            posiciones_por_columna, demanda_restante - barco, 
            visitados, posiciones_barcos
        )

    # Poda por demanda incumplida
    if (suma_columnas + suma_filas) - (2 * demanda_restante) >= mejor_solucion[1]:
        return mejor_solucion

    # Intentar colocar barco en las posiciones horizontales disponibles
    for fila, columna in list(posiciones_por_fila[barco]):
        if matriz[fila][columna] != CELDA_DISPONIBLE or demanda_columnas[columna] == 0 or demanda_filas[fila] < barco:
            continue

        if verificar_espacio_h(fila, columna, barco, matriz, demanda_filas, demanda_columnas):
            # Actualizar matriz y demandas
            registrar_barco_h(fila, columna, barco, matriz, demanda_filas, demanda_columnas, barcos[idx][1])
            
            # Registrar posición
            posiciones_barcos[barcos[idx][1]] = (fila, columna - barco + 1, fila, columna)

            mejor_solucion = backtrack(
                matriz, barcos, idx + 1, demanda_filas, demanda_columnas, 
                suma_filas - barco, suma_columnas - barco, 
                mejor_solucion, posiciones_por_fila, posiciones_por_columna, 
                demanda_restante - barco, visitados, posiciones_barcos
            )

            # Restaurar estado
            revertir_barco_h(fila, columna, barco, matriz, demanda_filas, demanda_columnas)
            posiciones_barcos[barcos[idx][1]] = None

            if mejor_solucion[1] == 0:
                return mejor_solucion

    # Intentar colocar barco en las posiciones verticales disponibles
    for fila, columna in list(posiciones_por_columna[barco]):
        if matriz[fila][columna] != CELDA_DISPONIBLE or demanda_columnas[columna] < barco or demanda_filas[fila] == 0:
            continue

        if verificar_espacio_v(fila, columna, barco, matriz, demanda_filas, demanda_columnas):
            # Actualizar matriz y demandas
            registrar_barco_v(fila, columna, barco, matriz, demanda_filas, demanda_columnas, barcos[idx][1])
            
            # Registrar posición
            posiciones_barcos[barcos[idx][1]] = (fila - barco + 1, columna, fila, columna)

            mejor_solucion = backtrack(
                matriz, barcos, idx + 1, demanda_filas, demanda_columnas, 
                suma_filas - barco, suma_columnas - barco, 
                mejor_solucion, posiciones_por_fila, posiciones_por_columna, 
                demanda_restante - barco, visitados, posiciones_barcos
            )

            # Restaurar estado
            revertir_barco_v(fila, columna, barco, matriz, demanda_filas, demanda_columnas)
            posiciones_barcos[barcos[idx][1]] = None

            if mejor_solucion[1] == 0:
                return mejor_solucion

    visitados[estado_actual] = backtrack(
        matriz, barcos, idx + 1, demanda_filas, demanda_columnas, 
        suma_columnas, suma_filas, mejor_solucion, posiciones_por_fila, 
        posiciones_por_columna, demanda_restante - barco, 
        visitados, posiciones_barcos
    )
    return visitados[estado_actual]

def buscar_pos_disponibles_para_barcos(i, j, columnas, filas, dicc_posiciones_columnas, dicc_posiciones_filas, largo, max_barco):
    if filas[i] == 0 or columnas[j] == 0:
        return dicc_posiciones_columnas, dicc_posiciones_filas
    columnas_cumple = False
    filas_cumple = False
    if filas[i] > 0:
        dicc_posiciones_filas[1].add((i,j))
        filas_cumple = True
    if columnas[j] > 0:
        dicc_posiciones_columnas[1].add((i,j))
        columnas_cumple = True
    for largo in range(2, max_barco+1):
        if not filas_cumple and not columnas_cumple:
            break
        if columnas_cumple and (i, j-1) in dicc_posiciones_filas[largo-1] and filas[i] >= largo:
            dicc_posiciones_filas[largo].add((i,j))
        else:
            columnas_cumple = False
        if filas_cumple and (i-1, j) in dicc_posiciones_columnas[largo-1] and columnas[j] >= largo:
                dicc_posiciones_columnas[largo].add((i,j))
        else:
            filas_cumple = False
    return dicc_posiciones_columnas, dicc_posiciones_filas

def verificar_espacio_h(fila, columna, largo_barco, tablero, demandas_filas, demandas_columnas):
    # Verificar que no haya barcos en la fila
    for i in range(columna, columna - largo_barco, -1):
        if i < 0 or tablero[fila][i] != CELDA_DISPONIBLE:
            return False
        if fila > 0 and tablero[fila-1][i] != CELDA_DISPONIBLE:
            return False
        if fila < len(tablero)-1 and tablero[fila+1][i] != CELDA_DISPONIBLE:
            return False
    if columna - largo_barco >= 0 and tablero[fila][columna - largo_barco] != CELDA_DISPONIBLE:
        return False
    if columna < len(tablero[0])-1 and tablero[fila][columna+1] != CELDA_DISPONIBLE:
        return False

    # Verificar demandas de fila y columna
    if demandas_filas[fila] < largo_barco:
        return False

    for i in range(columna, columna - largo_barco, -1):
        if demandas_columnas[i] <= 0:
            return False

    return True

def registrar_barco_h(fila, columna, largo_barco, tablero, demandas_filas, demandas_columnas, id_barco):
    for i in range(columna, columna - largo_barco, -1):
        tablero[fila][i] = id_barco
        demandas_filas[fila] -= 1
        demandas_columnas[i] -= 1

def revertir_barco_h(fila, columna, largo_barco, tablero, demandas_filas, demandas_columnas):
    for i in range(columna, columna - largo_barco, -1):
        tablero[fila][i] = CELDA_DISPONIBLE
        demandas_filas[fila] += 1
        demandas_columnas[i] += 1

def verificar_espacio_v(fila, columna, largo_barco, tablero, demandas_filas, demandas_columnas):
    # Verificar que no haya barcos en la columna
    for i in range(fila, fila - largo_barco, -1):
        if i < 0 or tablero[i][columna] != CELDA_DISPONIBLE:
            return False
        if columna > 0 and tablero[i][columna-1] != CELDA_DISPONIBLE:
            return False
        if columna < len(tablero[0])-1 and tablero[i][columna+1] != CELDA_DISPONIBLE:
            return False
        
    if fila - largo_barco >= 0 and tablero[fila - largo_barco][columna] != CELDA_DISPONIBLE:
        return False
    if fila < len(tablero)-1 and tablero[fila+1][columna] != CELDA_DISPONIBLE:
        return False

    # Verificar demandas de fila y columna
    if demandas_columnas[columna] < largo_barco:
        return False

    for i in range(fila, fila - largo_barco, -1):
        if demandas_filas[i] <= 0:
            return False

    return True

def registrar_barco_v(fila, columna, largo_barco, tablero, demandas_filas, demandas_columnas, id_barco):
    for i in range(fila, fila - largo_barco, -1):
        tablero[i][columna] = id_barco
        demandas_filas[i] -= 1
        demandas_columnas[columna] -= 1

def revertir_barco_v(fila, columna, largo_barco, tablero, demandas_filas, demandas_columnas):
    for i in range(fila, fila - largo_barco, -1):
        tablero[i][columna] = CELDA_DISPONIBLE
        demandas_filas[i] += 1
        demandas_columnas[columna] += 1

def ordenar_barcos_con_posicion(barcos):
    barcos_ordenados = []
    for i in range(len(barcos)):
        barcos_ordenados.append([barcos[i], i])
    # Ordeno los barcos de mayor a menor
    return sorted(barcos_ordenados, key= lambda x:x[0],reverse=True)

def resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas):
    matriz = [[CELDA_DISPONIBLE]*len(columnas) for _ in filas]
    
    posiciones_barcos = {i: None for i in range(len(barcos))}
    
    mejor_solucion = [copy.deepcopy(matriz), demanda_filas + demanda_columnas, posiciones_barcos]
    
    barcos = ordenar_barcos_con_posicion(barcos)
    
    pos_disponibles_filas = {}
    
    pos_disponibles_columnas = {}
    
    barco_mas_grande = barcos[0][0]

    for largo in range(1, barco_mas_grande+1):
        pos_disponibles_filas[largo] = set()
        pos_disponibles_columnas[largo] = set()
    
    for i in range(len(filas)):
        for j in range(len(columnas)):
            pos_disponibles_columnas, pos_disponibles_filas = buscar_pos_disponibles_para_barcos(
                i, j, columnas, filas, pos_disponibles_columnas, pos_disponibles_filas, largo, barco_mas_grande
            )
    
    visitados = {}
    solucion = backtrack(
        matriz, barcos, 0, filas, columnas, demanda_filas, demanda_columnas,
        mejor_solucion, pos_disponibles_filas, pos_disponibles_columnas,
        sum(barco[0] for barco in barcos), visitados, posiciones_barcos
    )

    demanda_cumplida = demanda_filas + demanda_columnas - solucion[1]
    return {
        "matriz_optimo": solucion[0],
        "demanda_cumplida": demanda_cumplida,
        "demanda_total": demanda_filas + demanda_columnas,
        "posiciones_barcos": solucion[2]
    }

"""
#ejemplo de un main para ejecutar la funcion
def main():
    # Cambiar el nombre del archivo según el caso
    barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/5_5_6.txt")
    demanda_filas = sum(filas)
    demanda_columnas = sum(columnas)
    
    start = time.time()
    solucion = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
    end = time.time()
    
    matriz = solucion["matriz_optimo"]
    matriz_formateado = [[" - " if celda == -1 else f" {str(celda)} "  for celda in fila] for fila in matriz]
    demanda_cumplida = solucion["demanda_cumplida"]
    demanda_total = solucion["demanda_total"]
    posiciones_barcos = solucion["posiciones_barcos"]

    print("matriz óptimo:")
    for fila in matriz_formateado:
        print(" ".join(map(str, fila)))
    print("\nDemanda cumplida:", demanda_cumplida)
    print("Demanda total:", demanda_total)
    print("\nTiempo de ejecución:", end - start, "segundos")

    # Imprimir las posiciones de los barcos
    print("\nPosiciones de los barcos:")
    for idx, pos in posiciones_barcos.items():
        if pos is not None:
            print(f"Barco {idx}: ({pos[0]},{pos[1]}) -> ({pos[2]},{pos[3]})")
        else:
            print(f"Barco {idx}: No colocado")

main()

"""