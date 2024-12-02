import random
import numpy as np

def leer_casos_de_prueba(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo if not linea.startswith('#')]

        datos = [int(linea) for linea in lineas if linea]

        longitudes_secciones = []
        longitud_actual = 0
        
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.strip() == '':
                    if longitud_actual > 0:
                        longitudes_secciones.append(longitud_actual)
                        longitud_actual = 0
                elif not linea.startswith('#'):
                    longitud_actual += 1
        
        if longitud_actual > 0:
            longitudes_secciones.append(longitud_actual)

        n_filas = longitudes_secciones[0]
        n_columnas = longitudes_secciones[1]
        
        demandas_filas = datos[:n_filas]
        demandas_columnas = datos[n_filas:n_filas + n_columnas]
        longitudes_barcos = datos[n_filas + n_columnas:]
        
        return demandas_filas, demandas_columnas, longitudes_barcos
    
def print_tablero(tablero, demandas_filas, demandas_columnas):
    max_num = max(max(demandas_filas), max(demandas_columnas), 1)  
    ancho_celda = len(str(max_num)) + 2  

    encabezado_columnas = " " * (ancho_celda + 1)  
    encabezado_columnas += "".join(f"{col:>{ancho_celda}}" for col in demandas_columnas)
    separador = " " * (ancho_celda + 1) + "-" * (len(demandas_columnas) * ancho_celda)

    print(encabezado_columnas)
    print(separador)

    for demanda, fila in zip(demandas_filas, tablero):
        fila_str = "".join(f"{celda:>{ancho_celda}}" for celda in fila)
        print(f"{demanda:>{ancho_celda - 1}} | {fila_str}")


def generar_caso_de_prueba(offset, tamaño, num_barcos):
    n = tamaño
    offset = random.randint(-offset, offset) 
    m = n + offset
    
    longitud_maxima = min(n, m)  
    longitudes_barcos = []
    for _ in range(num_barcos):
        longitud = random.randint(1, longitud_maxima)
        longitudes_barcos.append(longitud)
    
    longitudes_barcos.sort(reverse=True)
    
    tablero = np.zeros((n, m), dtype=int)
    
    barcos_colocados = []
    for longitud in longitudes_barcos:
        colocado = False
        intentos = 0
        max_intentos = 50 
        
        while not colocado and intentos < max_intentos:
            es_horizontal = random.choice([True, False])
            
            if es_horizontal:
                if longitud > m:
                    intentos += 1
                    continue
                fila = random.randint(0, n-1)
                columna = random.randint(0, m-longitud)
                coordenadas = [(fila, columna+i) for i in range(longitud)]
            else:
                if longitud > n:
                    intentos += 1
                    continue
                fila = random.randint(0, n-longitud)
                columna = random.randint(0, m-1)
                coordenadas = [(fila+i, columna) for i in range(longitud)]
            
            valido = True
            for f, c in coordenadas:
                for df in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nf, nc = f + df, c + dc
                        if 0 <= nf < n and 0 <= nc < m and tablero[nf, nc] == 1:
                            valido = False
                            break
                    if not valido:
                        break
                if not valido:
                    break
            
            if valido:
                for f, c in coordenadas:
                    tablero[f, c] = 1
                colocado = True
                barcos_colocados.append(longitud)
            
            intentos += 1
        
    demandas_filas = [sum(fila) for fila in tablero]
    demandas_columnas = [sum(columna) for columna in tablero.T]
    
    for i in range(n):
        extra = random.randint(0, m - demandas_filas[i])
        demandas_filas[i] += extra
    
    for j in range(m):
        extra = random.randint(0, n - demandas_columnas[j])
        demandas_columnas[j] += extra
    
    return n, m, barcos_colocados, demandas_filas, demandas_columnas
