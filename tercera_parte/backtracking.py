
import copy
from csv_casos import procesar_archivo
import time

CELDA_DISPONIBLE = -1

def backtrack(matriz, barcos, idx, demanda_filas, demanda_columnas, suma_filas, suma_columnas, mejor_solucion, dicc_pos_filas, dicc_pos_columnas, suma_restantes, estados_visitados, posiciones_barcos):
    if idx >= len(barcos) or suma_columnas == 0 or suma_filas == 0 or barcos[-1][0] > suma_columnas or barcos[-1][0] > suma_filas:
        if suma_columnas + suma_filas < mejor_solucion[1]:
            mejor_solucion[0] = copy.deepcopy(matriz)
            mejor_solucion[1] = suma_columnas + suma_filas
            mejor_solucion[2] = copy.deepcopy(posiciones_barcos)  # Guardar las posiciones actuales
        return mejor_solucion
    
    barco = barcos[idx][0]
    estado_actual = (tuple(demanda_filas), tuple(demanda_columnas), barco)
    
    if estado_actual in estados_visitados:
        return estados_visitados[estado_actual]

    # Si no tengo posiciones para colocar el barco actual
    if len(dicc_pos_columnas[barco]) == 0 and len(dicc_pos_filas[barco]) == 0:
        return backtrack(matriz, barcos, idx + 1, demanda_filas, demanda_columnas, suma_filas, suma_columnas, mejor_solucion, dicc_pos_filas, dicc_pos_columnas, suma_restantes-barco, estados_visitados, posiciones_barcos)

    # Si la suma de las demandas incumplidas hasta ahora más la demanda que me queda por cumplir
    # es mayor o igual a la mejor solución encontrada hasta el momento, corto la rama
    if (suma_columnas + suma_filas) - (2 * suma_restantes) >= mejor_solucion[1]:
        return mejor_solucion
    
    # Recorremos las posiciones disponibles para el barco en filas
    pos_disponibles_filas = dicc_pos_filas[barco].copy()
    
    for (fil_disponible, col_disponible) in pos_disponibles_filas:
        if matriz[fil_disponible][col_disponible] != CELDA_DISPONIBLE or demanda_columnas[col_disponible] == 0 or demanda_filas[fil_disponible] < barco:
                continue
        # Intentamos colocar el barco horizontalmente
        if adyacentes_libres(fil_disponible, col_disponible - barco + 1, fil_disponible, col_disponible, matriz, demanda_filas, demanda_columnas):
            dicc_pos_filas[barco].remove((fil_disponible, col_disponible))
            demanda_filas[fil_disponible] -= barco
            suma_filas -= barco
            suma_columnas -= barco
            for col in range(col_disponible - barco + 1, col_disponible + 1):
                matriz[fil_disponible][col] = barcos[idx][1]
                demanda_columnas[col] -= 1

            # Registramos la posición temporal del barco
            posiciones_barcos[barcos[idx][1]] = (fil_disponible, col_disponible - barco + 1, fil_disponible, col_disponible)
            
            mejor_solucion = backtrack(matriz, barcos, idx + 1, demanda_filas, demanda_columnas, suma_filas, suma_columnas, mejor_solucion, dicc_pos_filas, dicc_pos_columnas, suma_restantes - barco, estados_visitados, posiciones_barcos)
            
            # Deshacer cambios
            dicc_pos_filas[barco].add((fil_disponible, col_disponible))
            demanda_filas[fil_disponible] += barco
            suma_filas += barco
            suma_columnas += barco
            posiciones_barcos[barcos[idx][1]] = None
            for col in range(col_disponible - barco + 1, col_disponible + 1):
                matriz[fil_disponible][col] = CELDA_DISPONIBLE
                demanda_columnas[col] += 1
            
            if mejor_solucion[1] == 0:
                return mejor_solucion

    # Recorremos las posiciones disponibles para el barco en columnas
    pos_disponibles_columnas = dicc_pos_columnas[barco].copy()
    for (fil_disponible, col_disponible) in pos_disponibles_columnas:
        if matriz[fil_disponible][col_disponible] != CELDA_DISPONIBLE or demanda_columnas[col_disponible] < barco or demanda_filas[fil_disponible] == 0:
            continue
        
        if adyacentes_libres(fil_disponible - barco + 1, col_disponible, fil_disponible, col_disponible, matriz, demanda_filas, demanda_columnas):
            # Intentamos colocar el barco verticalmente
            dicc_pos_columnas[barco].remove((fil_disponible, col_disponible))
            demanda_columnas[col_disponible] -= barco
            suma_filas -= barco
            suma_columnas -= barco
            for fil in range(fil_disponible - barco + 1, fil_disponible + 1):
                matriz[fil][col_disponible] = barcos[idx][1]
                demanda_filas[fil] -= 1
            
            # Registramos la posición temporal del barco
            posiciones_barcos[barcos[idx][1]] = (fil_disponible - barco + 1, col_disponible, fil_disponible, col_disponible)
            
            mejor_solucion = backtrack(matriz, barcos, idx + 1, demanda_filas, demanda_columnas, suma_filas, suma_columnas, mejor_solucion, dicc_pos_filas, dicc_pos_columnas, suma_restantes - barco, estados_visitados, posiciones_barcos)
            
            # Deshacer cambios
            dicc_pos_columnas[barco].add((fil_disponible, col_disponible))
            demanda_columnas[col_disponible] += barco
            suma_filas += barco
            suma_columnas += barco
            posiciones_barcos[barcos[idx][1]] = None

            for fil in range(fil_disponible - barco + 1, fil_disponible + 1):
                matriz[fil][col_disponible] = CELDA_DISPONIBLE
                demanda_filas[fil] += 1
            
            if mejor_solucion[1] == 0:
                return mejor_solucion

    estados_visitados[estado_actual] = backtrack(matriz, barcos, idx + 1, demanda_filas, demanda_columnas, suma_columnas, suma_filas, mejor_solucion, dicc_pos_filas, dicc_pos_columnas, suma_restantes - barco, estados_visitados, posiciones_barcos)
    return estados_visitados[estado_actual]

