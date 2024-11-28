import unittest
from John_Jellicoe import resolvedor_john_jellicoe, leer_casos_de_prueba


class TestJohnJellicoe(unittest.TestCase):
    def assertDemandaCumplida(self, filename, expected_demanda_cumplida):
        row_demands, column_demands, _ = leer_casos_de_prueba(filename)
        resolvedor_john_jellicoe(filename) 
        demanda_cumplida = sum(row_demands) + sum(column_demands)
        self.assertEqual(demanda_cumplida, expected_demanda_cumplida)

    def test_BT_3_3_2(self):
        self.assertDemandaCumplida("parte5\TP3\3_3_2.txt", 4)

    def test_BT_5_5_6(self):
        self.assertDemandaCumplida("parte5\TP3\5_5_6.txt", 12)

    def test_BT_8_7_10(self):
        self.assertDemandaCumplida("parte5\TP3\8_7_10.txt", 26)

    def test_BT_10_3_3(self):
        self.assertDemandaCumplida("parte5\TP3\10_3_3.txt", 6)

    def test_BT_10_10_10(self):
        self.assertDemandaCumplida("parte5\TP3\10_10_10.txt", 40)

    def test_BT_12_12_21(self):
        self.assertDemandaCumplida("parte5\TP3\12_12_21.txt", 46)

    def test_BT_15_10_15(self):
        self.assertDemandaCumplida("parte5\TP3\15_10_15.txt", 40)

    def test_BT_20_20_20(self):
        self.assertDemandaCumplida("parte5\TP3\20_20_20.txt", 104)

    def test_BT_20_25_30(self):
        self.assertDemandaCumplida("parte5\TP3\20_25_30.txt", 172)

    def test_BT_30_25_25(self):
        self.assertDemandaCumplida("parte5\TP3\30_25_25.txt", 202)


if __name__ == '__main__':
    unittest.main()
