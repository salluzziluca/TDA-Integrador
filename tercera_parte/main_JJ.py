from John_Jellicoe import algoritmo_JJ, obtener_posiciones_barcos
from auxiliares import leer_casos_de_prueba, print_tablero

# python tercera_parte/main_JJ.py tercera_parte/casos_test/3_3_2.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/8_7_10.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/10_3_3.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/12_12_21.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/20_20_20.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/30_25_25.txt
def main(nombre_archivo):
    demandas_filas, demandas_columnas, longitudes_barcos = leer_casos_de_prueba(nombre_archivo)
    demandas_filas_originales, demandas_columnas_originales = demandas_filas.copy(), demandas_columnas.copy()
    n = len(demandas_filas)
    m = len(demandas_columnas)
    tablero, demanda_restante = algoritmo_JJ(n, m, longitudes_barcos, demandas_filas, demandas_columnas)

    demanda_total = sum(demandas_filas_originales) + sum(demandas_columnas_originales)

    print("Demanda total: ", demanda_total, "Demanda restante: ", demanda_restante, "Demanda cumplida: ", demanda_total - demanda_restante)
    print_tablero(tablero, demandas_filas_originales, demandas_columnas_originales)
    posiciones_barcos = obtener_posiciones_barcos(tablero)
    print("\nPosiciones de los barcos:")
    for idx, barco in enumerate(posiciones_barcos, start=1):
        print(f"Barco {idx}: {barco}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('nombre_archivo', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.nombre_archivo)

