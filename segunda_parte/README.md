# TDA-Integrador

# 1. Recurrencia del problema

La idea básica es que dos jugadores están tomando monedas de una secuencia de monedas. Cada jugador quiere maximizar la cantidad de monedas que puede tomar. Dado que cada jugador puede elegir la primera o la última moneda de la secuencia en su turno, el problema es inherentemente recursivo.

La ecuación de recurrencia se define de la siguiente manera:

- `OPT[izq][der]` representa el valor máximo que puede obtener el jugador que toma monedas entre las posiciones `izq` y `der`.
- El jugador tiene dos opciones:

### a. Tomar la moneda izquierda:
En este caso, el jugador toma `monedas[izq]` y el siguiente jugador puede tomar monedas entre las posiciones `izq + 1` y `der`. El valor acumulado será:
tomar_izq = monedas[izq] + min(OPT[izq + 2][der], OPT[izq + 1][der - 1])


Aquí, el jugador siguiente juega de forma óptima, lo que significa que tratará de minimizar lo que el jugador original puede obtener en su siguiente turno.

### b. Tomar la moneda derecha:
En este caso, el jugador toma `monedas[der]` y el siguiente jugador toma monedas entre las posiciones `izq` y `der - 1`. El valor acumulado será:
tomar_der = monedas[der] +\min(OPT[izq + 1][der - 1], OPT[izq][der - 2])

Finalmente, el jugador tomará la opción que le ofrezca el valor máximo:
OPT[izq][der] = max(toma_izq, tomar_der)

---

# 2. Demostración inductiva

Usaremos **inducción** para demostrar que la solución dada por la ecuación de recurrencia es correcta y maximiza el valor acumulado.

### Base inductiva:
Para un solo elemento, `OPT[i][i] = monedas[i]`. Esto es correcto, ya que si solo queda una moneda, el jugador necesariamente la tomará, y ese será su valor máximo.

### Paso inductivo:
Supongamos que la recurrencia es correcta para cualquier subsecuencia de longitud menor o igual a `k-1`. Ahora demostraremos que también es válida para una subsecuencia de longitud `k`.

El jugador tiene dos opciones, tomar la moneda izquierda o derecha. Si toma la izquierda, el valor que obtiene es el valor de esa moneda más lo que puede maximizar en las monedas restantes, sabiendo que el siguiente jugador tomará de forma óptima. El mismo razonamiento aplica si toma la moneda derecha.

El hecho de que tomemos el mínimo de las opciones del jugador siguiente asegura que estamos considerando que ambos jugadores juegan de forma óptima, lo que maximiza el valor acumulado para el primer jugador.

Dado que la recurrencia es válida para subsecuencias más pequeñas y seguimos esta lógica inductiva para subsecuencias más grandes, hemos demostrado por inducción que la recurrencia lleva al valor máximo acumulado.

https://www.overleaf.com/project/671e691d3ed6d3b699e59ca3

