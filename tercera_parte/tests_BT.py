import unittest
from csv_casos import procesar_archivo
from backtracking import resolver_problema


class TestBT(unittest.TestCase):
    def test_BT_3_3_2(self):
        n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("3_3_2.txt")
        print(n, m, barcos, demandas_filas, demandas_columnas)
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 4)
    
    def test_BT_5_5_6(self):
        n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("5_5_6.txt")
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 12)

    def test_BT_8_7_10(self):
        n, m, barcos, demandas_filas, demandas_columnas =  procesar_archivo("8_7_10.txt")
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 26)

    def test_BT_10_3_3(self):
        n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("10_3_3.txt")
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 6)

    def test_BT_10_10_10(self):
        n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("10_10_10.txt")
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 40)
    
    def test_BT_12_12_21(self):
        n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("12_12-21.txt")
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 46)

    def test_BT_15_10_15(self):
        n, m, barcos, demandas_filas, demandas_columnas = procesar_archivo("15_10_15.txt")
        result = resolver_problema(n, m, barcos, demandas_filas, demandas_columnas)
        self.assertTrue(result[3] == 40)
    """def test_BT_20_20_20(self):

        result = resolver_problema(procesar_archivo("20_20_20.txt"))
        self.assertTrue(result[3] == 104)
    def test_BT_20_25_30(self):
        result = resolver_problema(procesar_archivo("20_25_30.txt"))
        print(result)
        self.assertTrue(result[3] == 172)
    def test_BT_30_25_25(self):
        result = resolver_problema(procesar_archivo("30_25_25.txt"))
        self.assertTrue(result[3] == 202)
"""


if __name__ == '__main__':
    unittest.main()