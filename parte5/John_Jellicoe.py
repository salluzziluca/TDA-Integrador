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
    
    boat_lengths.sort(reverse=True) 
    
    for boat_length in boat_lengths:
        while True:
            max_row_demand = max(row_demands)
            max_column_demand = max(column_demands)
            
            if max_row_demand == 0 and max_column_demand == 0:
                break  
            
            if max_row_demand >= max_column_demand:
                max_index = row_demands.index(max_row_demand)
                if not cargar_barco_en_fila(tablero, boat_length, max_index, column_demands):
                    break
                row_demands[max_index] -= boat_length
            else:
                max_index = column_demands.index(max_column_demand)
                if not cargar_barco_en_columna(tablero, boat_length, max_index, row_demands):
                    break
                column_demands[max_index] -= boat_length
    
    return tablero

def es_posicion_valida(tablero, fila, columna, boat_length, horizontal):
    n, m = len(tablero), len(tablero[0])
    
    if horizontal and columna + boat_length > m:
        return False
    if not horizontal and fila + boat_length > n:
        return False

    if horizontal:
        for c in range(max(0, columna - 1), min(m, columna + boat_length + 1)):
            for r in range(max(0, fila - 1), min(n, fila + 2)):
                if tablero[r][c] == 1:
                    return False
    else:
        for r in range(max(0, fila - 1), min(n, fila + boat_length + 1)):
            for c in range(max(0, columna - 1), min(m, columna + 2)):
                if tablero[r][c] == 1:
                    return False
    
    return True

def cargar_barco_en_fila(tablero, boat_length, row, column_demands):
    
    for start_col in range(len(column_demands) - boat_length + 1):

        if all(column_demands[start_col + i] > 0 for i in range(boat_length)) and es_posicion_valida(tablero, row, start_col, boat_length, True):

            for i in range(boat_length):
                tablero[row][start_col + i] = 1
                column_demands[start_col + i] -= 1

            return True
        
    return False

def cargar_barco_en_columna(tablero, boat_length, column, row_demands):
    for start_row in range(len(row_demands) - boat_length + 1):
        if all(row_demands[start_row + i] > 0 for i in range(boat_length)) and es_posicion_valida(tablero, start_row, column, boat_length, False):
            for i in range(boat_length):
                tablero[start_row + i][column] = 1
                row_demands[start_row + i] -= 1
            return True
    return False


print_tablero(resolvedor_john_jellicoe("parte5/TP3/3_3_2.txt"))
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resolver el problema de John Jellicoe para un caso de prueba dado.")
    parser.add_argument("filename", type=str, help="Nombre del archivo con los casos de prueba.")
    args = parser.parse_args()
    # ejs
    # python parte5/John_Jellicoe.py parte5/TP3/3_3_2.txt
    # python parte5/John_Jellicoe.py parte5/TP3/8_7_10.txt
    # python parte5/John_Jellicoe.py parte5/TP3/10_3_3.txt
    # python parte5/John_Jellicoe.py parte5/TP3/12_12_21.txt
    # python parte5/John_Jellicoe.py parte5/TP3/20_20_20.txt
    # python parte5/John_Jellicoe.py parte5/TP3/30_25_25.txt
    print_tablero(resolvedor_john_jellicoe(args.filename))