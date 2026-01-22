---
id: ex-2018-02
year: 2018
exam: parcial 1 recuperacion
tags:
 - grafos
---

Se dispone de la clase Graph, con los métodos que se indican a continuación:
```java
public void addNode(Node)
public vois addLink(Link)
public void addLink2D(String, String, int)
public List<Node> getNodes()
public Node getNode(String)
public List<Link> getLinks()
public List<Link> getLinks(Node)
public Link getLink(Node, Node)
public int getWeight(List<Node>)
```

Un algoritmo alternativo a BFS y Dijkstra para recorrer un grafo es el algoritmo DFS (Depth First Search). El recorrido en profundidad se produce de tal forma que partiendo de un nodo se procesa el primero de los nodos alcanzables desde él mediante un Link, después el segundo y así sucesivamente todos los nodos que se pueden alcanzar con un solo Link. Para procesar cada uno de los nodos se utiliza el mismo procedimiento, siempre teniendo en cuenta que, al ser un grafo, no pasemos dos veces por el mismo nodo. En definitiva, se trata del recorrido en pre-orden usado para los árboles binarios BST.

Se muestra a continuación un ejemplo del orden de recorrido de DFS sobre un árbol para ver si desde el nodo “A” se puede alcanzar el nodo destino “J”:

![](./p1r/p1r_ex02.png)

Una de las formas de implementar DFS en un grafo es mediante un método recursivo, cuyo seudocódigo se proporciona a continuación:

```
1 método DFS(origen):
2   marcamos origen como visitado
3   para cada vértice v adyacente a origen en el Grafo:
4     si v no ha sido visitado:
5       marcamos como visitado v
6       llamamos recursivamente DFS(v)
```

- (a) (5 puntos) Codificar el algoritmo ListaNodos que devuelve todos los nodos alcanzables desde un determinado nodo src. Los nodos alcanzables desde un nodo son todos aquellos a los que se puede llegar desde ese nodo siguiendo una secuencia de enlaces (Link) definidos en el grafo. En el caso del grafo del ejemplo anterior, desde el nodo C serían alcanzables: <C,E,I,J,F,K,L> y desde el nodo D: <D, G, H>. Tenga en cuenta que en un caso real pudiera haber bucles al tratarse de un grafo. Se valorará con 2 puntos el uso de la clase Set para aumentar la velocidad del método ListaNodos, si además se justifica adecuadamente la mejora producida por su utilización.

??? note "Mostrar solución"
    ```java
    private List<Node> getNodesRec (Node src) {
        // Creamos las variables necesaria
        Set<Node> visited = new HashSet <Node>();

        // Si el nodo no ha sido visitado, lo marcamos como visitado, lo añadimos a la lista
        List <Node> list = new ArrayList <Node>();
        visited.add(src);
        list.add(src);

        // Llamada al método recursivo
        List<Node> alcanzables = getNodesRec (src, visited);
        list.addAll(alcanzables);

        return list;
    }

    private List<Node> getNodesRec (Node src, Set<Node> visited) {
        List <Node> list = new ArrayList <Node>();

        // Pasamos a recorrer los nodos desde los que se puede llegar con un Link desde este nodo
        for (Link link : graph.getLinks(src)) {
            Node next = graph.getNode(link.getDst());

            // Si el nodo ya ha sido visitado no hacemos nada
            if (visited.contains(next))
                continue;

            // Si el nodo no ha sido visitado, lo marcamos como visitado, lo añadimos a la lista
            visited.add(next);
            list.add(next);

            List <Node> res = getNodesRec(next, visited);

            // Añadimos a la lista de nodos alcanzables los nodos que devuelve getNodesRec al recorrer el nodo next
            list.addAll(res);
        }

        return list;
    }
    ```

    El uso de Set para controlar la lista de visitados permite mejorar el algoritmo frente a List, ya que la búsqueda en listas no
    está tan optimizada como en Set.

