import time
import unittest
from auxiliares import leer_casos_de_prueba, print_tablero
from backtracking import resolver_tablero
from csv_casos import procesar_archivo
from John_Jellicoe import algoritmo_JJ


class TestBtAndJohn(unittest.TestCase):
    def test_BT_3_3_2_COTA(self):
        n, m, barcos, filas, columnas = procesar_archivo("3_3_2.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba("tercera_parte/casos_test/3_3_2.txt")
        original_row_demands, original_column_demands = row_demands.copy(), column_demands.copy()

        n = len(row_demands)
        m = len(column_demands)
        
        # Get the solution board
        board, demanda_restante = algoritmo_JJ(n, m, boat_lengths, row_demands, column_demands)

        demanda_cumplida = sum(original_row_demands) + sum(original_column_demands) - demanda_restante
        cota = demanda_cumplida / result["demanda_cumplida"]
        print("Cota: ", cota)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBtAndJohn('test_BT_3_3_2_COTA'))
    runner = unittest.TextTestRunner()
    runner.run(suite)