---
id: ex-2024-01
year: 2024
exam: extraordinario
tags:
 - complejidad
---

Considere la clase `ArrayDoble`, con los atributos descritos en el diagrama de debajo. El atributo `array` es un array de enteros de dimensión `n`. Los elementos están separados en dos partes. Los `i` primeros elementos de este array son números impares ordenados de menor a mayor. Los últimos `n-i` elementos son números pares ordenados de menor a mayor. Puede haber posiciones vacías, cuyo valor será `null`, pero solo al final de cada una de las partes (par e impar). También puede haber valores repetidos. A continuación, se puede ver un ejemplo del contenido de este array:

![](./extra/extra_ex01-1.png)

![](./extra/extra_ex01-2.png)

Se pide, considerando como parcialmente válidas las implementaciones que apliquen simplificaciones y no cumplan todos los requisitos (p.e., que no consideren elementos duplicados):

- (a) (1.5 puntos) Implemente el método `buscar`. Este método debe devolver `true` cuando el valor buscado se encuentre en el array, y `false` en el resto de los casos. Su complejidad debe ser menor que $O(n)$. Justifique su elección de algoritmo. Puede crear tantos métodos auxiliares como considere adecuados.

??? note "Mostrar solución"
    El método buscar aplica búsqueda binaria sobre la parte adecuada del array. En el caso peor, su complejidad será $O(log(n))$.
    ```java
    public int posicion(Integer valor, int a, int z) {
        while (a < z) {
            int m = (a + z) / 2;
    
            if (this.array[m] == null) {
                z = m;
                continue;
            }
    
            if (this.array[m] == valor) {
                while (m > a && this.array[m - 1] == valor) {
                    m--;
                }
                return m;
            }
    
            if (this.array[m] < valor) {
                a = m + 1;
            } else {
                z = m;
            }
        }
        return a;
    }
    
    public boolean buscar(Integer valor) {
        int a = 0;
        int z = i;
    
        if (valor % 2 == 0) {
            a = i;
            z = this.array.length;
        }
    
        int pos = this.posicion(valor, a, z);
        if (pos < this.array.length) {
            return this.array[pos] == valor;
        }
        return false;
    }
    ```


- (b) (2.5 puntos) Implemente el método `eliminar`. Tras ejecutar este método, ningún elemento del array debe coincidir con ese valor, y las condiciones del enunciado sobre el orden de los valores y la posición de los valores `null` deben seguir cumpliéndose.

??? note "Mostrar solución"
    Hay al menos dos alternativas a la hora de eliminar un elemento impar. Pueden desplazarse todos los elementos a la derecha del borrado o sólo desplazarse los impares. En el primer caso, deberá decrementarse el valor de `i`, en el segundo el valor de `i` se mantiene.

    ```java
    public void eliminar(Integer valor) {
        int a = 0;
        int z = i;

        if (valor % 2 == 0) {
            a = i;
            z = this.array.length;
        }

        int izquierda = this.posicion(valor, a, z);
        if (izquierda >= z || this.array[izquierda] != valor) {
            return;
        }

        int derecha = izquierda + 1;
        while (derecha < z && valor == this.array[derecha]) {
            derecha++;
        }

        while (derecha < z) {
            this.array[izquierda++] = this.array[derecha++];
        }
    }
    ```

