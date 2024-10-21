from collections import deque 

LINEA_TESTS = 1

def csv_casos_a_lista(nombre_test):
    with open(f'greedy/casos_test/{nombre_test}') as f:
        linea = f.readlines()[LINEA_TESTS] # Picardías argentinas

        output = deque([int(s)  for s in linea[:-1].split(';')]) # dequeado paraque el pop(0) sea O(1)
        #la conversion de lisa a deque es O(n)
    return output 