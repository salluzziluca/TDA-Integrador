def elegir_moneda(monedas, jugador):
    if not monedas:
        return 0

    # Determina la moneda a elegir: mayor para Sophia, menor para Mateo
    if (jugador == "Sophia" and monedas[0] > monedas[-1]) or (jugador == "Mateo" and monedas[0] < monedas[-1]):
        return monedas.pop(0)
    else:
        return monedas.pop(-1)

def greedy(monedas):
    puntos_sophia = 0
    puntos_mateo = 0
    while monedas:
        puntos_sophia += elegir_moneda(monedas, "Sophia")
        puntos_mateo += elegir_moneda(monedas, "Mateo")

    return puntos_sophia, puntos_mateo

