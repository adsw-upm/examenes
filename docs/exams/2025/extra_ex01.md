---
id: ex-2025-01
year: 2025
exam: extraordinario
tags:
 - complejidad
---

Se quiere desarrollar un algoritmo al que llamaremos *split sort*.
Este algoritmo es similar a la fase de *merge* en *merge sort*.
Se parte de dos arrays `a` y `b`, de igual tamaño, sin elementos repetidos y ya ordenados de menor a mayor.
A diferencia de *merge*, nuestro *split sort* funciona en el sitio (*in place*).
Tras aplicar el algoritmo:

  * Los menores elementos deben quedar en `a`
  * Los mayores elementos deben quedar en `b`
  * Tanto `a` como `b` siguen estando ordenados correctamente
  * El conjunto de números (es decir, números contenidos en `a` o `b`) siguen siendo los mismos

Por ejemplo, si partimos de `a = [1, 3, 5, 7]; b = [2, 4, 6, 8]`, el resultado sería `a = [1, 2, 3, 4]`; `b = [5, 6, 7, 8]`.

Se pide:

- (a) (0.5 puntos) Describir al menos 5 casos en los que probar este código y el resultado esperado. Se valorará que los casos sean distintos y representativos.

??? note "Mostrar solución"
    Casos de prueba para el método `splitSort`:

       - Caso 1: `a = [1, 3, 5, 7]`, `b = [2, 4, 6, 8]` $\rightarrow$ Resultado esperado: `a = [1, 2, 3, 4]`, `b = [5, 6, 7, 8]`
       - Caso 2: `a = [10, 20, 30]`, `b = [15, 25, 35]` $\rightarrow$ Resultado esperado: `a = [10, 15, 20]`, `b = [25, 30, 35]`
       - Caso 3: `a = [5, 10]`, `b = [1, 2]` $\rightarrow$ Resultado esperado: `a = [1, 2]`, `b = [5, 10]`
       - Caso 4: `a = [1000, 2000]`, `b = [1500, 2500]` $\rightarrow$ Resultado esperado: `a = [1000, 1500]`, `b = [2000, 2500]`
       - Caso 5: `a = [3]`, `b = [4]` $\rightarrow$ Resultado esperado: `a = [3]`, `b = [4]`


- (b) (4 puntos) Desarrollar el código del método `void splitSort(int[] a, int[] b)`. Se valorará:

    * Que los arrays contengan los mismos elementos al final
    * Que `a` contenga los elementos menores y `b` los mayores
    * Que ambos arrays estén ordenados al terminar
    * No se permite crear nuevos arrays ni listas. Solo pueden modificarse `a` y `b`.

??? note "Mostrar solución"
    Una posible implementación del método `splitSort` en Java:
    ```{.java .numberLines}
    public static void splitSort(int[] a, int[] b) {
      int n = a.length;
      int m = b.length;

      for (int i = 0; i < n; i++) {
        if (a[i] > b[0]) {
          // Intercambiar a[i] con el menor de b
          int temp = a[i];
          a[i] = b[0];
          b[0] = temp;

          // Reordenar b (insertion sort para mantenerlo ordenado)
          int j = 0;
          while (j + 1 < m && b[j] > b[j + 1]) {
            int aux = b[j];
            b[j] = b[j + 1];
            b[j + 1] = aux;
            j++;
          }
        }
      }
    }
    ```


- (c) (0.5 puntos) Escribir el código necesario para probar el método `splitSort` en al menos 1 caso. 

??? note "Mostrar solución"
    ```{.java .numberLines}
    @Test
    public void testTodosMenoresEnB() {
      int[] a = {10, 12, 14};
      int[] b = {1, 2, 3};
      Ejercicio4.splitSort(a, b);
      assertSortedSplit(new int[]{1, 2, 3}, new int[]{10, 12, 14}, a, b);
    }
    
    @Test
    public void testYaOrdenado() {
      int[] a = {1, 2, 3};
      int[] b = {4, 5, 6};
      Ejercicio4.splitSort(a, b);
      assertSortedSplit(new int[]{1, 2, 3}, new int[]{4, 5, 6}, a, b);
    }
    ```
