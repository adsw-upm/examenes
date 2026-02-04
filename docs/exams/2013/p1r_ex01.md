---
id: ex-2013-01
year: 2013
exam: parcial 1 recuperacion
tags:
 - complejidad
---
- (a) (2,5 puntos) Dada una matriz de enteros de tamaño $N×N$, desarrolle un algoritmo de orden $O(N^2)$ para averiguar si un valor $K$ está presente o no en la matriz. Razone el orden de complejidad del algoritmo desarrollado.

Ejemplo:
|---|-----|-----|-----|-----|
| 84|   32|  -13|   33|   13|
|---|-----|-----|-----|-----|
| 7 |   82|   93|   89|  -23|
|---|-----|-----|-----|-----|
| 31|  -24|  -28|   57|  -93|
|---|-----|-----|-----|-----|
| 86|  -71|  -44|   75|  -12|
|---|-----|-----|-----|-----|
|-10|  -18|   53|   24|   78|
|---|-----|-----|-----|-----|

```java
busca(matriz, 13) -> true;
busca(matriz, 50) -> false;
```

??? note "Mostrar solución"
    ```java
    boolean busca1(int[][] matriz, int m) {
        for (int x = 0; x < matriz.length; x++) {
            for (int y = 0; y < matriz[x].length; y++) {
                if (matriz[x][y] == m)
                    return true;
            }
        }
        return false;
    }
    ```
    En cuanto a la complejidad, es un bucle que hace $N$ vueltas, y en cada una hay otro bucle anidado que hace otras $N$ vueltas. Por tanto, en total es de $O(N^2)$.


Dada una matriz de enteros de tamaño $N×N$ que está ordenada de forma que:

$\forall i, j: matriz[i][j] \leq matriz[i+1][j] \wedge matriz[i][j] \leq matriz[i][j+1]$

(se cumple que cada elemento es menor o igual que el de abajo y el de la derecha).

Se propone el siguiente algoritmo de búsqueda de un dato `m`:

```java
private static boolean busca2(int[][] matriz, int m) {
    int xa = 0;
    int xz = matriz.length;
    int ya = 0;
    int yz = matriz[0].length;
    return busca2(matriz, xa, xz, ya, yz, m);
}

private static boolean busca2(int[][] matriz,
        int xa, int xz, int ya, int yz, int m) {

    if (xa >= xz || ya >= yz)
        return false;

    int xm = (xa + xz) / 2;
    int ym = (ya + yz) / 2;
    int ref = matriz[xm][ym];

    if (ref == m)
        return true;

    if (ref < m)
        return busca2(matriz, xm + 1, xz, ya, yz, m)
            || busca2(matriz, xa, xz, ym + 1, yz, m);
    else
        return busca2(matriz, xa, xm, ya, yz, m)
            || busca2(matriz, xa, xz, ya, ym, m);
}
```

- (b) (2,5 puntos) Se pide calcular la complejidad temporal del algoritmo, razonando el resultado.

Ejemplo:

|---|-----|-----|-----|-----|
|-93|  -71|  -28|  -18|    7|
|---|-----|-----|-----|-----|
|-44|  -24|  -13|   13|   33|
|---|-----|-----|-----|-----|
|-23|  -12|   24|   53|   78|
|---|-----|-----|-----|-----|
|-10|   31|   57|   82|   86|
|---|-----|-----|-----|-----|
| 32|   75|   84|   89|   93|
|---|-----|-----|-----|-----|


```java
busca(matriz, 13) -> true;
busca(matriz, 50) -> false;
```

??? note "Mostrar solución"
    Un problema de tamaño $X = N^2$ se parte en 2 subproblemas de tamaño $(X/2)$. Esto hace $k$ veces, siendo $ X/2^k = 1 \Rightarrow k = \log_2(X)$.
    
    En la primera ronda hay 1 comparación

    En la segunda ronda 2 comparaciones
    
    En la tercera ronda 4 comparaciones
    
    $\dots$
    
    En la $k$-ésima ronda, $2^k$ comparaciones

    El número total de comparaciones es la suma $1 + 2 + 2^2 + 2^3 + \dots + 2^k$

    Sustituyendo $2 * 2^{\log_2(X)} = 2X$
    
    Como $X = N^2$ la solución al problema cuesta $2N^2$ comparaciones, siendo de la familia $O(N^2)$.
