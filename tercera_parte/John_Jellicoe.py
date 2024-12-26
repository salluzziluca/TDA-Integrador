import numpy as np

def puede_poner_barco(tablero, n, m, x, y, largo, es_horizontal):
    if es_horizontal:
        if y + largo > m:  
            return False
        for i in range(largo): # revisar adyacentes si es horizontal
            if tablero[x, y + i] == 1 or \
                (x > 0 and tablero[x - 1, y + i] == 1) or \
                (x < n - 1 and tablero[x + 1, y + i] == 1) or \
                (x > 0 and y + i > 0 and tablero[x - 1, y + i - 1] == 1) or \
                (x > 0 and y + i < m - 1 and tablero[x - 1, y + i + 1] == 1) or \
                (x < n - 1 and y + i > 0 and tablero[x + 1, y + i - 1] == 1) or \
                (x < n - 1 and y + i < m - 1 and tablero[x + 1, y + i + 1] == 1):
                return False
        if y > 0 and tablero[x, y - 1] == 1:
            return False
        if y + largo < m and tablero[x, y + largo] == 1:
            return False
    else:  
        if x + largo > n:  
            return False
        for i in range(largo): # revisar adyacentes si no es horizontal           
            if tablero[x + i, y] == 1 or \
                (y > 0 and tablero[x + i, y - 1] == 1) or \
                (y < m - 1 and tablero[x + i, y + 1] == 1) or \
                (x + i > 0 and y > 0 and tablero[x + i - 1, y - 1] == 1) or \
                (x + i > 0 and y < m - 1 and tablero[x + i - 1, y + 1] == 1) or \
                (x + i < n - 1 and y > 0 and tablero[x + i + 1, y - 1] == 1) or \
                (x + i < n - 1 and y < m - 1 and tablero[x + i + 1, y + 1] == 1):
                return False
        if x > 0 and tablero[x - 1, y] == 1:
            return False
        if x + largo < n and tablero[x + largo, y] == 1:
            return False
    return True

def colocar_barco(tablero, x, y, largo, es_horizontal):
    if es_horizontal:
        for i in range(largo):
            tablero[x, y + i] = 1
    else:
        for i in range(largo):
            tablero[x + i, y] = 1

def algoritmo_JJ(n, m, largo_barcos, filas_restricciones, col_restricciones):
    tablero = np.zeros((n, m), dtype=int)

    barcos = sorted(largo_barcos, reverse=True) # O(k log k)

    while barcos:
        filas_demandas = [(i, filas_restricciones[i]) for i in range(n) if filas_restricciones[i] > 0] # O(n+m)
        col_demandas = [(j, col_restricciones[j]) for j in range(m) if col_restricciones[j] > 0] # O(n+m)

        if not filas_demandas and not col_demandas:
            break  

        barco_colocado = False  # para verificar si el barco se colocó en esta iteración

        for barco in barcos:
            # Intentar colocar el barco en una fila
            if filas_demandas and (not col_demandas or max(filas_demandas, key=lambda x: x[1])[1] >= max(col_demandas, key=lambda x: x[1])[1]):
                fila_i = max(filas_demandas, key=lambda x: x[1])[0]
                if filas_restricciones[fila_i] >= barco:  # Verificar si la fila puede acomodar el barco
                    for columna_inicio in range(m):
                        if all(0 <= columna_inicio + i < m and col_restricciones[columna_inicio + i] > 0 for i in range(barco)) and puede_poner_barco(tablero, n, m, fila_i, columna_inicio, barco, True):
                            colocar_barco(tablero, fila_i, columna_inicio, barco, True)
                            filas_restricciones[fila_i] -= barco
                            for i in range(barco):
                                col_restricciones[columna_inicio + i] -= 1
                            barcos.remove(barco)
                            barco_colocado = True
                            break
                if barco_colocado:
                    break


            # Intentar colocar el barco en una columna
            if col_demandas and not barco_colocado:
                columna_i = max(col_demandas, key=lambda x: x[1])[0]
                if col_restricciones[columna_i] >= barco:  # Verificar si la columna puede acomodar el barco
                    for fila_inicio in range(n):
                        if all(0 <= fila_inicio + i < n and filas_restricciones[fila_inicio + i] > 0 for i in range(barco)) and puede_poner_barco(tablero, n, m, fila_inicio, columna_i, barco, False):
                            colocar_barco(tablero, fila_inicio, columna_i, barco, False)
                            col_restricciones[columna_i] -= barco
                            for i in range(barco):
                                filas_restricciones[fila_inicio + i] -= 1
                            barcos.remove(barco)
                            barco_colocado = True
                            break
                if barco_colocado:
                    break


        # Si no se pudo colocar ningún barco en esta iteración, salimos del bucle
        if not barco_colocado:
            break

    demanda_restante = sum(filas_restricciones) + sum(col_restricciones)
    return tablero, demanda_restante

def obtener_posiciones_barcos(tablero):
    """
    Extrae las posiciones de los barcos en el tablero.
    Devuelve una lista de barcos con sus coordenadas.
    """
    n, m = tablero.shape
    barcos = []
    visitados = set()
    
    for i in range(n):
        for j in range(m):
            if tablero[i, j] == 1 and (i, j) not in visitados:
                # Detectar un barco
                barco = []
                x, y = i, j
                
                # Verificar si es horizontal
                if j + 1 < m and tablero[x, y + 1] == 1:
                    while y < m and tablero[x, y] == 1:
                        barco.append((x, y))
                        visitados.add((x, y))
                        y += 1
                # Si no es horizontal, es vertical
                elif i + 1 < n and tablero[x + 1, y] == 1:
                    while x < n and tablero[x, y] == 1:
                        barco.append((x, y))
                        visitados.add((x, y))
                        x += 1
                else:
                    barco.append((x, y))
                    visitados.add((x, y))
                    
                barcos.append(barco)
    
    return barcos
