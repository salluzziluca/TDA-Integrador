import time
from backtracking import resolver_tablero
from csv_casos import procesar_archivo

# python tercera_parte/main_BT.py tercera_parte/casos_test/3_3_2.txt
# python tercera_parte/main_BT.py tercera_parte/casos_test/8_7_10.txt
# python tercera_parte/main_BT.py tercera_parte/casos_test/10_3_3.txt
# python tercera_parte/main_BT.py tercera_parte/casos_test/12_12_21.txt
# python tercera_parte/main_BT.py tercera_parte/casos_test/20_20_20.txt
# python tercera_parte/main_BT.py tercera_parte/casos_test/30_25_25.txt
def main(nombre_archivo):
    # Cambiar el nombre del archivo según el caso
    barcos, filas, columnas = procesar_archivo(nombre_archivo)
    demandas_filas = sum(filas)
    demandas_columnas = sum(columnas)
    
    start = time.time()
    solucion = resolver_tablero(barcos, filas, columnas, demandas_filas, demandas_columnas)
    end = time.time()
    
    tablero = solucion["matriz_optimo"]
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

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('nombre_archivo', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.nombre_archivo)

