---
id: ex-2022-02
year: 2022
exam: extraordinario
tags:
 - complejidad
---

Se dispone de una clase RedSocial que representa una red social de amistad entre personas. En concreto, se quiere representar la relación “seguir a una persona”. Para ello, se utiliza un grafo (g) dirigido para representar esta relación: un vértice (nodo) representa una persona y un arco (arista) una relación. En concreto A à B representa que la persona A siga a la persona B. Este arco no implica que B sigua a A.

En la clase RedSocial se utiliza un mapa (Map<Integer, String> mapaPersonas) que permite obtener el nombre de la persona de un vértice. El arco que representa la relación “seguir a una persona” se modelará en un objeto de la clase DirectedEdge, con peso 1. La clase RedSocial se describa en el diagrama de clases adjuntado.

En el sistema, se disponen las clases DijkstraSP, EdgeWeightedDigraph y DirectedEdge, para modelar el
sistema. 

![](./extra/extra_ex02.png)

- (a) (1 punto) Desarrolle el método public double getMediaSeguidores(), que devuelve el número medio de seguidores en el grafo. 

??? note "Mostrar solución"
    ```java
    public double getMediaSeguidores() {
        return (double) this.g.E()/this.g.V();
    }
    ```


- (b) (1,5 puntos) Desarrolle el método public String getVerticeMasSeguidores(), que devuelve el nombre de la persona que tiene más seguidores.

??? note "Mostrar solución"
    ```java
    public String getVerticeMasSeguidores() {
        int maxSeguidores = 0;
        int vertice = 0;

        for (int v = 0; v < this.g.V(); v++) {
            if (this.g.indegree(v) > maxSeguidores) {
                maxSeguidores = this.g.indegree(v);
                vertice = v;
            }
        }

        return this.mapaPersonas.get(vertice);
    }
    ```


- (c) (2,5 putnos) Desarrolle el método public List<String> getListaMinimoAmigosComun(int verticeOrigen, int verticeDestino), que recibe por parámetro un vértice de origen y un vértice de destino y debe devolver una lista de String con el nombre de las personas de la cadena mínima de amistad entre el origen y el destino. Nota: ni el nombre de la persona origen ni destino deberán aparecer en la lista.

??? note "Mostrar solución"
    ```java
    public List<String> getListaMinimoAmigosComun(int verticeOrigen, int verticeDestino) {
        List<String> amigos = new ArrayList<String>();
        DijkstraSP d = new DijkstraSP(this.g, verticeOrigen);
    
        if (d.pathTo(verticeDestino) != null) {
            for (DirectedEdge e : d.pathTo(verticeDestino)) {
                if (e.from() != verticeOrigen)
                    amigos.add(this.mapaPersonas.get(e.from()));
            }
        } else {
            return null;
        }
    
        return amigos;
    }
    ```