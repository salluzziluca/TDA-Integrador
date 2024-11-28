import argparse
from lector_casos import leer_casos_de_prueba

def print_tablero(tablero):
    for fila in tablero:
        print(fila)
        
def resolvedor_john_jellicoe(filename):
    row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
    n = len(row_demands)
    m = len(column_demands)
    tablero = [[0] * m for _ in range(n)]
    
    boat_lengths.sort(reverse=True)  # Ordenar barcos de mayor a menor longitud
    
    for boat_length in boat_lengths:
        while True:
            max_row_demand = max(row_demands)
            max_column_demand = max(column_demands)
            
            if max_row_demand == 0 and max_column_demand == 0:
                break  # No quedan demandas
            
            if max_row_demand >= max_column_demand:
                max_index = row_demands.index(max_row_demand)
                if not cargar_barco_en_fila(tablero, boat_length, max_index, column_demands):
                    break
            else:
                max_index = column_demands.index(max_column_demand)
                if not cargar_barco_en_columna(tablero, boat_length, max_index, row_demands):
                    break
    
    print_tablero(tablero)


def es_posicion_valida(tablero, fila, columna, boat_length, horizontal):
    n, m = len(tablero), len(tablero[0])
    if horizontal:
        if columna + boat_length > m:
            return False
        for c in range(columna, columna + boat_length):
            if tablero[fila][c] == 1 or \
               (fila > 0 and tablero[fila - 1][c] == 1) or \
               (fila < n - 1 and tablero[fila + 1][c] == 1):
                return False
    else:
        if fila + boat_length > n:
            return False
        for r in range(fila, fila + boat_length):
            if tablero[r][columna] == 1 or \
               (columna > 0 and tablero[r][columna - 1] == 1) or \
               (columna < m - 1 and tablero[r][columna + 1] == 1):
                return False
    return True

def cargar_barco_en_fila(tablero, boat_length, row, column_demands):
    for start_col in range(len(column_demands) - boat_length + 1):
        if all(column_demands[start_col + i] > 0 for i in range(boat_length)) and \
           es_posicion_valida(tablero, row, start_col, boat_length, True):
            for i in range(boat_length):
                tablero[row][start_col + i] = 1
                column_demands[start_col + i] -= 1
            return True
    return False

def cargar_barco_en_columna(tablero, boat_length, column, row_demands):
    for start_row in range(len(row_demands) - boat_length + 1):
        if all(row_demands[start_row + i] > 0 for i in range(boat_length)) and \
           es_posicion_valida(tablero, start_row, column, boat_length, False):
            for i in range(boat_length):
                tablero[start_row + i][column] = 1
                row_demands[start_row + i] -= 1
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resolver el problema de John Jellicoe para un caso de prueba dado.")
    parser.add_argument("filename", type=str, help="Nombre del archivo con los casos de prueba.")
    args = parser.parse_args()

    # ejs
    # python John_Jellicoe.py TP3/3_3_2.txt
    # python John_Jellicoe.py TP3/8_7_10.txt
    # python John_Jellicoe.py TP3/10_3_3.txt
    # python John_Jellicoe.py TP3/12_12_21.txt
    # python John_Jellicoe.py TP3/20_20_20.txt
    # python John_Jellicoe.py TP3/30_25_25.txt
    resolvedor_john_jellicoe(args.filename)