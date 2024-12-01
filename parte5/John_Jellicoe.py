import numpy as np

def can_place_ship(board,n,m, x, y, length, is_horizontal):
    if is_horizontal:
        if y + length > m:  
            return False
        for i in range(length):
            if board[x, y + i] == 1 or \
                (x > 0 and board[x - 1, y + i] == 1) or \
                (x < n - 1 and board[x + 1, y + i] == 1) or \
                (x > 0 and y + i > 0 and board[x - 1, y + i - 1] == 1) or \
                (x > 0 and y + i < m - 1 and board[x - 1, y + i + 1] == 1) or \
                (x < n - 1 and y + i > 0 and board[x + 1, y + i - 1] == 1) or \
                (x < n - 1 and y + i < m - 1 and board[x + 1, y + i + 1] == 1):
                return False
        if y > 0 and board[x, y - 1] == 1:
            return False
        if y + length < m and board[x, y + length] == 1:
            return False
    else:  
        if x + length > n:  
            return False
        for i in range(length):
            
            if board[x + i, y] == 1 or \
                (y > 0 and board[x + i, y - 1] == 1) or \
                (y < m - 1 and board[x + i, y + 1] == 1) or \
                (x + i > 0 and y > 0 and board[x + i - 1, y - 1] == 1) or \
                (x + i > 0 and y < m - 1 and board[x + i - 1, y + 1] == 1) or \
                (x + i < n - 1 and y > 0 and board[x + i + 1, y - 1] == 1) or \
                (x + i < n - 1 and y < m - 1 and board[x + i + 1, y + 1] == 1):
                return False
        if x > 0 and board[x - 1, y] == 1:
            return False
        if x + length < n and board[x + length, y] == 1:
            return False
    return True

def place_ship(board, x, y, length, is_horizontal):
    if is_horizontal:
        for i in range(length):
            board[x, y + i] = 1
    else:
        for i in range(length):
            board[x + i, y] = 1


def algoritmo_JJ(n, m, ship_lengths, row_restrictions, col_restrictions):
    board = np.zeros((n, m), dtype=int)

    ships = sorted(ship_lengths, reverse=True) # O(k log k)

    while ships:
        row_demand = [(i, row_restrictions[i]) for i in range(n) if row_restrictions[i] > 0] # O(n+m)
        col_demand = [(j, col_restrictions[j]) for j in range(m) if col_restrictions[j] > 0] # O(n+m)

        if not row_demand and not col_demand:
            break  

        ship_placed = False  # para verificar si el barco se colocó en esta iteración

        for ship in ships:
            # Intentar colocar el barco en una fila
            if row_demand and (not col_demand or max(row_demand, key=lambda x: x[1])[1] >= max(col_demand, key=lambda x: x[1])[1]):
                target_row = max(row_demand, key=lambda x: x[1])[0]
                if row_restrictions[target_row] >= ship:  # Verificar si la fila puede acomodar el barco
                    for start_col in range(m):
                        # Asegurar que todas las columnas involucradas tienen suficiente demanda
                        if all(0 <= start_col + i < m and col_restrictions[start_col + i] > 0 for i in range(ship)) and can_place_ship(board,n,m, target_row, start_col, ship, True):
                            place_ship(board, target_row, start_col, ship, True)
                            row_restrictions[target_row] -= ship
                            for i in range(ship):
                                col_restrictions[start_col + i] -= 1
                            ships.remove(ship)
                            ship_placed = True
                            break
                if ship_placed:
                    break


            # Intentar colocar el barco en una columna
            if col_demand and not ship_placed:
                target_col = max(col_demand, key=lambda x: x[1])[0]
                if col_restrictions[target_col] >= ship:  # Verificar si la columna puede acomodar el barco
                    for start_row in range(n):
                        # Asegurar que todas las filas involucradas tienen suficiente demanda
                        if all(0 <= start_row + i < n and row_restrictions[start_row + i] > 0 for i in range(ship)) and can_place_ship(board,n,m, start_row, target_col, ship, False):
                            place_ship(board, start_row, target_col, ship, False)
                            col_restrictions[target_col] -= ship
                            for i in range(ship):
                                row_restrictions[start_row + i] -= 1
                            ships.remove(ship)
                            ship_placed = True
                            break
                if ship_placed:
                    break


        # Si no se pudo colocar ningún barco en esta iteración, salimos del bucle
        if not ship_placed:
            break

    demanda_restante = sum(row_restrictions) + sum(col_restrictions)
    return board, demanda_restante
