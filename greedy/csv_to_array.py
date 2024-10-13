LINEA_TESTS = 1

def csv_test_to_array(nombre_test):
    with open(f'greedy/casos_test/{nombre_test}') as f:
        linea = f.readlines()[LINEA_TESTS]

        output = [int(s)  for s in linea[:-1].split(';')]
    return output


