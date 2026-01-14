---
id: ex-2016-01
year: 2016
exam: extraordinario
tags:
 - complejidad
---

Queremos programar una clase Conjunto usando internamente una tabla hash con lista de desbordamiento. Se pide programar los siguientes métodos:

```java
void add(Object x)
```

```java
boolean contains(Object x)
```

```java
void remove(Object x)
```

Razone la complejidad de dichos métodos.

No se aceptará como solución recurrir a la clase Map o a la clase Set de la biblioteca de java.

- (a) (2,1 puntos) Escribir el código de los métodos mencionados.

??? note "Mostrar solución"
    ```java
    public class Conjunto {
        private List<Object>[] tabla;

        public Conjunto(int size) {
            tabla = new List[size];
        }

        public void add(Object x) {
            int h = hash(x);
            if (tabla[h] == null)
                tabla[h] = new ArrayList<Object>();
            if (!tabla[h].contains(x))
                tabla[h].add(x);
        }

        public void remove(Object x) {
            int h = hash(x);
            if (tabla[h] == null)
                return;
            tabla[h].remove(x);
        }

        public boolean contains(Object x) {
            int h = hash(x);
            if (tabla[h] == null)
                return false;
            return tabla[h].contains(x);
        }

        private int hash(Object x) {
            return Math.abs(x.hashCode() % tabla.length);
        }
    }
    ```

- (b) (1,4 puntos) Razonar la complejidad de los métodos.

??? note "Mostrar solución"
    La complejidad de add() es O(1) sobre el supuesto de que la tabla de direccionamiento está dimensionada holgadamente; si no, sería la complejidad de la lista de desbordamiento.

    La complejidad de remove() y contains() es la misma.
