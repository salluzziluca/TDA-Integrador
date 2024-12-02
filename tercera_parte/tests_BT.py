import unittest
import time
from csv_casos import procesar_archivo
from backtracking import resolver_tablero


class TestBT(unittest.TestCase):
    def test_BT_3_3_2(self):
        
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/3_3_2.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))

        self.assertTrue(result["demanda_cumplida"] == 4)
    
    def test_BT_5_5_6(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/5_5_6.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 12)

    def test_BT_8_7_10(self):
        barcos, filas, columnas =  procesar_archivo("tercera_parte/casos_test/8_7_10.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 26)

    def test_BT_10_3_3(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/10_3_3.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 6)

    def test_BT_10_10_10(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/10_10_10.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 40)
    
    def test_BT_12_12_21(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/12_12_21.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 46)

    def test_BT_15_10_15(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/15_10_15.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 40)
        
    def test_BT_20_20_20(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/20_20_20.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 104)
        
    def test_BT_20_25_30(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/20_25_30.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 172)
        
    def test_BT_30_25_25(self):
        barcos, filas, columnas = procesar_archivo("tercera_parte/casos_test/30_25_25.txt")
        demanda_filas = sum(filas)
        demanda_columnas = sum(columnas)
        inicio = time.time()
        result = resolver_tablero(barcos, filas, columnas, demanda_filas, demanda_columnas)
        print("Tiempo de ejecución de la matriz {} x {} = {}: ".format(len(filas), len(columnas), time.time() - inicio))
        self.assertTrue(result["demanda_cumplida"] == 202)



if __name__ == '__main__':
    unittest.main()