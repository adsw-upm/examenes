---
id: ex-2022-01
year: 2022
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Utilizando el modelo de datos de la práctica 2 donde un vértice representaba un actor y una arista representa la película en la que han colaborado ambos actores. Se disponen las clases GraphLoader, Movie y DijkstraSP que podemos utilizar para resolver el problema. Y en el campo EdgeWeightedDigraph g de la clase GraphLoader tenemos ya cargado el grafo de actores y películas. Según el siguiente diagrama de clases:

![](./p1r/p1r_ex01.png)

### Class EdgeWeightedDigraph

| Tipo                   | Método                    | Descripción                                                   |
| ---------------------- | ------------------------- | ------------------------------------------------------------- |
| void                   | `addEdge(DirectedEdge e)` | Adds the directed edge to this edge-weighted digraph.         |
| Iterable<DirectedEdge> | `adj(int v)`              | Returns the directed edges incident from vertex v.            |
| int                    | `E()`                     | Returns the number of edges in this edge-weighted digraph.    |
| Iterable<DirectedEdge> | `edges()`                 | Returns all directed edges in this edge-weighted digraph.     |
| int                    | `V()`                     | Returns the number of vertices in this edge-weighted digraph. |

---

### Class DijkstraSP

| Constructor                                | Descripción                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `DijkstraSP(EdgeWeightedDigraph G, int s)` | Computes a shortest-paths tree from the source vertex s to every other vertex in the edge-weighted digraph G. |

| Tipo                   | Método          | Descripción                                                                 |
| ---------------------- | --------------- | --------------------------------------------------------------------------- |
| double                 | `distTo(int v)` | Returns the length of a shortest path from the source vertex s to vertex v. |
| Iterable<DirectedEdge> | `pathTo(int v)` | Returns a shortest path from the source vertex s to vertex v.               |

---

### Class DirectedEdge 

| Tipo   | Método     | Descripción                                   |
| ------ | ---------- | --------------------------------------------- |
| int    | `from()`   | Returns the tail vertex of the directed edge. |
| int    | `to()`     | Returns the head vertex of the directed edge. |
| double | `weight()` | Returns the weight of the directed edge.      |


Se pide:
- (a) (1 punto) Desarrolle el método obtenerIndiceMayor: Recibe un array de enteros y devuelve un int con el índice de la posición con el valor mayor. En caso de empate, se puede devolver cualquiera de los n índices que empatan: public int obtenerIndiceMayor(int[] array)

??? note "Mostrar solución"
    ```java
    public int obtenerIndiceMayor(int[] array) {
        if (array == null || array.length == 0)
            return -1; // null or empty

        int largest = 0;
        for (int i = 1; i < array.length; i++) {
            if (array[i] > array[largest])
                largest = i;
        }

        return largest; // position of the first largest found
    }
    ```


- (b) (2 punto) El algoritmo Dijkstra calcula el árbol de caminos más cortos desde un nodo. El constructor calcula este algoritmo y proporciona un método (pathTo) para obtener el camino mínimo desde el origen. Se pide desarrollar el método actorCentralDesdeOrigen que retorna un array, cuyo tamaño es el número de vértices (en el grafo) y sus valores son el número de veces que aparece el vértice en cualquier camino: public int[] actorCentralDesdeOrigen(int origen)

??? note "Mostrar solución"
    ```java
    public int[] actorCentralDesdeOrigen(int origen) {
        int[] btw = new int[this.g.V()];

        for (int destino = origen + 1; destino < this.g.V(); destino++) {
            if ((origen != destino) && (g.pathTo(destino) != null)) {
                for (DirectedEdge e : g.pathTo(destino)) {
                    if (e.to() != destino)
                        btw[e.to()]++;
                }
            }
        }

        return btw;
    }
    ```


- (c) (2 punto) Desarrolle el método que retorne el actor más central del grafo. Para ello, hay que calcular el actor más central entre los árboles de caminos de los vértices del grafo: public String actorCentral()

??? note "Mostrar solución"
    ```java
    public String actorCentral() {
        int[] btw = new int[this.g.V()];

        for (int origen = 0; origen < this.g.V(); origen++) {
            DijkstraSP d = new DijkstraSP(this.g, origen);
            int[] aux = this.actorCentralDesdeOrigen(origen);

            for (int i = 0; i < this.g.V(); i++) { // corregido inicialización de i
                btw[i] += aux[i];
            }
        }

        int actor = obtenerIndiceMayor(btw);
        Map<Integer, String> actorsMapInverted = this.getActorsMapInverted();
        return actorsMapInverted.get(actor);
    }
    ```

Nota: es muy aconsejable desarrollar estos métodos en el mismo orden y desarrollar el tercer método usando los
dos anteriores.