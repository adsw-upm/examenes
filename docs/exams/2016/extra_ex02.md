---
id: ex-2016-02
year: 2016
exam: extraordinario
tags:
 - complejidad
---

Se pide programar un método que determine si existen dos elementos de un array de enteros que sumen un cierto valor `K`.

```java
boolean check(int[] datos, int k)
```

Ejemplos:

```java
check([4, 6, 10, 8], 13) à FALSE
check([1, 4, 45, 6, 10, -8], 16) à TRUE
```

Razone la complejidad en tiempo de ejecución de dicho método.

Sugerencia. Para conseguir un algoritmo $O(N)$ puede meter los datos del array en un conjunto (similar al propuesto en la primera pregunta).

- (a) (3,5) Implemente el método y razone su complejidad. La complejidad del método ha de ser $O(N)$, en cualquier otro caso, solo se podrá optar a la mitad de los puntos.

??? note "Mostrar solución"
    La solución óptima, con complejidad $O(n)$ es:
    ```java
    static boolean check1(int[] data, int K) {
        Set<Integer> set = new HashSet<>();
        for (int v : data) {
            if (set.contains(K - v))
                return true;
            set.add(v);
        }
        return false;
    }
    ```
    El orden de complejidad es $O(N)$ porque se trata de un bucle que recorre los elementos del array y, dentro del bucle, las operaciones `contains()` y `add()` son $O(1)$.
    
    Soluciones alternativas con otros órdenes de complejidad son:

    * $O(n log n)$
    ```java
    static boolean check2(int[] data, int K) {
        int[] mdata = new int[data.length];
        System.arraycopy(data, 0, mdata, 0, data.length);
    
        Arrays.sort(mdata);
    
        int a = 0;
        int z = mdata.length - 1;
    
        while (a < z) {
            int s = mdata[a] + mdata[z];
            if (s == K)
                return true;
            if (s < K)
                a++;
            else
                z--;
        }
        return false;
    }
    ```
    
    * $O(n^2)$
    ```java
    static boolean check3(int[] data, int K) {
        for (int i = 0; i < data.length; i++) {
            for (int j = i + 1; j < data.length; j++) {
                if (data[i] + data[j] == K)
                    return true;
            }
        }
        return false;
    }
    ```
