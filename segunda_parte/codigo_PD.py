def programacion_dinamica_sofia(monedas):
    
    n = len(monedas)
    OPT = [[0] * n for _ in range (n)]
    
    for i in range(n):
        OPT[i][i] = monedas[i]
        
        
    for k in range(2, n + 1):
        for izq in range(n - k + 1):
            der = izq + k - 1 
            tomar_izq = monedas[izq] + min(OPT[izq + 2][der] if izq + 2 <= der else 0, OPT[izq + 1][der - 1] if izq + 1 <= der - 1 else 0)
            tomar_der = monedas[der] + min(OPT[ izq + 1][der - 1] if izq + 1 <= der - 1 else 0, OPT[izq][der-2] if izq <= der -2 else 0)
            OPT[izq][der] = max(tomar_izq, tomar_der)
            
    return OPT[0][n-1]


def reconstruir_camino(dp, monedas):
    n = len(monedas)
    camino = []  # Almacenará las monedas que Sophia debe elegir
    left, right = 0, n - 1  # Índices que delimitan el intervalo de monedas que se están considerando
    

    # Mientras haya monedas por elegir
    while left <= right:
        # Si solo queda una moneda, Sophia la toma
        if left == right:
            camino.append(('izquierda', monedas[left]))
            break

        # Verificamos cuál fue la mejor decisión en dp[left][right]
        # Si Sophia elige la moneda de la izquierda
        if monedas[left] + min(dp[left + 2][right], dp[left + 1][right - 1]) == dp[left][right]:
            camino.append(('izquierda', monedas[left]))
            left += 1  # Reducimos el intervalo por la izquierda
        else:  # Si Sophia elige la moneda de la derecha
            camino.append(('derecha', monedas[right]))
            right -= 1  # Reducimos el intervalo por la derecha

    return camino


