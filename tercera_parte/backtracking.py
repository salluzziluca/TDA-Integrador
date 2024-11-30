
import copy
from csv_casos import procesar_archivo
import time

LUGAR_LIBRE = -1
#100% funcional, por si acaso no tocar
#corre los tests de la catedra en 80segs aprox.
                
                
def adyacentes_libres(i_inicial, j_inicial, i_final, j_final, matriz, filas, columnas):
    for i in range(i_inicial, i_final+1):
        if filas[i] == 0:
            return False
        
        for j in range(j_inicial, j_final+1):
            if matriz[i][j] != LUGAR_LIBRE:
                return False
            if columnas[j] == 0:
                return False
            if (j+1 < len(columnas) and matriz[i][j+1] != LUGAR_LIBRE) or (j-1 >= 0 and matriz[i][j-1] != LUGAR_LIBRE):
                return False
            if (i+1 < len(filas) and matriz[i+1][j] != LUGAR_LIBRE) or (i-1 >= 0 and matriz[i-1][j] != LUGAR_LIBRE):
                return False
    return True

def backtrack(matriz, barcos, idx, filas, columnas, suma_filas, suma_columnas, mejor, dicc_pos_filas, dicc_pos_columnas, suma_restantes, estados_visitados, posiciones_barcos):
    if idx >= len(barcos) or suma_columnas == 0 or suma_filas == 0 or barcos[-1][0] > suma_columnas or barcos[-1][0] > suma_filas:
        return (copy.deepcopy(matriz), suma_columnas+suma_filas) if suma_columnas+suma_filas < mejor[1] else mejor
    
    barco = barcos[idx][0]
    estado_actual =(tuple(filas), tuple(columnas), barco)
    
    if estado_actual in estados_visitados:
        return estados_visitados[estado_actual]

    # Si no tengo posiciones para colocar el barco actual
    if len(dicc_pos_columnas[barco]) == 0 and len(dicc_pos_filas[barco]) == 0:
        return backtrack(matriz, barcos, idx+1, filas, columnas, suma_filas, suma_columnas, mejor, dicc_pos_filas, dicc_pos_columnas, suma_restantes-barco, estados_visitados, posiciones_barcos)

    # Si la suma de las demandas incumplidas hasta ahora más la demanda que me queda por cumplir
    # es mayor o igual a la mejor solución encontrada hasta el momento, corto la rama
    if suma_columnas-suma_restantes + suma_filas-suma_restantes >= mejor[1]:
        return mejor
    
    # Recorremos las posiciones disponibles para el barco en filas
    posiciones_filas = dicc_pos_filas[barco].copy()
    for (i,j) in posiciones_filas:
        if matriz[i][j] != LUGAR_LIBRE or columnas[j] == 0 or filas[i] < barco:
                continue
        
        # Intentamos colocar el barco horizontalmente
        if adyacentes_libres(i, j-barco+1, i, j, matriz, filas, columnas):
            dicc_pos_filas[barco].remove((i,j))
            filas[i] -= barco
            suma_filas -= barco
            suma_columnas -= barco
            for col in range(j-barco+1, j+1):
                matriz[i][col] = barcos[idx][1]
                columnas[col] -= 1

            # Registramos la posición del barco en posiciones_barcos
            posiciones_barcos[idx] = (i, j-barco+1, i, j)
            
            mejor = backtrack(matriz, barcos, idx+1, filas, columnas, suma_filas, suma_columnas, mejor, dicc_pos_filas, dicc_pos_columnas, suma_restantes-barco, estados_visitados, posiciones_barcos)
            dicc_pos_filas[barco].add((i,j))
            filas[i] += barco
            suma_filas += barco
            suma_columnas += barco
            for col in range(j-barco+1, j+1):
                matriz[i][col] = LUGAR_LIBRE
                columnas[col] += 1
            
            if mejor[1] == 0:
                return mejor
        
    # Recorremos las posiciones disponibles para el barco en columnas
    posiciones_columnas = dicc_pos_columnas[barco].copy()
    for (i,j) in posiciones_columnas:      
        if matriz[i][j] != LUGAR_LIBRE or columnas[j] < barco or filas[i] == 0:
            continue
        
        if adyacentes_libres(i-barco+1, j, i, j, matriz, filas, columnas):
            dicc_pos_columnas[barco].remove((i,j))
            columnas[j] -= barco
            suma_filas -= barco
            suma_columnas -= barco
            for fil in range(i-barco+1, i+1):
                matriz[fil][j] = barcos[idx][1]
                filas[fil] -= 1
            
            # Registramos la posición del barco en posiciones_barcos
            posiciones_barcos[idx] = (i-barco+1, j, i, j)
            
            mejor = backtrack(matriz, barcos, idx+1, filas, columnas, suma_filas, suma_columnas, mejor, dicc_pos_filas, dicc_pos_columnas, suma_restantes-barco, estados_visitados, posiciones_barcos)
            dicc_pos_columnas[barco].add((i,j))
            columnas[j] += barco
            suma_filas += barco
            suma_columnas += barco
            for fil in range(i-barco+1, i+1):
                matriz[fil][j] = LUGAR_LIBRE
                filas[fil] += 1
            
            if mejor[1] == 0:
                return mejor
    
    estados_visitados[estado_actual] = backtrack(matriz, barcos, idx+1, filas, columnas, suma_columnas, suma_filas, mejor, dicc_pos_filas, dicc_pos_columnas, suma_restantes-barco, estados_visitados, posiciones_barcos)
    return estados_visitados[estado_actual]


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
    matriz = [[LUGAR_LIBRE]*len(columnas) for _ in filas]
    mejor = (copy.deepcopy(matriz), demandas_filas + demandas_columnas)
    barcos = ordenar_barcos_con_posicion(barcos)
    posiciones_barcos = {}
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
    matriz_optima, demanda_incumplida = backtrack(
        matriz, barcos, 0, filas, columnas, demandas_filas, demandas_columnas,
        mejor, dicc_posiciones_filas, dicc_posiciones_columnas,
        sum(barco[0] for barco in barcos), estados_visitados, posiciones_barcos
    )

    demanda_cumplida = demandas_filas + demandas_columnas - demanda_incumplida
    return {
        "tablero_optimo": matriz_optima,
        "demanda_cumplida": demanda_cumplida,
        "demanda_total": demandas_filas + demandas_columnas,
        "posiciones_barcos": posiciones_barcos
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
    tablero_formateado = [["-" if cell == -1 else str(cell) for cell in row] for row in tablero]
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
            print(f"Barco {idx + 1}: ({pos[0]},{pos[1]}) -> ({pos[2]},{pos[3]})")
        else:
            print(f"Barco {idx + 1}: No colocado")

main()