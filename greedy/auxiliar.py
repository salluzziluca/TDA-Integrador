

def get_random_cant_monedas():
    # devuelve un array aleatorio de numeros mayores a 0 
    return deque([random.randint(1, 10000) for _ in range(1000)])

print(get_random_cant_monedas())
