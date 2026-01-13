---
id: ex-2015-05
year: 2015
exam: extraordinario
tags:
 - android
---

- (a) (2 puntos) El proyecto 2 se basa en una adaptación del proyecto 1. Seleccione la respuesta o respuestas correctas en la hoja de respuestas. Las respuestas incorrectas restan.
    - 1. La clase Terreno se adapta al ciclo de vida de Android
        - I. No sería imprescindible realizar esta adaptación; simplemente la aplicación seguiría usando recursos cuando no está en primer plano.
        - II. Si no hacemos la adaptación, tendremos interbloqueos.
        - III. Los móviles se congelan en onPause() y se descongelan en onResume().
        - IV. Los móviles se resucitan en onCreate()
    - 2. Las clases que extienden Movil (p.ej. Jugador, Estatua, Depredador, …)
        - I. Deben implementar restart() porque es un método abstracto en Movil
        - II. Si además implementan Runnable, deben crear en restart() una hebra (new Thread()) y llamar a start() en la hebra creada
        - III. Si ademá s implementan Runnable, deben crear en pause() una hebra (new Thread()) y llamar a pause() en la hebra creada
        - IV. Siempre que extienden Movil deben implementar Runnable

??? note "Mostrar solución"
    - En 1 la opción correcta es III.

    - En 2 las opciones correctas son III y IV.

- (b) (3 puntos) Deseamos simplificar el comportamiento que hemos implementado el proyecto 2 para mover con el dedo el jugador. El nuevo comportamiento consiste en que si pulsamos en la casilla donde está el jugador, lanza un popup. Si pulsamos en una casilla diferente, el jugador se mueve en la dirección en la que está dicha casilla respecto del jugador.

Además, queremos poner una traza de error si se pulsa fuera del tablero.

Suponga que dispone del método popup para lanzar el popup como en la práctica, así como el resto de métodos de las clases.

??? note "Mostrar solución"
    ```java
    @Override
    public boolean onTouch(View view, MotionEvent event) {
        try {
            Movil jugador = terreno.getJugador();
            if (jugador == null) {
                return false;
            }

            if (event.getAction() == MotionEvent.ACTION_DOWN) {
                int x1 = (int) (event.getX() / lado1);
                int y1 = terreno.getN() - 1 - (int) (event.getY() / lado1);

                Casilla casilla = terreno.getCasilla(x1, y1);
                Casilla casillaJugador = jugador.getCasilla();

                if (casillaJugador.equals(casilla)) {
                    popup(casilla);
                } else {
                    int dx = (int) (x1 - casillaJugador.getX());
                    int dy = (int) (y1 - casillaJugador.getY());
                    Direccion direccion = null;

                    if (dy > 0)
                        direccion = Direccion.NORTE;
                    else if (dy < 0)
                        direccion = Direccion.SUR;
                    else if (dx > 0)
                        direccion = Direccion.ESTE;
                    else if (dx < 0)
                        direccion = Direccion.OESTE;

                    if (direccion != null) {
                        terreno.move(jugador, direccion);
                    }
                }
            }
        } catch (Exception e) {
            Log.e(TAG, "Ha pulsado fuera del tablero");
        }
        return false;
    }
    ```