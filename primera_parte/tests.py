import unittest
from csv_casos import csv_casos_a_lista 
from greedy import greedy_monedas

RESULTADO_SOPHIA = 0
RESULTADO_MATEO = 1

class TestGreedy(unittest.TestCase):
    def test_greedy_20(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/20.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])
    
    def test_greedy_25(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/25.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])

    def test_greedy_50(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/50.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])

    def test_greedy_100(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/100.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])

    def test_greedy_1000(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/1000.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])
    
    def test_greedy_10000(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/10000.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])

    def test_greedy_20000(self):
        result = greedy_monedas(csv_casos_a_lista("primera_parte/casos_test/20000.txt"))
        self.assertTrue(result[RESULTADO_SOPHIA]>result[RESULTADO_MATEO])



if __name__ == '__main__':
    unittest.main()