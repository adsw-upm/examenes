---
id: ex-2013-01
year: 2013
exam: extraordinario
tags:
    - complejidad
---

La siguiente clase implementa un conjunto de enteros ordenados mediante un árbol binario. El árbol no contiene datos duplicados.
```java
public class Arbol {
    private class Nodo {
        int valor;
        Nodo izq, der;
    }

    private Nodo raiz;
    private int n; // número de datos almacenados en el árbol
    ...
    public int cuenta(int x) {...} // número de valores <= x
    ...
}
```
- (a) (1,5 puntos) Escriba el método ```int cuenta(int x)``` de forma que devuelva el número de valores menores o
iguales que ```x``` en el árbol.

Ejemplo:

Si el árbol contiene los valores (1,3,4,6,10,14), obtendremos
 - cuenta(1) = 1
 - cuenta(6) = 4
 - cuenta(9) = 4

??? note "Mostrar solución"
    Una posible implementación del método, utilizando un método auxiliar recursivo, es la siguiente:

    ```java
    public int cuenta(int x) {
        return cuenta(raiz, x);
    }

    private int cuenta(Nodo nodo, int x) {
        if (nodo == null) {
            return 0;
        }

        if (nodo.valor == x) { 
            // suma 1 y sigue buscando por la izquierda
            return 1 + cuenta(nodo.izq, x);
        } else if (nodo.valor < x) { 
            // suma 1 y sigue buscando por los dos lados
            return 1 + cuenta(nodo.izq, x) + cuenta(nodo.der, x);
        } else { 
            // no suma y sigue buscando por la izquierda
            return cuenta(nodo.izq, x);
        }
    }
    ```
    El algoritmo usa la propiedad del árbol binario de búsqueda de que todos los nodos que están en el subárbol izquierdo de uno dado tienen un valor menor que éste. Por tanto, si se encuentra el valor ```x``` ya no hay que seguir buscando por su derecha. Si el valor del nodo es menor que ```x```, puede haber nodos menores tanto a la izquierda como a la derecha. Por último, si el valor del nodo es mayor que ```x```, basta con seguir contando por la izquierda, ya que los nodos que haya a la derecha serán también mayores que ```x```.


- (b) (1,5 puntos) Calcule la complejidad del algoritmo, justificando el resultado ne

??? note "Mostrar solución"
    Para la complejidad, observamos que se van recorriendo todos los nodos del árbol, excepto cuando se encuentra un valor mayor que x, en cuyo caso se descarta el subárbol derecho.

    Más en detalle, el método cuenta tiene cuatro casos posibles. Si calculamos el número de operaciones que se hacen cada vez que se ejecuta, tenemos
    - Sumas:
        1) nodo == null:! T(n) = 0
        2) nodo.valor == x! T(n) = 1 + T(n/2)
        3) nodo.valor < x! T(n) = 2 + 2T(n/2)
        4) nodo.valor > x! T(n) = T(n/2)
    - Llamadas recursivas:
        1) nodo == null:! T(n) = 0
        2) nodo.valor == x! T(n) = 1 + T(n/2)
        3) nodo.valor < x! T(n) = 1 + 2T(n/2)
        4) nodo.valor > x! T(n) = T(n/2)
    Suponiendo que el caso 3 es el más frecuente,
        T(n) ≈ 1 + 2T(n/2)
    que es lineal, O(n).