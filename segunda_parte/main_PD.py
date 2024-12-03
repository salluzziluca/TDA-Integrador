from codigo_PD import programacion_dinamica_sofia
from csv_casos_PD import csv_tests_PD

# python segunda_parte/main_PD.py segunda_parte/TP2/20.txt
# python segunda_parte/main_PD.py segunda_parte/TP2/25.txt
# python segunda_parte/main_PD.py segunda_parte/TP2/50.txt
# python segunda_parte/main_PD.py segunda_parte/TP2/100.txt
# python segunda_parte/main_PD.py segunda_parte/TP2/1000.txt
# python segunda_parte/main_PD.py segunda_parte/TP2/10000.txt
# python segunda_parte/main_PD.py segunda_parte/TP2/20000.txt
def main(archivo):
    # Cargar las monedas desde un archivo o lista de prueba
    monedas = csv_tests_PD(archivo)  
    max_puntaje = programacion_dinamica_sofia(monedas)
    print("Máximo puntaje que puede obtener Sophia:", max_puntaje)
    # print("Camino de elecciones:")
    # for paso in resultado:
    #     print(paso)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('nombre_archivo', help='Nombre del archivo de entrada')
    args = parser.parse_args()

    main(args.nombre_archivo)