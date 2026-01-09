---
id: ex-2014-01
year: 2014
exam: parcial 1 recuperacion
tags:
 - complejidad
---

- (a) (5 puntos) Se llama montón (*heap*) a un *array* de valores enteros en el que, representado como un árbol binario, todo nodo es mayor o igual que culaquiera de sus dos hijos (si existen):

![](./p1/p1r_ex1.png)

Se ve que para todo nodo representado en la posición `i` de un array su hijo izquierdo se encuentra en la posición `2·i + 1` y su hijo derecho se encuentra en la posición `2·i + 2`.

Así pues, para ordenar de mayor a menor un conjunto de valores enteros, basta con colocarlos primero como un montón, y después ir extrayendo sucesivamente el primer valor del array (la raíz principal), y a continuación recuperar el montón de los elementos restantes, hasta que no quede ningún elemento.

Para recuperar el montón de los restantes elementos cuando se extrae el primer elemento de la tabla, basta con colocar en su lugar el último, y a continuación hacer descender éste en el árbol iterativamente, si resulta necesario, hasta el nivel donde no sea menor que ninguno de sus dos (posibles) descendientes. Detrás se puede ver el código de esta operación, aunque no resulta necesario en absoluto consultarlo, si se ha entendido correctamente este párrafo.

Sabiendo que la operación de construir un montón a partir de un array de enteros cualquiera tiene una complejidad del orden de n ∗ log(n), se pide encontrar y justificar la complejidad del algoritmo completo de ordenación descrito

```java
private static int[] montonOrdenado(int[] monton) {
    int[] resultado = new int[monton.length];

    for (int j = 0; j < monton.length; j++) {
        resultado[j] = monton[0];

        int ultimoIndice = monton.length - 1 - j;
        monton[0] = monton[ultimoIndice];
        --ultimoIndice;

        int i = 0;
        while (true) {
            int indiceHijoIzquierdo = 2 * i + 1;
            int indiceHijoDerecho = 2 * i + 2;

            // No hay hijos
            if (indiceHijoIzquierdo > ultimoIndice)
                break;

            // Solo hay hijo izquierdo
            if (indiceHijoDerecho > ultimoIndice) {
                if (monton[i] < monton[indiceHijoIzquierdo])
                    intercambia(monton, i, indiceHijoIzquierdo);
                break;
            }

            // Ambos hijos son menores o iguales
            if ((monton[i] >= monton[indiceHijoIzquierdo])
                    && (monton[i] >= monton[indiceHijoDerecho]))
                break;

            // Uno de los hijos es mayor
            if (monton[indiceHijoDerecho] < monton[indiceHijoIzquierdo]) {
                intercambia(monton, i, indiceHijoIzquierdo);
                i = indiceHijoIzquierdo;
            } else {
                intercambia(monton, i, indiceHijoDerecho);
                i = indiceHijoDerecho;
            }
        }
    }
    return resultado;
}

private static void intercambia(int[] array, int i, int j) {
    int t = array[i];
    array[i] = array[j];
    array[j] = t;
}
```

??? note "Mostrar solución"
    En la extracción de los valores en orden (descendente) del *array*, para cada uno de ellos hay que hacer descender en el árbol la nueva raiz, hasta que encuentre un lugar apropiado para que se siga cumpliendo la condición de *heap*. Y como el árbol está siempre equilibrado, este descenso será, como mucho, de longitud log(n).
    
    Como, por otra parte, esta operación ha de realizarse para cada uno de los valores del array, la complejidad de la extracción ordenada de los n valores será de orden n·log(n). Con lo que se tiene una complejidad para el algoritmo de ordenación completo (creación del heap original más extracción ordenada de todos sus valores) de orden n·log(n) + n·log(n). Expresión que, según las reglas de combinación de órdenes de complejidad, equivale simplemente a n·log(n).