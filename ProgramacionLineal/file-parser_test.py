import unittest
from file_parser import leer_casos_de_prueba

class TestFileParser(unittest.TestCase):
    def test_3_3_2_file(self):
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba("ProgramacionLineal/TP3-20241123T201822Z-001/TP3/3_3_2.txt")
        
        # Test dimensions
        self.assertEqual(len(row_demands), 3)
        self.assertEqual(len(column_demands), 3)
        self.assertEqual(len(boat_lengths), 2)
        
        # Test specific values
        self.assertEqual(row_demands, [3, 1, 2])
        self.assertEqual(column_demands, [3, 2, 0])
        self.assertEqual(boat_lengths, [1, 1])
        
        # Test sums
        self.assertEqual(sum(boat_lengths), 2)
        self.assertEqual(sum(row_demands), 6)
        self.assertEqual(sum(column_demands), 5)

    def test_5_5_6_file(self):
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba("ProgramacionLineal/TP3-20241123T201822Z-001/TP3/5_5_6.txt")
        
        # Test dimensions
        self.assertEqual(len(row_demands), 5)
        self.assertEqual(len(column_demands), 5)
        self.assertEqual(len(boat_lengths), 6)
        
        # Test specific values
        self.assertEqual(row_demands, [3, 3, 0, 1, 1])
        self.assertEqual(column_demands, [3, 1, 0, 3, 3])
        self.assertEqual(boat_lengths, [1, 2, 2, 2, 2, 1])
        
        # Test sums
        self.assertEqual(sum(boat_lengths), 10)
        self.assertEqual(sum(row_demands), 8)
        self.assertEqual(sum(column_demands), 10)

    def test_8_7_10_file(self):
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba("ProgramacionLineal/TP3-20241123T201822Z-001/TP3/8_7_10.txt")
        
        # Test dimensions
        self.assertEqual(len(row_demands), 8)
        self.assertEqual(len(column_demands), 7)
        self.assertEqual(len(boat_lengths), 10)
        
        # Test specific values
        self.assertEqual(row_demands, [1, 4, 4, 4, 3, 3, 4, 4])
        self.assertEqual(column_demands, [6, 5, 3, 0, 6, 3, 3])
        self.assertEqual(boat_lengths, [2, 1, 2, 2, 1, 3, 2, 7, 7, 7])

    def test_10_3_3_file(self):
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba("ProgramacionLineal/TP3-20241123T201822Z-001/TP3/10_3_3.txt")
        
        # Test dimensions
        self.assertEqual(len(row_demands), 10)
        self.assertEqual(len(column_demands), 3)
        self.assertEqual(len(boat_lengths), 3)
        
        # Test specific values
        self.assertEqual(row_demands, [1, 0, 1, 0, 1, 0, 0, 1, 1, 1])
        self.assertEqual(column_demands, [1, 4, 3])
        self.assertEqual(boat_lengths, [3, 3, 4])

    def test_10_10_10_file(self):
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba("ProgramacionLineal/TP3-20241123T201822Z-001/TP3/10_10_10.txt")
        
        # Test dimensions
        self.assertEqual(len(row_demands), 10)
        self.assertEqual(len(column_demands), 10)
        self.assertEqual(len(boat_lengths), 10)
        
        # Test specific values
        self.assertEqual(row_demands, [3, 2, 2, 4, 2, 1, 1, 2, 3, 0])
        self.assertEqual(column_demands, [1, 2, 1, 3, 2, 2, 3, 1, 5, 0])
        self.assertEqual(boat_lengths, [4, 3, 3, 2, 2, 2, 1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()