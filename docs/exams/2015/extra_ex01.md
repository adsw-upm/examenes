---
id: ex-2015-01
year: 2015
exam: extraordinario
tags:
 - complejidad
---

Para un programa de análisis del genoma humano, necesitamos encontrar una subsecuencia de elementos en orden creciente. Esto corresponde a un problema de programación conocido como LIS (Longest Increasing Subsequence) donde, por ejemplo, dada la secuencia:

{0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}

una solución es [0, 2, 6, 9, 11, 15] (la solución no es necesariamente única).

Buscando por Internet encontramos esta solución que hemos probado y pasa las pruebas:
```java
int[] lis(int[] x) {
    int n = x.length;
    int[] p = new int[n];
    int[] m = new int[n + 1];
    int le = 0;

    for (int i = 0; i < n; i++) {
        int lo = 1;
        int hi = le;
        while (lo <= hi) {
            int mid = (lo + hi + 1) / 2;
            if (x[m[mid]] < x[i])
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        int newLe = lo;
        p[i] = m[newLe - 1];
        m[newLe] = i;
        if (newLe > le)
            le = newLe;
    }

    int[] s = new int[le];
    int k = m[le];
    for (int i = le - 1; i >= 0; i--) {
        s[i] = x[k];
        k = p[k];
    }
    return s;
}
```

- (a) (4 puntos) Se pide calcular su complejidad en función de tamaño $N$ de la secuencia de entrada, razonando la solución. NOTA: A efectos del examen se valorará más el razonamiento que el resultado final.

??? note "Mostrar solución"
    Al principio hay un doble bucle anidado, siendo el bucle externo de complejidad lineal, mientras que el bucle interno es en principio de complejidad logarítmica, ya que hace búsqueda dicotómica en un intervalo de tamaño no mayor que $n$.  Visto en más detalle, el bucle interno empieza con un intervalo de una unidad y aumenta su tamaño como mucho en una unidad más en cada vuelta al bucle externo (algunas vueltas se incrementa en una unidad y algunas vueltas no se incrementa).  Así pues, su tiempo de ejecución estará acotado por una constante que multiplica a $(log 1 + log 2 ... log n)$, lo cual es igual a $log(1*2*...n)$, es decir, $log(n!)$. Cantidad que puede acotarse también por $log(n^n)$, es decir, $n*log(n)$ (aplicando la fórmula de Stirling se obtiene un valor mas aproximado, $(n*log n - n)$, pero del mismo orden de complejidad). Es decir, el bucle doble tiene complejidad lineal logarítmica. Y a continuación del bucle doble anidado hay un bucle simple que es de complejidad lineal.

    Sumando todas las complejidades individuales según su regla (el resultado es el término de mayor complejidad), la complejidad del algoritmo descrito resulta ser lineal logarítmica. En términos formales: 

    $C(for.while) = O(log 1 + log 2 ... log n) = O(log(1*2*...n)) = O(log(n!)) = O(n*log n)$

    $C(lis) =$

    $= C(for.while) + C(for)$

    $= O(n*log n) + O(n)$

    $= O(n*log n)$