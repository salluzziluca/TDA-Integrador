# TDA-Integrador

# Complejidad algoritmica

Cada iteracion recorro 4 posiciones. Por lo tanto la complejidad del while es n/2. Y luego la complejidad de elegir moneda es O(1) ya que solo se hace una operacion de comparacion y otra de pop o popleft, ambos O(1) porque estamos usando un deque. Por lo tanto la complejidad total es O(n/2) = O(n)

## Pares

n, n+1, n+2, n+3 -> S: n+3 n+2 M:n n+1

n, n+1, n+3, n+2 -> S: n+2 n+3 M: n n+1

n, n+2, n+1, n+3 -> S: n+3 n+2 M: n n+1

n, n+2, n+3, n+1 -> S: n+1 n+3 M: n n+2

n, n+3, n+1, n+2 -> S: n+2 n+3 M: n n+2

n, n+3, n+2, n+1 -> S: n+1 n+3 M: n n+2

n+1, n, n+2, n+3 -> S: n+3 n+2 M: n+1 n

n+1, n, n+3, n+2 -> S: n+2 n+3 M: n+1 n

n+1, n+2, n, n+3 -> S: n+3 n+2 M: n+1 n

n+1, n+2, n+3, n -> S: n+1 n+3 M: n+2 n

n+1, n+3, n, n+2 -> S: n+2 n+3 M: n+1 n

n+1, n+3, n+2, n -> S: n+1 n+3 M: n+2 n

n+2, n, n+1, n+3 -> S: n+3 n+2 M: n+1 n

n+2, n, n+3, n+1 -> S: n+2 n+3 M: n+1 n

n+2, n+1, n, n+3 -> S: n+3 n+2 M: n+1 n

n+2, n+1, n+3, n -> S: n+2 n+3 M: n n+1

n+2, n+3, n, n+1 -> S: n+2 n+3 M: n+1 n

n+2, n+3, n+1, n -> S: n+2 n+3 M: n n+1

n+3, n, n+1, n+2 -> S: n+3 n+2 M: n n+1

n+3, n, n+2, n+1 -> S: n+3 n+2 M: n n+1

n+3, n+1, n, n+2 -> S: n+3 n+2 M: n+1 n

n+3, n+1, n+2, n -> S: n+3 n+2 M: n n+1

n+3, n+2, n, n+1 -> S: n+3 n+2 M: n+1 n

n+3, n+2, n+1, n -> S: n+3 n+2 M: n n+1

## Impares

n, n+1, n+2 -> S: n+2 n+1 M: n

n+1, n+2, n -> S: n+1 n+2 M: n

n, n+2, n+1 -> S: n+1 n+2 M: n

n+2, n, n+1 -> S: n+1 n+2 M: n

n+1, n, n+2 -> S: n+2 n+1 M: n

n+2, n+1, n -> S: n+2 n+1 M: n

Podriamos decir que para todo conjunto par o impar de numeros, Sophia siempre ganara sin importar el orden en el que se encuentren los numeros.

## Prueba por absurdo

Si en vez de elegir la mas grande elije la mas chica, esto le dará alguna ventaja en un futuro a nivel global?

Si ella agarra la moneda mas grande en su turno, deja a Mateo con dos peores opciones, en una situacion menos ventajosa.
Si por lo contrario agarra una moneda mas chica, esta le daria a ella una desventaja en el futuro.
EJ: Tengo la situacion [3, 9, 1, 2], Si Sophia sigue el algoritmo greedy, deberia agarrar la 3. Pero ella puede llegar a pensar que le conviene agarrar el 2 para forzar una situacion de desventaja en el turno de mateo (que se vea obligado a agarrar el 1).

Por greedy: Sophia: [3, 9] Mateo: [2, 1]
Sin greedy: Sophia: [2, 9 ] Mateo: [1, 3]

Como se puede ver. Por greedy ella termina con un total de 12 puntos mientras que sin greedy termina con 11. Por lo tanto, no es conveniente para ella agarrar la moneda mas chica.

### Variabilidad con respecto a la optimalidad

El algoritmo es óptimo independientemente de la cantidad de monedas o sus valores, excepto en el caso de una cantidad par de monedas de mismo valor lo que resulta en empate siempre

## Base inductiva:

Con una sola moneda (n=1) Sophia gana porque empieza ella y la elige

5
Sophia: [5]
Mateo: []

## Paso inductivo:

Al agregar una moneda al problema Sophia sigue ganando porque Mateo agarra la menor (desestimamos el caso de una cantidad par de monedas de mismo valor ya que es inevitablemente empate)

5;1
Sophia: [5]
Mateo: [1]

Si seguimos agregando monedas va a ser lo mismo ya que Sophia va elegir la mayor y Mateo seguira eligiendo la menor, sumando siempre menos que Sophia para cualquier n

5;1;5
Sophia: [5;5]
Mateo: [1]

5;1;5;5
Sophia: [5;5]
Mateo: [5;1]

.
.
.

### Observaciones sobre la complejidad

1. **Entrada:**  
   La función recibe una lista de enteros `monedas` y la convierte en un `deque`, lo que permite operaciones eficientes en ambos extremos de la secuencia.

2. **Operaciones con `deque`:**

    - `deque.popleft()` tiene una complejidad de \(O(1)\).
    - `deque.pop()` tiene una complejidad de \(O(1)\).

3. **Bucle:**

    - El bucle `while deque_monedes` se ejecuta mientras haya monedas en el deque.
    - Dado que se elimina una moneda en cada iteración, el bucle se ejecuta \(n\) veces, donde \(n\) es el número inicial de monedas.

4. **Función `elegir_moneda`:**
    - Dentro del bucle, la función `elegir_moneda` se llama dos veces (una por cada jugador).
    - Esta función realiza un número constante de operaciones (\(O(1)\)) en cada llamada, ya que incluye comparaciones y una operación `popleft()` o `pop()`.

### Complejidad temporal general

-   El bucle `while` se ejecuta \(n\) veces.
-   Dentro del bucle, `elegir_moneda` se llama dos veces, y cada llamada toma \(O(1)\).
-   Por lo tanto, la complejidad total de la función es \(O(2n) = O(n)\).

### Complejidad espacial

-   El `deque` requiere \(O(n)\) espacio para almacenar las monedas.
-   No se utiliza memoria adicional significativa, ya que las variables `puntos_sophia` y `puntos_mateo` son escalares.

### Conclusión

-   **Complejidad temporal:** \(O(n)\)
-   **Complejidad espacial:** \(O(n)\)
