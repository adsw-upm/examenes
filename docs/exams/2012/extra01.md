---
id: ex-2012-03
year: 2012
exam: extraordinario
tags:
    - android
---

Se pide escribir un algoritmo para extraer la mediana de los valores de un array. Si un array de $N$ datos está ordenado, la mediana es el valor del medio, $\text{array}[N/2]$.

El objetivo es preparar un método:

```java
public long mediana(long[] datos)
```

que devuelve la mediana del array que se le pasa.

Debe partir del algoritmo de quicksort y modificarlo de forma que, cuando se separan los datos en dos partes, solo se siga procesando la parte que contiene la mediana, sin ordenar la otra.

Se pide:

- (a) (1 punto) Escribir el algoritmo de forma recursiva.

??? note "Mostrar solución"
    ```java
    package examen_20120702;
    import java.util.Arrays;
    import java.util.Random;

    public class P1 {
        public long mediana1(long[] datos) {
            mediana1(datos, 0, datos.length);
            return datos[datos.length / 2];
        }

        public long mediana2(long[] datos) {
            mediana2(datos, 0, datos.length);
            return datos[datos.length / 2];
        }

        private void mediana1(long[] datos, int a, int z) {
            long pivote = datos[(a + z) / 2];
            int inf = a;
            int sup = z;
            while (inf < sup) {
                while (datos[inf] < pivote)
                    inf++;
                while (pivote < datos[sup - 1])
                    sup--;
                if (inf < sup) {
                    long tmp = datos[inf];
                    datos[inf] = datos[sup - 1];
                    datos[sup - 1] = tmp;
                    inf++;
                    sup--;
                }
            }
            int mitad = datos.length / 2;
            if (a <= mitad && mitad < sup)
                mediana1(datos, a, sup);
            if (inf <= mitad && mitad < z)
                mediana1(datos, inf, z);
        }
    }
    ```


- (b) (1 punto) Escribir el algoritmo de forma iterativa.

??? note "Mostrar solución"
    ```java
    package examen_20120702;
    import java.util.Arrays;
    import java.util.Random;

    public class P1 {
        public long mediana1(long[] datos) {
            mediana1(datos, 0, datos.length);
            return datos[datos.length / 2];
        }

        public long mediana2(long[] datos) {
            mediana2(datos, 0, datos.length);
            return datos[datos.length / 2];
        }

        private void mediana2(long[] datos, int a, int z) {
            while (a < z) {
                long pivote = datos[(a + z) / 2];
                int inf = a;
                int sup = z;
                while (inf < sup) {
                    while (datos[inf] < pivote)
                        inf++;
                    while (pivote < datos[sup - 1])
                        sup--;
                    if (inf < sup) {
                        long tmp = datos[inf];
                        datos[inf] = datos[sup - 1];
                        datos[sup - 1] = tmp;
                        inf++;
                        sup--;
                    }
                }
                int mitad = datos.length / 2;
                if (a <= mitad && mitad < sup)
                    z = sup;
                else if (inf <= mitad && mitad < z)
                    a = inf;
                else
                    return;
            }
        }
    }
    ```
    

- (c) (1 punto) Calcular la complejidad razonando el por qué.

??? note "Mostrar solución"
    - Caso peor: el comportamiento es equivalente a quicksort cuando siempre se elige un pivote pésimo. La partición genera tamaños $1$ y $n-1$, por lo que el coste es:

    $n + (n-1) + (n-2) + \dots + 1 = O(n^2)$

    - Caso medio: cada paso divide el array aproximadamente por la mitad, y solo se sigue por la parte donde está la mediana:

    $n + \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \dots = 2n = O(n)$

    Por tanto:
    - Caso peor: $O(n^2)$
    - Caso medio: $O(n)$
    