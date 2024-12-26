from greedy import greedy_monedas
from greedy import imprimir_estado_juego
from csv_casos import csv_casos_a_lista

# python primera_parte/main_greedy.py primera_parte/casos_test/20.txt
# python primera_parte/main_greedy.py primera_parte/casos_test/25.txt
# python primera_parte/main_greedy.py primera_parte/casos_test/50.txt
# python primera_parte/main_greedy.py primera_parte/casos_test/100.txt
# python primera_parte/main_greedy.py primera_parte/casos_test/1000.txt
# python primera_parte/main_greedy.py primera_parte/casos_test/10000.txt
# python primera_parte/main_greedy.py primera_parte/casos_test/20000.txt
def main(filename):
    monedas = csv_casos_a_lista(filename)
    puntos_sophia, puntos_mateo, estado_juego = greedy_monedas(monedas)

    print(f'Puntos Sophia: {puntos_sophia}')
    print(f'Puntos Mateo: {puntos_mateo}')

    imprimir_estado_juego(estado_juego)
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.filename)