def adyacentes_libres(i_inicial, j_inicial, i_final, j_final, matriz, filas, columnas):
    for i in range(i_inicial, i_final+1):
        if filas[i] == 0:
            return False
        
        for j in range(j_inicial, j_final+1):
            if matriz[i][j] != CELDA_DISPONIBLE:
                return False
            if columnas[j] == 0:
                return False
            if (j+1 < len(columnas) and matriz[i][j+1] != CELDA_DISPONIBLE) or (j-1 >= 0 and matriz[i][j-1] != CELDA_DISPONIBLE):
                return False
            if (i+1 < len(filas) and matriz[i+1][j] != CELDA_DISPONIBLE) or (i-1 >= 0 and matriz[i-1][j] != CELDA_DISPONIBLE):
                return False
    return True

def buscar_largos_para_posicion(i, j, columnas, filas, dicc_posiciones_columnas, dicc_posiciones_filas, largo, max_barco):
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

def ordenar_barcos_con_posicion(barcos):
    barcos_ordenados = []
    for i in range(len(barcos)):
        barcos_ordenados.append([barcos[i], i])
    # Ordeno los barcos de mayor a menor
    return sorted(barcos_ordenados, key= lambda x:x[0],reverse=True)

def resolver_tablero(barcos, filas, columnas, demandas_filas, demandas_columnas):
    matriz = [[CELDA_DISPONIBLE]*len(columnas) for _ in filas]
    posiciones_barcos = {i: None for i in range(len(barcos))}
    mejor_solucion =[copy.deepcopy(matriz), demandas_filas + demandas_columnas, posiciones_barcos]
    barcos = ordenar_barcos_con_posicion(barcos)
    dicc_posiciones_filas = {}
    dicc_posiciones_columnas = {}
    max_barco = barcos[0][0]

    for largo in range(1, max_barco+1):
        dicc_posiciones_filas[largo] = set()
        dicc_posiciones_columnas[largo] = set()
    
    for i in range(len(filas)):
        for j in range(len(columnas)):
            dicc_posiciones_columnas, dicc_posiciones_filas = buscar_largos_para_posicion(
                i, j, columnas, filas, dicc_posiciones_columnas, dicc_posiciones_filas, largo, max_barco
            )
    
    estados_visitados = {}
    solucion = backtrack(
        matriz, barcos, 0, filas, columnas, demandas_filas, demandas_columnas,
        mejor_solucion, dicc_posiciones_filas, dicc_posiciones_columnas,
        sum(barco[0] for barco in barcos), estados_visitados, posiciones_barcos
    )

    demanda_cumplida = demandas_filas + demandas_columnas - solucion[1]
    return {
        "tablero_optimo": solucion[0],
        "demanda_cumplida": demanda_cumplida,
        "demanda_total": demandas_filas + demandas_columnas,
        "posiciones_barcos": solucion[2]
    }

def main():
    # Cambiar el nombre del archivo según el caso
    barcos, filas, columnas = procesar_archivo("12_12_21.txt")
    demandas_filas = sum(filas)
    demandas_columnas = sum(columnas)
    
    start = time.time()
    solucion = resolver_tablero(barcos, filas, columnas, demandas_filas, demandas_columnas)
    end = time.time()
    
    tablero = solucion["tablero_optimo"]
    tablero_formateado = [[" - " if celda == -1 else f" {str(celda)} "  for celda in fila] for fila in tablero]
    demanda_cumplida = solucion["demanda_cumplida"]
    demanda_total = solucion["demanda_total"]
    posiciones_barcos = solucion["posiciones_barcos"]

    print("Tablero óptimo:")
    for fila in tablero_formateado:
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