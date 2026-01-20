---
id: ex-2018-02
year: 2018
exam: extraordinario
tags:
 - complejidad
---


Disponemos de las clases Datos, DatosOrdenado y BST, cuyos esquemas se pueden ver debajo. La case Datos almacena valores enteros sin ordenar en un array de tamaño fijado en el constructor. La clase DatosOrdenado almacena valores enteros ordenados de menor a mayor en un array de tamaño fijado en el constructor. La clase BST almacena valores enteros en un BST, donde en cada nodo del árbol se almacena un número entero en el campo valor.
```java
public class Datos {
    private int[] valores;
    // …..
    public int cuentaMenores(int val) {
        // …
    }
    // …
}

public class DatosOrdenado {
    private int[] valores;
    // …..
    public int cuentaMenores(int val) {
        // …
    }
    // …
}

public class BST {
    private class Nodo {
        int valor;
        Nodo izd;
        Nodo der;
    }

    private Nodo raiz;
    // …..
    public int cuentaMenores(int val) {
        // …
    }
    // …
}
```

En una aplicación concreta que estamos desarrollando, deseamos conocer cuántos valores almacenados son menores que un cierto valor val que se pasa como parámetro. Este valor que se pasa como parámetro puede no ser uno de los valores almacenados.

- (a) (2,5 puntos) Codificar el método public int cuentaMenores (int val), en cada una de las 3 clases: Datos, DatosOrdenado y BST. Nota: Para simplificar suponga que tanto en Datos como en DatosOrdenado, los arrays de enteros están ocupados en su totalidad por valores almacenados. Suponga que no hay datos repetidos y que no hay operaciones de modificación (inserción o borrado), sino exclusivamente se trata de buscar en una estructura de datos construida.

??? note "Mostrar solución"
    ```java
    class Datos {
        public int cuentaMenores(int val) {
            int cuenta = 0;
            for (int i = 0; i < nValores; i++) {
                if (valores[i] < val)
                    cuenta++;
            }
            return cuenta;
        }
    }

    class DatosOrdenado {
        public int cuentaMenores(int val) {
            int n = valores.length;
            int centro, inf = 0, sup = n - 1;
            while (inf <= sup) {
                centro = (sup + inf) / 2;
                if (valores[centro] == val)
                    return centro;
                else if (val < valores[centro]) {
                    sup = centro - 1;
                } else {
                    inf = centro + 1;
                }
            }
            return sup + 1;
        }
    }

    class BST {
        private int cuentaMenores(Nodo actual, int val) {
            int cuenta = 0;
            if (actual == null)
                return 0;
            if (actual.valor == val)
                return cuentaTodos(actual.izd);
            if (actual.valor < val)
                cuenta = 1;
            int nizd = cuentaMenores(actual.izd, val);
            int nder = cuentaMenores(actual.der, val);
            return cuenta + nizd + nder;
        }

        private int cuentaTodos(Nodo actual) {
            if (actual == null)
                return 0;
            return 1 + cuentaTodos(actual.izd) + cuentaTodos(actual.der);
        }
    }
    ```


- (b) (2,5 puntos) Se pide: Considerando sólo los métodos cuentaMenores que acaba de implementar, cuál de las tres clases seleccionaría para almacenar un conjunto de valores de tamaño fijo (M) donde se vayan a realizar frecuentes llamas al método cuentaMenores.

??? note "Mostrar solución"
    La clase Datos al tener los valores no ordenados nos obliga a recorrer todo el array, por lo tanto, la complejidad es proporcional al número de valores almacenados: O(N)

    La Clase DatosOrdenado, tiene los valores ordenados de menor a mayor. Que los valores estén ordenados permite utilizar búsqueda dicotómica para localizar el valor, o en su defecto la posición donde debería estar el valor que estamos buscando. Esta operación tiene una complejidad O(log N). Una vez localizada la posición donde está o debería estar el valor, todos los de la izquierda son menores que él, por lo tanto, por lo que directamente conocemos el número de valores menores que el que nos pasan como parámetro usando el índice de la posición del array donde está o debería estar el valor pasado como parámetro. El resultado es un algoritmo de orden O(log N)

    En el caso del BST la estructura de BST ayuda a encontrar el valor en el árbol con una complejidad O(log N),pero como lo que nos piden es el número de valores menor que el valor pasado como parámetro, e incluso puede ocurrir que le propio valor no se encuentre en el árbol, debemos recorrer casi todo el árbol con una complejidad O(N).

    Por lo tanto, a la vista de este análisis, para nuestro problema concreto, la clase seleccionada es DatosOrdenado

