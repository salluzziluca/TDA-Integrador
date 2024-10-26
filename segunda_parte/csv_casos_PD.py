LINEA_TESTS = 1

def csv_tests_PD(nombre_test):
    with open(f'segunda_parte/TP2/{nombre_test}') as f:
        linea = f.readlines()[LINEA_TESTS] # Picardías argentinas

        output = [int(s)  for s in linea[:-1].split(';')] 
    return output 