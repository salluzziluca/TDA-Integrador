from lector_casos import leer_casos_de_prueba

def print_tablero(tablero):
    for fila in tablero:
        print(fila)
        
def resolvedor_john_jellicoe(filename):
    row_demands, column_demands, boat_lengths = leer_casos_de_prueba(filename)
    n = len(row_demands)
    m = len(column_demands)
    tablero = [[0] * m for _ in range(n)]
    max_row_demand = max(row_demands)
    max_column_demand = max(column_demands)
    max_boat_length = max(boat_lengths)
    if max_row_demand> max_column_demand:
        max_index = row_demands.index(max_row_demand)
        cargar_barco_en_fila(tablero, max_boat_length, max_index, column_demands)
        #poner barco en max row
    else:
            #poner barco en max column
        max_index = column_demands.index(max_column_demand)
        cargar_barco_en_columna(tablero, max_boat_length, max_index, row_demands)
    print_tablero(tablero)
        
def cargar_barco_en_columna(tablero, boat_length, column, row_demands):
    """Esta funcion recibe un tablero, un bote y una columna. Para todas las filas de esa columna se fija si puede agregar el barco (chequeando las demandas) y si puede lo agrega"""
    valid_rows=[]
    i=0
    while i<len(row_demands):
        demand = row_demands[i]
        if demand>0:
            valid_rows.append(row_demands.index(demand))
        i+=1
    # if len(valid_rows)>=boat_length:
    #     for row in valid_rows:
    #         tablero[row][column]=1
    #     return True
    # miro si hay valid rows contiguas = boat_length
    valid_rows_contiguas= []
    for i in range(len(valid_rows)):
        if valid_rows[i]==valid_rows[i-1]+1:
            valid_rows_contiguas.append(valid_rows[i])
        if len(valid_rows_contiguas)==boat_length:
            for row in valid_rows_contiguas:
                tablero[row][column]=1
            return True
    return False        

    
def cargar_barco_en_fila(tablero, boat_length, row, column_demands):
    """Esta funcion recibe un tablero, un bote y una fila. Para todas las columnas de esa fila se fija si puede agregar el barco (chequeando las demandas) y si puede lo agrega"""
    valid_columns=[]
    i=0
    while i<len(column_demands):
        demand = column_demands[i]
        if demand>0:
            valid_columns.append(column_demands.index(demand))
        i+=1
    # if len(valid_columns)>=boat_length:
    #     for column in valid_columns:
    #         tablero[row][column]=1
    #     return True
    # miro si hay valid columns contiguas = boat_length
    valid_columns_contiguas= []
    for i in range(len(valid_columns)):
        if valid_columns[i]==valid_columns[i-1]+1:
            valid_columns_contiguas.append(valid_columns[i])
        if len(valid_columns_contiguas)==boat_length:
            for column in valid_columns_contiguas:
                tablero[row][column]=1
            return True
    return False



resolvedor_john_jellicoe("parte5/TP3/20_20_20.txt")