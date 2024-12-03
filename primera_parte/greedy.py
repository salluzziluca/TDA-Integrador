SOPHIA = 0
MATEO = 1

def elegir_moneda(monedas, jugador, izq, der):
    if (jugador == SOPHIA and monedas[izq] > monedas[der]) or (jugador == MATEO and monedas[izq] < monedas[der]):
        return monedas[izq], izq + 1, der  
    else:
        return monedas[der], izq, der - 1  

def greedy_monedas(monedas):
    izq, der = 0, len(monedas) - 1  
    puntos_sophia, puntos_mateo = 0, 0

    turno_sophia = True
    while izq <= der:
        jugador = SOPHIA if turno_sophia else MATEO
        moneda, izq, der = elegir_moneda(monedas, jugador, izq, der)
        if turno_sophia:
            puntos_sophia += moneda
        else:
            puntos_mateo += moneda
        turno_sophia = not turno_sophia  

    return puntos_sophia, puntos_mateo
