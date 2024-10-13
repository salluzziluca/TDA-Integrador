from csv_to_array import csv_test_to_array 


def elije_sophia(monedas):
    if not monedas:
        return

    moneda_elegida = -1 
    cant_monedas = len(monedas)
    if monedas[0]>monedas[cant_monedas-1]:
        moneda_elegida = monedas[0]
        monedas.pop(0)
    else:
        moneda_elegida = monedas[cant_monedas-1]
        monedas.pop(cant_monedas-1)
    return moneda_elegida

def elije_mateo(monedas):
    if not monedas:
        return
        
    moneda_elegida = -1 
    cant_monedas = len(monedas)
    if monedas[0]<monedas[cant_monedas-1]:
        moneda_elegida = monedas[0]
        monedas.pop(0)
    else:
        moneda_elegida = monedas[cant_monedas-1]
        monedas.pop(cant_monedas-1)
    return moneda_elegida

def greedy(monedas):
    
    puntos_sophia = 0
    puntos_mateo = 0
    while len(monedas)>0:
        puntos_sophia += elije_sophia(monedas)
        puntos_mateo += elije_mateo(monedas)
    print(puntos_sophia, puntos_mateo)
    return puntos_sophia, puntos_mateo


        
print(greedy(csv_test_to_array("20.txt")))


