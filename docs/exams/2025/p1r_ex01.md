---
id: ex-2025-01
year: 2025
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Tenemos arrays de `2n` números enteros dispuestos de forma capicúa y ordenados en sentido ascendente-descendente. En la primera mitad del array hay `n` números ordenados de forma ascendente, y en la segunda mitad, los mismos `n` números pero ordenados de forma descendente. El valor de `n` siempre es una potencia de 2.

Un ejemplo de este tipo de arrays sería:  `[1 3 6 9 10 12 14 16 16 14 12 10 9 6 3 1]`. En este ejemplo, `n = 8`. Otro ejemplo con `n = 4` sería: `[1 2 3 4 4 3 2 1]`.

- (a) (1,5 puntos) Queremos utilizar el algoritmo de ordenación por burbuja como el incluido en las transparencias de la asignatura para ordenar estos arrays. A continuación se incluye una copia del algoritmo adaptado a estos arrays. ¿Cuál es el número de veces que se evalúa la condición del `if` en la línea 6, para este tipo de arrays en concreto?. Indique la respuesta en función del tamaño del array y justifíquela brevemente.

```{.java .numberLines}
public void burbuja(int[] data) { 
  boolean changed;
  do {
    changed = false;
    for (int i = 0; i < data.length - 1;i++) {
      if (data[i] > data[i + 1]) {
        swap(data, i, i + 1);
        changed = true;
      }
    }
  } while (changed);
}
```

??? note "Mostrar solución"
    La complejidad de peor caso de burbuja es $O(n^2)$ y mejor caso $O(n)$, donde $n$ es el tamaño del array. Para estos arrays de tamaño $2n$, el algoritmo de burbuja tiene que recolocar todos los números menos el primero. El bucle externo se ejecuta $2n - 1$ veces. El bucle interno también se ejecuta $2n - 1$ veces. El número total de comparaciones es $(2n - 1)^2$.


- (b) (2,5 puntos) Implemente un método que reciba como parámetro un array (con la misma estructura descrita anteriormente) y ordene sus elementos en orden ascendente.

La puntuación de este apartado se asignará según los criterios siguientes:

  - Si la solución no deja ordenado el array recibido, la puntuación no superará 0.5 puntos.
  - Si la complejidad es mayor que $O(n^2)$, la puntuación no superará 0.5 puntos.
  - Si la complejidad es mayor que $O(n\cdot log(n))$, la puntuación no superará 1 punto.
  - Si la complejidad es mayor que $O(n)$, la puntuación no superará 1.5 puntos.
  - Se valorará positivamente no utilizar arrays ni listas auxiliares o adicionales. En caso de emplearlos, la puntuación se reducirá al menos 1 punto.

No es necesario comprobar que el array recibido esté construido correctamente

??? note "Mostrar solución"
    Una posible solución para ordenar el array de forma ascendente es la siguiente:

    ```{.java .numberLines}
     public static void ordenaCapicuaAscendenteArray(int[] arr) {
       int dest = arr.length - 1;
       for (int org = arr.length / 2 - 1; org >= 0; org--) {
           arr[dest--] = arr[org];
           arr[dest--] = arr[org];
       }
     }
    ```


- (c) (1 punto) Calcule la complejidad del algoritmo implementado en el apartado 2, justificando su razonamiento y mostrando los pasos seguidos hasta llegar a la expresión final.

??? note "Mostrar solución"
    La complejidad de esta solución es $O(n)$, donde $2n$ es el tamaño del array. El bucle `for` de la línea 3 se ejecuta $n$ veces y las sentencias del cuerpo del bucle son de coste constante $O(1)$.
