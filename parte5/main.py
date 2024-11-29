from John_Jellicoe import naval_battle_solver
from lector_casos import leer_casos_de_prueba

# python parte5/main.py parte5/TP3/3_3_2.txt
# python parte5/main.py parte5/TP3/8_7_10.txt
# python parte5/main.py parte5/TP3/10_3_3.txt
# python parte5/main.py parte5/TP3/12_12_21.txt
# python parte5/main.py parte5/TP3/20_20_20.txt
# python parte5/main.py parte5/TP3/30_25_25.txt
def main(filename):
    row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
    n = len(row_demands)
    m = len(column_demands)
    print(naval_battle_solver(n, m, boat_lengths, row_demands, column_demands))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.filename)

