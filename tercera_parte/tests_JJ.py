import unittest
from auxiliares import leer_casos_de_prueba, print_tablero
from John_Jellicoe import algoritmo_JJ

class TestJohnJellicoe(unittest.TestCase):
    def assertDemandaCumplida(self, archivo):    
        demandas_filas, demandas_columnas, longitudes_barcos = leer_casos_de_prueba(archivo)
        demandas_filas_originales, demandas_columnas_originales = demandas_filas.copy(), demandas_columnas.copy()

        n = len(demandas_filas)
        m = len(demandas_columnas)
        
        # Obtener el tablero solución
        tablero, demanda_restante = algoritmo_JJ(n, m, longitudes_barcos, demandas_filas, demandas_columnas)
        
        # Validar que las demandas no sean excedidas
        self.validar_demandas(tablero, demandas_filas_originales, demandas_columnas_originales)
        self.validar_sin_barcos_adyacentes(tablero)

        demanda_total = sum(demandas_filas_originales) + sum(demandas_columnas_originales)

        print("-------------------------------------------------------")
        print(archivo)
        print("Demanda total: ", demanda_total, "Demanda restante: ", demanda_restante, "Demanda cumplida: ", demanda_total - demanda_restante)
        print_tablero(tablero, demandas_filas_originales, demandas_columnas_originales)

    def validar_demandas(self, tablero, demandas_filas, demandas_columnas):
        n, m = tablero.shape
        
        for i in range(n):
            suma_fila = sum(tablero[i])
            if suma_fila > demandas_filas[i]:
                self.fail(f"La fila {i} excede la demanda: obtenido {suma_fila}, máximo permitido {demandas_filas[i]}")
        
        for j in range(m):
            suma_columna = sum(tablero[:, j])
            if suma_columna > demandas_columnas[j]:
                self.fail(f"La columna {j} excede la demanda: obtenido {suma_columna}, máximo permitido {demandas_columnas[j]}")

    def validar_sin_barcos_adyacentes(self, tablero):
        n, m = tablero.shape
        for i in range(n):
            for j in range(m):
                if tablero[i, j] == 1:
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m:                        
                                if tablero[ni, nj] == 1:
                                    if di == 0 or dj == 0: 
                                        continue 
                                    else:  
                                        self.fail(f"Se encontraron barcos adyacentes en las posiciones ({i},{j}) y ({ni},{nj})")

    def test_JJ_3_3_2(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/3_3_2.txt")

    def test_JJ_5_5_6(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/5_5_6.txt")

    def test_JJ_8_7_10(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/8_7_10.txt")

    def test_JJ_10_3_3(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/10_3_3.txt")

    def test_JJ_10_10_10(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/10_10_10.txt")

    def test_JJ_12_12_21(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/12_12_21.txt")

    def test_JJ_15_10_15(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/15_10_15.txt")

    def test_JJ_20_20_20(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/20_20_20.txt")

    def test_JJ_20_25_30(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/20_25_30.txt")

    def test_JJ_30_25_25(self):
        self.assertDemandaCumplida("tercera_parte/casos_test/30_25_25.txt")

if __name__ == '__main__':
    unittest.main()