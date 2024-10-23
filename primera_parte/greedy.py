from collections import deque 

SOPHIA = 0
MATEO = 1

MONEDA_IZQ = 0
MONEDA_DER = -1

def elegir_moneda(monedas, jugador):
    if not monedas:
        return 0

    # Determina la moneda a elegir: mayor para Sophia, menor para Mateo
    if (jugador == SOPHIA and monedas[MONEDA_IZQ] > monedas[MONEDA_DER]) or (jugador == MATEO and monedas[MONEDA_IZQ] < monedas[MONEDA_DER]):
        return monedas.popleft() # Moneda izq
    else:
        return monedas.pop() # Moneda der

def greedy_monedas(monedas):
    deque_monedes = deque(monedas) # dequeado paraque el pop(0) sea O(1)
    puntos_sophia = 0
    puntos_mateo = 0
    while deque_monedes:
        puntos_sophia += elegir_moneda(deque_monedes, SOPHIA)
        puntos_mateo += elegir_moneda(deque_monedes, MATEO)

    return puntos_sophia, puntos_mateo

