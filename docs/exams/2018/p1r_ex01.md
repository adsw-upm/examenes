---
id: ex-2018-01
year: 2018
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Dado un conjunto `P` de puntos en un plano de 2 dimensiones, necesitamos calcular el subconjunto de `P` tal que una banda elástica alrededor de ellos no deja a ningún punto fuera.

En geometría, a este subconjunto se le denomina envolvente convexa (*convex hull*). Una de sus propiedades es que si enumeramos los puntos según las agujas del reloj (`L1, L2, ..., Ln`) todos los pares de segmentos consecutivos van girando hacia la derecha. Por ejemplo, `L1-L2` está girado a la derecha en comparación con `L0-L1`.

En Internet hemos encontrado este algoritmo (Andrew, 1979) que divide el problema en 2 partes. Calcula la envolvente superior, luego la inferior, y las une.

El algoritmo es como sigue para un conjunto de `N` puntos:

1. Se ordenan los puntos `P` en orden creciente de coordenada `X` y, si tienen el mismo `X`, en orden creciente de coordenada `Y`;
2. Se prepara una lista `UPPER` con los 2 primeros puntos, `L0` y `L1`;
3. Para `i` entre `2` y `N`:
    1. Se añade `Li` a la lista `UPPER`;
    2. Mientras los 3 últimos puntos en la lista `UPPER` hagan un giro a la izquierda, se elimina el punto intermedio de esos 3.
4. Se prepara una lista `LOWER` con los 2 últimos puntos `L(n-1), L(n-2)`;
5. Para `i` entre `N-3` y `0`, descendiendo:
    1. Se añade `Li` a la lista `LOWER`;
    2. Mientras los 3 últimos puntos en la lista `LOWER` hagan un giro a la izquierda, se elimina el punto intermedio de esos 3.
6. Se concatenan las listas `UPPER` y `LOWER` prescindiendo de los puntos finales de cada una.

Suponga que disponemos de un método auxiliar que, dados 3 puntos, nos dice si los segmentos `AB` y `BC` hacen un giro a la izquierda: 
```java
boolean giroIzquierda(Punto A, Punto B, Punto C)
```

- (a) (5 puntos) Calcular la complejidad del algoritmo en función del tamaño `N` del conjunto de puntos `P`.

??? note "Mostrar solución"
    El método auxiliar, `giroIzquierda()`, trabaja sobre 3 puntos `A`, `B`, y `C` y es por tanto independiente del tamaño `N` del conjunto de puntos. Su complejidad es $O(1)$.
    
    El algoritmo principal ordena una lista de `N` puntos. La comparación entre 2 puntos `A` y `B` es independiente del número de puntos, y por tanto es de complejidad $O(1)$. El algoritmo de ordenación introduce su propia complejidad que se puede estimar en $O(n log n)$ si escogemos un buen algoritmo como puede ser el *merge sort*.
    
    El algoritmo global:
    
    | Paso | Descripción          | Complejidad |
    |-----:|----------------------|-------------|
    | 1    | Ordenación           | $O(n log n)$|
    | 2    | `new list UPPER`     | $O(1)$      |
    | 3    | bucle `2..N`         | $O(n)$(*)   |
    | 4    | `new list LOWER`     | $O(1)$      |
    | 5    | bucle `2..N`         | $O(n)$(*)   |
    | 6    | concatena            | $O(n)$      |
    | TOTAL|                      | $O(n log n)$|
    
    (*) En principio parece un bucle de `N` veces sobre una lista que va creciendo hasta `N`; resultando en $n^2$. Pero ocurre que cada pasada por el bucle elimina un elemento de la lista y o la lista es larga y el `while` termina pronto, o al revés. En resumen, que por una razón u otra no pasamos de $O(n)$. En otras palabras, la combinación `FOR-WHILE` recorre exactamente `N` puntos, bien conservando cada punto o eliminándolo.
    
    Por otra parte, la operación `remove(penúltimo)` es independiente del tamaño de la lista y, por tanto, de $O(1)$.
    
    Codificación en Java:
    ```java
    List<Punto> scan(List<Punto> puntos) {
        if (puntos.size() < 3) return null;
    
        puntos.sort(new Comparator<Punto>() {
            @Override
            public int compare(Punto p1, Punto p2) {
                if (p1.x == p2.x)
                    return p1.y - p2.y;
                return p1.x - p2.x;
            }
        });
    
        List<Punto> upper = new ArrayList<>();
        upper.add(puntos.get(0));
        upper.add(puntos.get(1));
    
        for (int i = 2; i < puntos.size(); i++) {
            upper.add(puntos.get(i));
            while (true) {
                int size = upper.size();
                if (size < 3)
                    break;
                Punto A = upper.get(size - 3);
                Punto B = upper.get(size - 2);
                Punto C = upper.get(size - 1);
                if (!isGiroIzquierda(A, B, C))
                    break;
                upper.remove(size - 2);
            }
        }
    
        int n = puntos.size();
        List<Punto> lower = new ArrayList<>();
        lower.add(puntos.get(n - 1));
        lower.add(puntos.get(n - 2));
    
        for (int i = n - 3; i >= 0; i--) {
            lower.add(puntos.get(i));
            while (true) {
                int size = lower.size();
                if (size < 3)
                    break;
                Punto A = lower.get(size - 3);
                Punto B = lower.get(size - 2);
                Punto C = lower.get(size - 1);
                if (!isGiroIzquierda(A, B, C))
                    break;
                lower.remove(size - 2);
            }
        }
    
        List<Punto> hull = new ArrayList<>();
        hull.addAll(upper);
        hull.remove(hull.size() - 1);
        hull.addAll(lower);
        hull.remove(hull.size() - 1);
    
        return hull;
    }
    
    private boolean isGiroIzquierda(Punto A, Punto B, Punto C) {
        int x1 = A.getX();
        int y1 = A.getY();
        int x2 = B.getX();
        int y2 = B.getY();
        int x3 = C.getX();
        int y3 = C.getY();
    
        int val1 = (x2 - x1) * (y3 - y1);
        int val2 = (y2 - y1) * (x3 - x1);
    
        return val1 > val2;
    }
    ```
