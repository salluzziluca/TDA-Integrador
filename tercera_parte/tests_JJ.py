import unittest
from auxiliares import leer_casos_de_prueba, print_tablero
from John_Jellicoe import algoritmo_JJ

class TestJohnJellicoe(unittest.TestCase):
    def assertDemandaCumplida(self, filename):    
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
        original_row_demands, original_column_demands = row_demands.copy(), column_demands.copy()

        n = len(row_demands)
        m = len(column_demands)
        
        # Get the solution board
        board, demanda_restante = algoritmo_JJ(n, m, boat_lengths, row_demands, column_demands)
        
        # Validate demands aren't exceeded
        self.validate_demands(board, original_row_demands, original_column_demands)
        self.validate_no_adjacent_ships(board)

        demanda_total = sum(original_row_demands) + sum(original_column_demands)

        print("-------------------------------------------------------")
        print(filename)
        print("Demanda total: ",demanda_total,"Demanda restante: ",demanda_restante,"Demanda cumplida: ",demanda_total-demanda_restante)
        print_tablero(board, original_row_demands, original_column_demands)

    def validate_demands(self, board, row_demands, column_demands):
        """Validate that no row or column demand is exceeded"""
        n, m = board.shape
        
        # Check row demands
        for i in range(n):
            row_sum = sum(board[i])
            if row_sum > row_demands[i]:
                self.fail(f"Row {i} exceeds demand: got {row_sum}, max allowed {row_demands[i]}")
        
        # Check column demands
        for j in range(m):
            col_sum = sum(board[:, j])
            if col_sum > column_demands[j]:
                self.fail(f"Column {j} exceeds demand: got {col_sum}, max allowed {column_demands[j]}")

    def validate_no_adjacent_ships(self, board):
        """Validate that no ships are adjacent (including diagonally)"""
        n, m = board.shape
        for i in range(n):
            for j in range(m):
                if board[i, j] == 1:
                    # Check surrounding cells
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m:
                                # Allow adjacent cells only if they're part of the same ship
                                if board[ni, nj] == 1:
                                    # Verify it's part of the same ship
                                    if di == 0 or dj == 0:  # orthogonal
                                        continue  # same ship possible
                                    else:  # diagonal
                                        self.fail(f"Found adjacent ships at positions ({i},{j}) and ({ni},{nj})")

    def test_JJ_3_3_2(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/3_3_2.txt")

    def test_JJ_5_5_6(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/5_5_6.txt")

    def test_JJ_8_7_10(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/8_7_10.txt")

    def test_JJ_10_3_3(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/10_3_3.txt")

    def test_JJ_10_10_10(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/10_10_10.txt")

    def test_JJ_12_12_21(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/12_12_21.txt")

    def test_JJ_15_10_15(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/15_10_15.txt")

    def test_JJ_20_20_20(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/20_20_20.txt")

    def test_JJ_20_25_30(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/20_25_30.txt")

    def test_JJ_30_25_25(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/30_25_25.txt")

if __name__ == '__main__':
    unittest.main()