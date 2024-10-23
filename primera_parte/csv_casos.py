LINEA_TESTS = 1

def csv_casos_a_lista(nombre_test):
    with open(f'primera_parte/casos_test/{nombre_test}') as f:
        linea = f.readlines()[LINEA_TESTS] # Picardías argentinas

        output = [int(s)  for s in linea[:-1].split(';')] 
    return output 