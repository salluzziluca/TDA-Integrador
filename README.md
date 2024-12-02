## Parte 2:
Para demostrar que el problema de la batalla naval es np-completo se debe poder reducir bin packing (que es np-completo)
al problema de la batalla naval.

Bin packing - problema de decisión: dado un arreglo de números y B bins, cada uno de capacidad C, se debe poder decidir
si los números pueden dividirse en B bins de tal forma que la sumatoria de los números en cada bin sea igual a C.

Idea: Se puede formar 1 tablero de (2*B*C)xB (2*B*C filas, B columnas), la demanda de cada fila será de 1, y la demanda
de cada columna será de C. La demanda total sería de 3*B*C. Con esto se puede llamar al problema de la batalla naval y
verificar que la demanda total cumplida sea de 2*B*C con el arreglo de números.

La idea es que, con los números vistos como barcos, cada barco se pueda colocar de forma vertical y cumpla con la
demanda C de cada columna.
