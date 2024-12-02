import unittest
from csv_casos_PD import csv_tests_PD
from codigo_PD import programacion_dinamica_sofia


class TestPD(unittest.TestCase):
    def test_PD_5(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/5.txt"))
        self.assertTrue(result == 1483)
    
    def test_PD_10(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/10.txt"))
        self.assertTrue(result == 2338)

    def test_PD_20(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/20.txt"))
        self.assertTrue(result == 5234)

    def test_PD_25(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/25.txt"))
        self.assertTrue(result == 7491)

    def test_PD_50(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/50.txt"))
        self.assertTrue(result == 14976)
    
    def test_PD_100(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/100.txt"))
        self.assertTrue(result == 28844)

    def test_PD_1000(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/1000.txt"))
        self.assertTrue(result == 1401590)
        
    def test_PD_2000(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/2000.txt"))
        self.assertTrue(result == 2869340)

    def test_PD_5000(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/5000.txt"))
        self.assertTrue(result == 9939221)
    def test_PD_10000(self):
        result = programacion_dinamica_sofia(csv_tests_PD("segunda_parte/TP2/10000.txt"))
        self.assertTrue(result == 34107537)



if __name__ == '__main__':
    unittest.main()