import unittest
import numpy as np
from lector_casos import leer_casos_de_prueba
from John_Jellicoe import naval_battle_solver

class TestJohnJellicoe(unittest.TestCase):
    def assertDemandaCumplida(self, filename, expected_demanda_cumplida):
        # Get the input data
        row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
        n = len(row_demands)
        m = len(column_demands)
        
        # Get the solution board
        board = naval_battle_solver(n,m, boat_lengths,row_demands, column_demands)
        
        # Calculate actual fulfilled demands
        fulfilled_row_demands = [min(sum(board[i]), row_demands[i]) for i in range(n)]
        fulfilled_col_demands = [min(sum(board[:, j]), column_demands[j]) for j in range(m)]
        
        # Calculate total fulfilled demand
        total_fulfilled = sum(fulfilled_row_demands) + sum(fulfilled_col_demands)
        
        # Compare with expected
        self.assertEqual(total_fulfilled, expected_demanda_cumplida, 
            f"Expected fulfilled demand {expected_demanda_cumplida}, but got {total_fulfilled}")
        
        # Additional validations
        self.validate_ship_placements(board, boat_lengths)
        self.validate_no_adjacent_ships(board)

    def validate_ship_placements(self, board, boat_lengths):
        """Validate that all placed ships match the required lengths"""
        n, m = board.shape
        ships_found = []
        
        # Find horizontal ships
        for i in range(n):
            current_length = 0
            for j in range(m):
                if board[i, j] == 1:
                    current_length += 1
                elif current_length > 0:
                    ships_found.append(current_length)
                    current_length = 0
            if current_length > 0:
                ships_found.append(current_length)
        
        # Find vertical ships
        for j in range(m):
            current_length = 0
            for i in range(n):
                if board[i, j] == 1:
                    current_length += 1
                elif current_length > 0:
                    ships_found.append(current_length)
                    current_length = 0
            if current_length > 0:
                ships_found.append(current_length)
        
        # Remove duplicates (ships counted both horizontally and vertically)
        ships_found = sorted([s for s in ships_found if s > 1])
        boat_lengths = sorted([l for l in boat_lengths if l > 1])
        
        self.assertEqual(ships_found, boat_lengths, 
            f"Found ships of lengths {ships_found}, but expected {boat_lengths}")

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

    # Original test cases
    def test_JJ_3_3_2(self):
        self.assertDemandaCumplida("parte5/TP3/3_3_2.txt", 4)

    def test_JJ_5_5_6(self):
        self.assertDemandaCumplida("parte5/TP3/5_5_6.txt", 12)

    def test_JJ_8_7_10(self):
        self.assertDemandaCumplida("parte5/TP3/8_7_10.txt", 26)

    def test_JJ_10_3_3(self):
        self.assertDemandaCumplida("parte5/TP3/10_3_3.txt", 6)

    def test_JJ_10_10_10(self):
        self.assertDemandaCumplida("parte5/TP3/10_10_10.txt", 40)

    def test_JJ_12_12_21(self):
        self.assertDemandaCumplida("parte5/TP3/12_12_21.txt", 46)

    def test_JJ_15_10_15(self):
        self.assertDemandaCumplida("parte5/TP3/15_10_15.txt", 40)

    def test_JJ_20_20_20(self):
        self.assertDemandaCumplida("parte5/TP3/20_20_20.txt", 104)

    def test_JJ_20_25_30(self):
        self.assertDemandaCumplida("parte5/TP3/20_25_30.txt", 172)

    def test_JJ_30_25_25(self):
        self.assertDemandaCumplida("parte5/TP3/30_25_25.txt", 202)

if __name__ == '__main__':
    unittest.main()