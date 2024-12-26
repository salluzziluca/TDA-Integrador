SOPHIA = 0
MATEO = 1

def elegir_moneda(monedas, jugador, izq, der):
    # Si es Sophia y la moneda izquierda es mayor, o si es Mateo y la moneda izquierda es menor
    if (jugador == SOPHIA and monedas[izq] > monedas[der]) or (jugador == MATEO and monedas[izq] < monedas[der]):
        return {
            'valor': monedas[izq],
            'posicion': izq,
            'es_izquierda': True,
            'nuevo_izq': izq + 1,
            'nuevo_der': der
        }
    else:
        return {
            'valor': monedas[der],
            'posicion': der,
            'es_izquierda': False,
            'nuevo_izq': izq,
            'nuevo_der': der - 1
        }

def greedy_monedas(monedas):
    izq, der = 0, len(monedas) - 1
    puntos_sophia = puntos_mateo = 0
    estado_juego = []
    monedas_restantes = [monedas[:]]  # Guardamos el estado inicial
    
    turno = 0
    while izq <= der:
        jugador = SOPHIA if turno % 2 == 0 else MATEO
        decision = elegir_moneda(monedas, jugador, izq, der)
        
        # Registrar la decisión y el estado del juego
        estado = {
            'turno': turno + 1,
            'jugador': 'Sofia' if jugador == SOPHIA else 'Mateo',
            'moneda': decision['valor'],
            'posicion': 'primera' if decision['es_izquierda'] else 'ultima',
            'monedas_antes': monedas[izq:der + 1],
            'monedas_despues': monedas[decision['nuevo_izq']:decision['nuevo_der'] + 1],
            'puntos_sophia': puntos_sophia + (decision['valor'] if jugador == SOPHIA else 0),
            'puntos_mateo': puntos_mateo + (decision['valor'] if jugador == MATEO else 0)
        }
        estado_juego.append(estado)
        
        # Actualizar puntos
        if jugador == SOPHIA:
            puntos_sophia += decision['valor']
        else:
            puntos_mateo += decision['valor']
        
        # Actualizar índices
        izq = decision['nuevo_izq']
        der = decision['nuevo_der']
        turno += 1

    return puntos_sophia, puntos_mateo, estado_juego

def imprimir_estado_juego(estado_juego):
    print("\nReconstrucción detallada del juego:")
    print("=" * 60)
    
    for estado in estado_juego:
        print(f"\nTurno {estado['turno']}:")
        print(f"Monedas disponibles: {estado['monedas_antes']}")
        print(f"{estado['jugador']} agarra la {estado['posicion']} moneda: {estado['moneda']}")
        if len(estado['monedas_despues']) > 0:
            print(f"Monedas restantes: {estado['monedas_despues']}")
        print(f"Puntuación - Sofia: {estado['puntos_sophia']}, Mateo: {estado['puntos_mateo']}")

