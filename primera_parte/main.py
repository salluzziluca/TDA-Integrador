from greedy import greedy_monedas
from csv_casos import csv_casos_a_lista

# python primera_parte/main.py primera_parte/casos_test/20.txt
# python primera_parte/main.py primera_parte/casos_test/25.txt
# python primera_parte/main.py primera_parte/casos_test/50.txt
# python primera_parte/main.py primera_parte/casos_test/100.txt
# python primera_parte/main.py primera_parte/casos_test/1000.txt
# python primera_parte/main.py primera_parte/casos_test/10000.txt
# python primera_parte/main.py primera_parte/casos_test/20000.txt
def main(filename):
    print(greedy_monedas(csv_casos_a_lista(filename)))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.filename)