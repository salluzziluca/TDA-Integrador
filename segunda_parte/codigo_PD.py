def programacion_dinamica_sofia(monedas):
    n = len(monedas)
    OPT = [[0] * n for _ in range(n)]
    decisiones = [[None] * n for _ in range(n)]  # Registro de decisiones: 'izq' o 'der'

    # Inicialización de la tabla para cuando hay una sola moneda
    for i in range(n):
        OPT[i][i] = monedas[i]
        decisiones[i][i] = 'izq'  # Tomar la única moneda disponible

    # Llenado de la tabla de programación dinámica
    for k in range(2, n + 1):  # k es el tamaño del intervalo
        for izq in range(n - k + 1):
            der = izq + k - 1

            # Opción 1: Sophia toma la moneda de la izquierda
            if izq + 1 <= der:
                if monedas[izq + 1] >= monedas[der]:
                    tomar_izq = monedas[izq] + OPT[izq + 2][der] if izq + 2 <= der else monedas[izq]
                else:
                    tomar_izq = monedas[izq] + OPT[izq + 1][der - 1] if izq + 1 <= der - 1 else monedas[izq]
            else:
                tomar_izq = monedas[izq]

            # Opción 2: Sophia toma la moneda de la derecha
            if izq <= der - 1:
                if monedas[izq] >= monedas[der - 1]:
                    tomar_der = monedas[der] + OPT[izq + 1][der - 1] if izq + 1 <= der - 1 else monedas[der]
                else:
                    tomar_der = monedas[der] + OPT[izq][der - 2] if izq <= der - 2 else monedas[der]
            else:
                tomar_der = monedas[der]

            # Elegir la mejor opción y registrar la decisión
            if tomar_izq > tomar_der:
                OPT[izq][der] = tomar_izq
                decisiones[izq][der] = 'izq'
            else:
                OPT[izq][der] = tomar_der
                decisiones[izq][der] = 'der'

    return OPT[0][n - 1], decisiones

def reconstruir_camino(decisiones, monedas):
    n = len(monedas)
    camino = []  # Almacenará las monedas que Sophia y Mateo eligen
    left, right = 0, n - 1  # Índices que delimitan el intervalo de monedas
    turnos = 0  # Contador de turnos

    # Mientras haya monedas por elegir
    while left <= right:
        if decisiones[left][right] == 'izq':
            if turnos % 2 == 0:
                camino.append(('Sofia agarra la primera: ', monedas[left]))
            else:
                camino.append(('Mateo agarra la primera', monedas[left]))
            left += 1  # Reducimos el intervalo por la izquierda
        else:
            if turnos % 2 == 0:
                camino.append(('Sofia agarra la ultima', monedas[right]))
            else:
                camino.append(('Mateo agarra la ultima', monedas[right]))
            right -= 1  # Reducimos el intervalo por la derecha

        turnos += 1  # Cambiamos de turno
    
    return camino
