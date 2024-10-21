# TDA-Integrador

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
