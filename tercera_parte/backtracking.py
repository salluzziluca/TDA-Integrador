'''Condicion de barco:
-si no hay ni un barco.
-si la cant de fil y col se pasan de la cant pedida.
-las filas y cols pedidas sean adyacentes. '''

import numpy as np
from csv_casos import procesar_archivo


def calcular_demanda_incumplida(tablero, demandas_filas, demandas_columnas):
    incumplida = 0
    cumplida = 0
    filas_ocupadas = np.sum(tablero, axis=1)
    columnas_ocupadas = np.sum(tablero, axis=0)
    
    for i in range(len(demandas_filas)):
        if filas_ocupadas[i] < demandas_filas[i]:
            incumplida += demandas_filas[i] - filas_ocupadas[i]
        cumplida += min(filas_ocupadas[i], demandas_filas[i])
    
    for j in range(len(demandas_columnas)):
        if columnas_ocupadas[j] < demandas_columnas[j]:
            incumplida += demandas_columnas[j] - columnas_ocupadas[j]
        cumplida += min(columnas_ocupadas[j], demandas_columnas[j])
    
    return incumplida, cumplida

def es_valido(tablero, fila, columna, longitud, orientacion, demandas_filas, demandas_columnas):
    n, m = tablero.shape
    if orientacion == "H":
        if columna + longitud > m:
            return False
        for j in range(columna, columna + longitud):
            if tablero[fila, j] == 1 or np.sum(tablero[:, j]) + 1 > demandas_columnas[j]:
                return False
        if np.sum(tablero[fila, :]) + longitud > demandas_filas[fila]:
            return False
    elif orientacion == "V":
        if fila + longitud > n:
            return False
        for i in range(fila, fila + longitud):
            if tablero[i, columna] == 1 or np.sum(tablero[i, :]) + 1 > demandas_filas[i]:
                return False
        if np.sum(tablero[:, columna]) + longitud > demandas_columnas[columna]:
            return False
    return True

def colocar_barco(tablero, fila, columna, longitud, orientacion, valor):
    if orientacion == "H":
        tablero[fila, columna:columna + longitud] = valor
    elif orientacion == "V":
        tablero[fila:fila + longitud, columna] = valor

def backtrack(tablero, barcos, demandas_filas, demandas_columnas, index, mejor_solucion, posiciones_actuales):
    if index == len(barcos):
        incumplida, cumplida = calcular_demanda_incumplida(tablero, demandas_filas, demandas_columnas)
        if incumplida < mejor_solucion[1]:
            mejor_solucion[0] = np.copy(tablero)
            mejor_solucion[1] = incumplida
            mejor_solucion[2] = list(posiciones_actuales)
            mejor_solucion[3] = cumplida
        return

    longitud = barcos[index]
    n, m = tablero.shape
    for fila in range(n):
        for columna in range(m):
            for orientacion in ["H", "V"]:
                if es_valido(tablero, fila, columna, longitud, orientacion, demandas_filas, demandas_columnas):
                    colocar_barco(tablero, fila, columna, longitud, orientacion, 1)
                    posiciones_actuales.append((fila, columna))
                    backtrack(tablero, barcos, demandas_filas, demandas_columnas, index + 1, mejor_solucion, posiciones_actuales)
                    colocar_barco(tablero, fila, columna, longitud, orientacion, 0)
                    posiciones_actuales.pop()

def resolver_problema(n, m, barcos, demandas_filas, demandas_columnas):
    tablero = np.zeros((n, m), dtype=int)
    mejor_solucion = [None, float("inf"), [], 0]  # [mejor_tablero, demanda_incumplida, posiciones, demanda_cumplida]
    backtrack(tablero, barcos, demandas_filas, demandas_columnas, 0, mejor_solucion, [])
    return mejor_solucion


def main():
    # Dimensiones del tablero
    n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("3_3_2.txt")
    print(n, m, barcos, demandas_filas, demandas_columnas)
    # Resolver
    solucion = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)

    # Imprimir resultados
    print("Mejor tablero encontrado:")
    print(solucion[0])
    print("Posiciones de los barcos:")
    for i, pos in enumerate(solucion[2]):
        print(f"{i}: {pos}")
    print("Demanda cumplida:", solucion[3])
    print("Demanda total:", sum(demandas_filas) + sum(demandas_columnas))

#main()
