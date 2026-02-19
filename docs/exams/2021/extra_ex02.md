---
id: ex-2021-02
year: 2021
exam: extraordinario
tags:
 - complejidad
---

Se quiere evaluar tres algoritmos que calculan cuántas veces aparecen los números en un rango de valores enteros en otra secuencia de enteros representada en un array desordenado y sin valores repetidos. Los tres algoritmos retornan los mismos valores y son correctos. La signatura de los tres algoritmos es: `buscar(int[] buscados, int inicio, int fin)`, donde: `buscados` es el array de enteros e `inicio` y `fin` (`inicio <= fin`) determinan el rango de enteros a buscar.

Por ejemplo: `buscados = [1, 9, 4, 5, -3, 8, 7]`; `inicio = 5, fin = 7`. Entonces, habría que contar el número de veces que aparecen los enteros de la secuencia: 5, 6, 7. El resultado será: 2, ya que el 5 aparece una vez, el 6 no aparece y el 7 aparece una vez. 

```java
public static int buscar1(int[] buscados, int inicio, int fin) {
    int encontrados = 0;
    ordenaOptimo(buscados);

    for (int unNumero = inicio; unNumero <= fin; unNumero++) {
        if (busquedaBinaria(buscados, unNumero) != -1) {
            encontrados++;
        }
    }
    return encontrados;
}

public static int buscar2(int[] buscados, int inicio, int fin) {
    int encontrados = 0;

    for (int unNumero = inicio; unNumero <= fin; unNumero++) {
        for (int i = 0; i < buscados.length; i++) {
            if (buscados[i] == unNumero) {
                encontrados++;
                break;
            }
        }
    }
    return encontrados;
}

public static int buscar3(int[] buscados, int inicio, int fin) {
    int encontrados = 0;
    ordenaOptimo(buscados);

    int principio = buscaMasCercano(buscados, inicio, true);
    int final_ = buscaMasCercano(buscados, fin, false);
    int dif = final_ - principio;

    if ((principio < 0 && fin != buscados[final_]) ||
        (principio == buscados.length - 1 && inicio != buscados[principio])) {
        dif--;
    } else {
        if (principio >= 0 && final_ < buscados.length &&
            inicio != buscados[principio] && fin != buscados[final_]) {
            dif--;
        }
        if (principio >= 0 && final_ < buscados.length &&
            inicio == buscados[principio] && fin == buscados[final_]) {
            dif++;
        }
    }
    return dif;
}
```

Se describen algunos aspectos sobre los métodos auxiliares del código:

- `ordenaOptimo`: implementa un algoritmo de ordenación del array en orden ascendente, y tiene una complejidad $n log n$ (donde $n$ es el tamaño del array que recibe como parámetro). Al completar este método, el array de entrada estará ordenado.
- `busquedaBinaria`: implementa un algoritmo de búsqueda binaria, de un entero, en un array ordenado; devuelve la posición del número en el array, o -1 si no se encuentra en el array.
- `buscaMasCercano`: en un array ordenado, busca la posición cuyo valor es el más próximo al segundo parámetro. La implementación de este método emplea un algoritmo de búsqueda binaria de complejidad $log n.
- En el método `buscar2`, se supone que el número de veces que se ejecuta el segundo bucle es $N/2$.

¿Cuál de los tres algoritmos se debería utilizar en los siguientes casos? Justifique cada caso, para cada algoritmo, indicando la complejidad del algoritmo. $N$ es el número de elementos en el array y $M$ es el número de elementos en la secuencia de búsqueda `(fin – inicio + 1)`.

- (a) (1,5 puntos) $M=2$ y $N$ es número muy grande.

??? note "Mostrar solución"
    La complejidad del método `buscar1` es:
    
    $N log N$, esto es `ordenarOptimo`;
    
    $M log N$, esto es el bucle `for`;
    
    La complejidad depende de los valores $N$ y $M$.

    La complejidad del método `buscar2` es: $M*N/2$

    La complejidad del método `buscar3` es:
    
    $N log N$, esto es `ordenarOptimo`;
    
    $2 log N$, esto la complejidad de ejecución 2 veces de `buscaMasCercano`.
    
    La complejidad es $N log N$.


- (b) (1,5 puntos) $M = N$, ambos números grandes. 

??? note "Mostrar solución"
    Caso 1, $M = 2$:
    
    La complejidad de `buscar1` es $N log N$;
    
    La complejidad de `buscar2` es $N$;
    
    La complejidad de `buscar3` es $N log N$;

    Es mejor algoritmo `buscar2`.


    Caso 2, $M = N$:

    La complejidad de `buscar1` es $N log N$;

    La complejidad de `buscar2` es $N2/2$;

    La complejidad de `buscar3` es $N log N$;

    Es mejor algoritmo `buscar1` o `buscar3`.

    Caso 3, $M >> N$:

    La complejidad de `buscar1` es $M log N$;

    La complejidad de `buscar2` es $M*N/2$;

    La complejidad de `buscar3` es $N log N$;
    
    Es mejor el algoritmo `buscar3`.


- (c) (2 puntos) $M$ es bastante más grande que $N$, y ambos son grandes.

??? note "Mostrar solución"
    Vacío

