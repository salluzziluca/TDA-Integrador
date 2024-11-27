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