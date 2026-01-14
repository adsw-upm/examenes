---
id: ex-2016-01
year: 2016
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Se quiere desarrollar un algoritmo que, dado un array de enteros, calcule cuál es el número que se repite más veces. Así, si el array contiene {2, 4, 3, 4, 2, 6, 1, 4, 4}, el algoritmo devuelve 4. Si hay empate, devuelve el primer
valor. Se pide:

- (a) (1 punto) Escribir un método en Java que compute el algoritmo descrito. Si el array está vacío o es nulo, se lanzará
una excepción. La cabecera del método debe ser:

```java
int mayoria (int []v) throws exception
```

??? note "Mostrar solución" 
    Hay varias posibles soluciones:
    
    1. hacer un histograma, eligiendo el valor mayor según se cuenta
    2. ordenar el array y contar repeticiones sucesivas
    
    Se incluye la solución 1, almacenando el histograma en un Map. Una posible solución es:
    ```java
    public static int mayoria(int[] v) throws Exception {
        if (v == null || v.length == 0)
            throw new IllegalArgumentException("mayoria: invalid argument");
    
        Map<Integer, Integer> histograma = new HashMap<Integer, Integer>();
        int masRep = v[0];        // candidato inicial
        int repeticiones = 1;    // aparece una vez
    
        for (int i = 0; i < v.length; i++) {
            Integer veces = histograma.get(v[i]);
            veces = (veces == null) ? 1 : veces + 1;
            histograma.put(v[i], veces);
    
            if (veces > repeticiones) {
                repeticiones = veces;
                masRep = v[i];
            }
        }
        return masRep;
    }
    ```



Se desea calcular la complejidad del método del apartado anterior. Se pide:

- (b) (1 punto) ¿Cuál es la ecuación de recurrencia?

??? note "Mostrar solución" 
    T(n) = T(n-1) +c si n > 1

    T(0) = d


(c) (1 punto) Determinar su complejidad.

??? note "Mostrar solución" 
    Se puede resolver la ecuación de (b) o razonar de la siguiente forma:

    Las instrucciones sencillas (if, asignaciones, acceso al array) son constantes O(1).

    El acceso al Map (get y put) podemos considerarlo también constante en condiciones adecuadas de carga.

    Sólo el bucle for depende de n, procesando cada elemento una única vez, ergo es de complejidad O(n).
    
    Como O(1) ⊆ O(n), el resultado es que el algoritmo es de complejidad O(n).

    Comentarios adicionales:
    - no puede existir un algoritmo mejor que O(n) porque al menos hay que ver cada elemento una vez.
    - se puede tener un algoritmo O(n2) si con un for vamos viendo cada elemento, y para cada elemento contamos el número de repeticiones recorriendo el array (for dentro de for).
    - el O(n log n) se obtiene en varias circunstancias:
        - suponiendo un algoritmo de ordenación de esa complejidad.
        - usando un árbol binario de búsqueda para almacenar el histograma.
