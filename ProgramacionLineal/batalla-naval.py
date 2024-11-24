from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary, PULP_CBC_CMD
import numpy as np
import time

# Parámetros del problema
n, m = 6, 6  # Dimensiones del tablero
k = 3         # Número de barcos
barcos = [3, 2, 1]  # Longitud de cada barco


restricciones_filas = [3, 2, 1, 1, 1, 2]
restricciones_columnas = [2, 1, 2, 1, 2, 1]

problema = LpProblem("Batalla_Naval", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(m)), cat=LpBinary)
y = LpVariable.dicts("y", ((b, i, j, o) for b in range(k) 
                           for i in range(n) 
                           for j in range(m) 
                           for o in ["H", "V"]), cat=LpBinary)

problema += 0

# Restricción de consumo de filas
for i in range(n):
    problema += lpSum(x[i, j] for j in range(m)) == restricciones_filas[i]

# Restricción de consumo de columnas
for j in range(m):
    problema += lpSum(x[i, j] for i in range(n)) == restricciones_columnas[j]

# Cada barco debe ser colocado exactamente una vez
for b in range(k):
    problema += lpSum(y[b, i, j, o] for i in range(n) for j in range(m) for o in ["H", "V"]) == 1

# Restricción de dimensiones y ocupación
for b, tam in enumerate(barcos):
    for i in range(n):
        for j in range(m):
            # Horizontal
            if j + tam <= m:
                problema += y[b, i, j, "H"] <= lpSum(x[i, j + l] for l in range(tam))
            else:
                problema += y[b, i, j, "H"] == 0
            
            # Vertical
            if i + tam <= n:
                problema += y[b, i, j, "V"] <= lpSum(x[i + l, j] for l in range(tam))
            else:
                problema += y[b, i, j, "V"] == 0

# Separación entre barcos (corregida)
for i in range(n):
    for j in range(m):
        # Vecinos de la casilla (i, j)
        vecinos = [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1),             (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)
        ]
        problema += lpSum(x[i_, j_] for i_, j_ in vecinos if 0 <= i_ < n and 0 <= j_ < m) <= 1 - x[i, j]

inicio = time.time()
problema.solve(PULP_CBC_CMD(msg=False))
tiempo_lp = time.time() - inicio

solucion = np.zeros((n, m), dtype=int)
for i in range(n):
    for j in range(m):
        if x[i, j].varValue > 0.5:
            solucion[i, j] = 1

# Mostrar resultados
print("Tablero solucionado:")
print(solucion)
print(f"Tiempo de resolución (Programación Lineal): {tiempo_lp:.4f} segundos")
