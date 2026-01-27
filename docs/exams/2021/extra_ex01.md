---
id: ex-2021-01
year: 2021
exam: extraordinario
tags:
 - grafos
---

Un sistema real se describe como un grafo no dirigido. Los arcos o aristas (edge) tienen un coste o peso mayor que cero. Un camino es una secuencia de arcos que conectan dos nodos o vértices. Un camino se representa mediante una lista (List<Edge>). En este sistema, interesa agrupar a todos los posibles caminos entre dos nodos concretos, que se representa mediante una lista de caminos (List<List<Edge>>).

Se pide desarrollar dos métodos, descritos en el cuadro adjunto:

- (a) (2 puntos) menorCamino selecciona el camino mínimo (el de menor coste total) de una lista de caminos. Se aconseja (no obligatorio) desarrollar un método que reciba como entrada un camino y retorne el peso total del camino.

- (b) (3 puntos) numeroVecesUsadoArco: genera un diccionario (Map<Edge, Integer>) con el número de veces que aparece cada arco en la lista de caminos del parámetro de entrada.

![](./extra/placeholder.jpg)

Nota: En la implementación de estos métodos, se gestionan listas de arcos. No es necesario conocer, ni gestionar los vértices conectados en los caminos incluidos en la lista de entrada.

??? note "Mostrar solución"
    ```java
    private double pesoCamino(List<Edge> camino) {
        double distancia = 0;
        for (Edge arco : camino) {
            distancia = distancia + arco.weight();
        }
        return distancia;
    }

    /**
     * Seleccionar el camino con el menor coste total.
     * @param listaCaminos una lista de caminos del grafo del sistema entre dos vértices.
     * @return La respuesta es un camino que sea el mínimo de la lista recibida.
     * Si hubieran varios caminos mínimos con el mismo coste, se puede retornar
     * cualquiera de ellos.
     */
    public List<Edge> menorCamino(List<List<Edge>> listaCaminos) {
        List<Edge> menorCamino = null;
        double menorPeso = Double.MAX_VALUE;

        for (List<Edge> camino : listaCaminos) {
            double aux = pesoCamino(camino);
            if (menorCamino == null || aux < menorPeso) {
                menorPeso = aux;
                menorCamino = camino;
            }
        }
        return menorCamino;
    }

    /**
     * Determinar cuántas veces aparece cada arco en una lista de caminos
     * @param listaCaminos una lista de caminos del grafo del sistema entre dos vértices.
     * @return devuelve un diccionario, en el que la clave es un arco y el valor un
     * entero que representa el número de veces que el arco aparece en el parámetro de entrada.
     */
    public Map<Edge, Integer> numeroVecesUsadoArco(List<List<Edge>> listaCaminos) {
        // Diccionario
        Map<Edge, Integer> diccionario = new HashMap<Edge, Integer>();

        for (List<Edge> camino : listaCaminos) {
            for (Edge arco : camino) {
                if (diccionario.containsKey(arco)) {
                    int aux = diccionario.get(arco) + 1;
                    diccionario.put(arco, aux);
                } else {
                    diccionario.put(arco, 1);
                }
            }
        }
        return diccionario;
    }
    ```
