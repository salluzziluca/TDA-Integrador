from John_Jellicoe import algoritmo_JJ
from auxiliares import leer_casos_de_prueba, print_tablero

# python tercera_parte/main_JJ.py tercera_parte/casos_test/3_3_2.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/8_7_10.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/10_3_3.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/12_12_21.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/20_20_20.txt
# python tercera_parte/main_JJ.py tercera_parte/casos_test/30_25_25.txt
def main(filename):
    row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
    original_row_demands, original_column_demands = row_demands.copy(), column_demands.copy()
    n = len(row_demands)
    m = len(column_demands)
    board, demanda_restante = algoritmo_JJ(n, m, boat_lengths, row_demands, column_demands)

    demanda_total = sum(original_row_demands) + sum(original_column_demands)

    print("Demanda total: ", demanda_total,"Demanda restante: ", demanda_restante, "Demanda cumplida: ",demanda_total-demanda_restante)
    print_tablero(board,original_row_demands, original_column_demands)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.filename)

