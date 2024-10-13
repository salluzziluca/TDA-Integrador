SOPHIA = 0
MATEO = 1

MONEDA_IZQ = 0
MONEDA_DER = -1

def elegir_moneda(monedas, jugador):
    if not monedas:
        return 0

    # Determina la moneda a elegir: mayor para Sophia, menor para Mateo
    if (jugador == SOPHIA and monedas[MONEDA_IZQ] > monedas[MONEDA_DER]) or (jugador == MATEO and monedas[MONEDA_IZQ] < monedas[MONEDA_DER]):
        return monedas.pop(MONEDA_IZQ)
    else:
        return monedas.pop(MONEDA_DER)

def greedy(monedas):
    puntos_sophia = 0
    puntos_mateo = 0
    while monedas:
        puntos_sophia += elegir_moneda(monedas, SOPHIA)
        puntos_mateo += elegir_moneda(monedas, MATEO)

    return puntos_sophia, puntos_mateo

