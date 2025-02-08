import time
import unittest
from auxiliares import leer_casos_de_prueba, print_tablero
from backtracking import resolver_tablero
from csv_casos import procesar_archivo
from John_Jellicoe import algoritmo_JJ


class TestBtAndJohn(unittest.TestCase):
    def comparar_cotas(self, filename):
        barcos, filas, columnas = procesar_archivo(filename)
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
        original_row_demands, original_column_demands = row_demands.copy(), column_demands.copy()

        n = len(row_demands)
        m = len(column_demands)
        
        # Get the solution board
        board, demanda_restante = algoritmo_JJ(n, m, boat_lengths, row_demands, column_demands)

        demanda_cumplida = sum(original_row_demands) + sum(original_column_demands) - demanda_restante

        cota = demanda_cumplida /  result["demanda_cumplida"]
        print(f"Demanda cumplida JJ: {demanda_cumplida} | Demanda cumplida BT: {result["demanda_cumplida"]} | Cota: {cota}")

    def test_comp_3_3_2(self):
        self.comparar_cotas("tercera_parte/casos_test/3_3_2.txt")

    def test_comp_5_5_6(self):
        self.comparar_cotas("tercera_parte/casos_test/5_5_6.txt")

    def test_comp_8_7_10(self):
        self.comparar_cotas("tercera_parte/casos_test/8_7_10.txt")

    def test_comp_10_3_3(self):
        self.comparar_cotas("tercera_parte/casos_test/10_3_3.txt")

    def test_comp_10_10_10(self):
        self.comparar_cotas("tercera_parte/casos_test/10_10_10.txt")

    def test_comp_12_12_21(self):
        self.comparar_cotas("tercera_parte/casos_test/12_12_21.txt")

    def test_comp_15_10_15(self):
        self.comparar_cotas("tercera_parte/casos_test/15_10_15.txt")

    def test_comp_20_20_20(self):
        self.comparar_cotas("tercera_parte/casos_test/20_20_20.txt")

    def test_comp_20_25_30(self):
        self.comparar_cotas("tercera_parte/casos_test/20_25_30.txt")

    def test_comp_30_25_25(self):
        self.comparar_cotas("tercera_parte/casos_test/30_25_25.txt")


if __name__ == '__main__':
    unittest.main()