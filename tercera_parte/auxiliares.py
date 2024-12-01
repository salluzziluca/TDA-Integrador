import random

import numpy as np

def leer_casos_de_prueba(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if not line.startswith('#')]

        data = [int(line) for line in lines if line]

        section_lengths = []
        current_length = 0
        
        with open(filename, 'r') as file:
            for line in file:
                if line.strip() == '':
                    if current_length > 0:
                        section_lengths.append(current_length)
                        current_length = 0
                elif not line.startswith('#'):
                    current_length += 1
        
        if current_length > 0:
            section_lengths.append(current_length)

        n_rows = section_lengths[0]
        n_cols = section_lengths[1]
        
        row_demands = data[:n_rows]
        column_demands = data[n_rows:n_rows + n_cols]
        boat_lengths = data[n_rows + n_cols:]
        
        return row_demands, column_demands, boat_lengths
    
def print_tablero(board, row_demands, column_demands):
    max_num = max(max(row_demands), max(column_demands), 1)  
    cell_width = len(str(max_num)) + 2  

    col_header = " " * (cell_width + 1)  
    col_header += "".join(f"{col:>{cell_width}}" for col in column_demands)
    separator = " " * (cell_width + 1) + "-" * (len(column_demands) * cell_width)

    print(col_header)
    print(separator)

    for demand, row in zip(row_demands, board):
        row_str = "".join(f"{cell:>{cell_width}}" for cell in row)
        print(f"{demand:>{cell_width - 1}} | {row_str}")


def generate_test_case(offset_n_m, size, num_boats):
    n = size
    offset = random.randint(-offset_n_m, offset_n_m) 
    m = n + offset
    
    
    max_length = min(n, m)  
    boat_lengths = []
    for _ in range(num_boats):
        length = random.randint(1, max_length)
        boat_lengths.append(length)
    
    boat_lengths.sort(reverse=True)
    
    board = np.zeros((n, m), dtype=int)
    
    placed_boats = []
    for length in boat_lengths:
        placed = False
        attempts = 0
        max_attempts = 50 
        
        while not placed and attempts < max_attempts:
            is_horizontal = random.choice([True, False])
            
            if is_horizontal:
                if length > m:
                    attempts += 1
                    continue
                row = random.randint(0, n-1)
                col = random.randint(0, m-length)
                coords = [(row, col+i) for i in range(length)]
            else:
                if length > n:
                    attempts += 1
                    continue
                row = random.randint(0, n-length)
                col = random.randint(0, m-1)
                coords = [(row+i, col) for i in range(length)]
            
            valid = True
            for r, c in coords:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and board[nr, nc] == 1:
                            valid = False
                            break
                    if not valid:
                        break
                if not valid:
                    break
            
            if valid:
                for r, c in coords:
                    board[r, c] = 1
                placed = True
                placed_boats.append(length)
            
            attempts += 1
        
    row_demands = [sum(row) for row in board]
    column_demands = [sum(column) for column in board.T]
    
    for i in range(n):
        extra = random.randint(0, m - row_demands[i])
        row_demands[i] += extra
    
    for j in range(m):
        extra = random.randint(0, n - column_demands[j])
        column_demands[j] += extra
    
    return n, m, placed_boats, row_demands, column_demands