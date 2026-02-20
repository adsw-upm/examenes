---
id: ex-2025-05
year: 2025
exam: extraordinario
tags:
 - complejidad
---

- (a) (6 puntos) Desarrolle un método que permita saber cual es la pieza (el tipo de pieza) que se usa en el movimiento más utilizado como apertura de las blancas (primera pieza que mueven) en el conjunto de partidas cargadas. De la misma manera, desarrolle un método que permita saber cual es el movimiento más utilizado como apertura de las negras (primera pieza que mueven) en contestación a la apertura de las blancas más utilizada. Consejo: piense qué piezas se pueden mover al inicio de una partida de ajedrez.

??? note "Mostrar solución"
    Métodos a incluir en la clase `AnalizadorGrafos`:

    ```java
    public TipoPieza getAperturaBlancas() {
      Nodo nodoBasico = nodos.get(Tablero.getTableroBasico());
      Enlace enlaceMayorPeso = obtenerEnlaceMayorPeso(nodoBasico);
      Tablero destino = enlaceMayorPeso.getDestino().getTablero();
      return detectarTipoPiezaMovida(destino, 7); // Fila 7 para peones blancos
    }

    public TipoPieza getAperturaNegras() {
      Nodo nodoBasico = nodos.get(Tablero.getTableroBasico());
      Enlace primerEnlace = obtenerEnlaceMayorPeso(nodoBasico);
      Nodo nodoDestino = primerEnlace.getDestino();
      Enlace segundoEnlace = obtenerEnlaceMayorPeso(nodoDestino);
      Tablero destino = segundoEnlace.getDestino().getTablero();
      return detectarTipoPiezaMovida(destino, 2); // Fila 2 para peones negros
    }

    private Enlace obtenerEnlaceMayorPeso(Nodo nodo) {
      Enlace enlaceMayorPeso = null;
      for (Enlace enlace : nodo.getEnlaces()) {
        if (enlaceMayorPeso == null || enlace.getPeso() > enlaceMayorPeso.getPeso()) {
          enlaceMayorPeso = enlace;
        }
      }
      return enlaceMayorPeso;
    }

    private TipoPieza detectarTipoPiezaMovida(Tablero tablero, int fila) {
      Pieza matriz[][] = tablero.getMatrizPiezas();
      for (int col = 0; col < 8; col++) {
        Pieza pieza = matriz[fila][col];
        if (pieza == null) {
          return TipoPieza.PEON; // Si falta algun peón, se habrá movido
        }
      }
      return TipoPieza.CABALLO; // Si están todos, será un caballo
    }
    ```
