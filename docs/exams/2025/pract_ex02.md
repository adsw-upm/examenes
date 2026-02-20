---
id: ex-2025-02
year: 2025
exam: extraordinario
tags:
 - complejidad
---

- (a) (5 puntos) Desarrollar el método `public Tablero[] movimientoMasRepetido()` que devuelve un array con los dos tableros que representan el movimiento más repetido en el grafo.

??? note "Mostrar solución"
    ```java
    public Tablero[] movimientoMasRepetido() {
      Enlace maxEnlace = null;
      for (Enlace enlace : this.enlaces) {
        if (maxEnlace == null || enlace.getPeso() > maxEnlace.getPeso()) {
          maxEnlace = enlace;
        }
      }
      return new Tablero[] {maxEnlace.getOrigen().getTablero(),
                           maxEnlace.getDestino().getTablero()};
    }
    ```


- (b) (5 puntos) Desarrolle un método que reciba como parámetro dos tableros y calcule el camino de longitud impar más corto, entre ellos. El método debe devolver una secuencia de `Nodo` que represente el camino encontrado. Tenga en cuenta que si no existe un camino entre los dos tableros, el método debe devolver `null`. Si hay varios caminos de la misma longitud, devolverá el primero que se encuentre.

??? note "Mostrar solución"
    Usamos el mismo algoritmo que hayamos implementado en la práctica 2. Solo se debe añadir la condición de longitud impar para considerar un camino válido

    Si es BFS, basta con añadir una condición que compruebe si la longitud del camino es impar antes de devolver el camino encontrado. Si es Dijkstra, se debe modificar la lógica del método relax para que solo actualice la distancia al destino si la longitud del camino es impar.
