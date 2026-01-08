---
id: ex-2013-02
year: 2013
exam: parcial 1 recuperacion
tags:
 - monitores
---

- (a) (5 puntos) Desarrolle un monitor en Java que gestione el despegue de aviones y avionetas en un aeropuerto como se especifica a continuación:

Los aviones, al despegar, generan turbulencias, por lo que entre dos despegues consecutivos debe transcurrir un intervalo mínimo de tiempo:

* 3 minutos después del despegue de un avión.
* 2 minutos después del despegue de una avioneta.

Además se debe impedir que despeguen consecutivamente dos avionetas si hay aviones esperando. No hay restricciones de este tipo respecto a los aviones (pueden despegar consecutivamente).

El monitor responde al siguiente esquema:

```java
class GestorDespegue {
    ...
    
    // Lo invoca un avión cuando quiere despegar
    ... despegarAvion() {...}
    
    // Lo invoca una avioneta cuando quiere despegar
    ... despegarAvioneta() {...}
    
    // Lo invoca el temporizador para indicar que
    // ha transcurrido el intervalo mínimo desde
    // el despegue anterior
    ... autorizarDespegue() {...}
    ...
}
```

Para gestionar el intervalo de tiempo entre despegues, se dispone de una clase `Temporizador`, cuya interfaz se muestra a continuación. El método `iniciarTemporizador` arranca un temporizador que deja pasar un cierto tiempo. Cuando el tiempo expira, se invoca el método `autorizarDespegue` del objeto `GestorDespegue` que se pasa en el constructor. No es necesario desarrollar esta clase.

```java
public class Temporizador {
    public Temporizador(GestorDespegue gestor) { ... }
    public void iniciarTemporizador(int minutos) { ... }
}
```

??? note "Mostrar solución"
    Una solución posible al problema del monitor de gestión de despegues es la siguiente:

    ```java
    public class GestorDespegue {

        private boolean pistaOcupada = true;
        private int nAvionesEsperando = 0;

        private final int tiempoAvion = 3;
        private final int tiempoAvioneta = 2;

        private boolean anteriorAvioneta = false;

        private Temporizador unTemporizador = new Temporizador(this);

        // Invocado por un avión cuando quiere despegar
        public synchronized void despegarAvion() throws InterruptedException {
            nAvionesEsperando++;
            while (pistaOcupada)
                wait();

            nAvionesEsperando--;
            anteriorAvioneta = false;

            unTemporizador.iniciarTemporizador(tiempoAvion);
            pistaOcupada = true;
        }

        // Invocado por una avioneta cuando quiere despegar
        public synchronized void despegarAvioneta() throws InterruptedException {
            while (pistaOcupada || (nAvionesEsperando > 0 && anteriorAvioneta))
                wait();

            anteriorAvioneta = true;
            unTemporizador.iniciarTemporizador(tiempoAvioneta);
            pistaOcupada = true;
        }

        // Invocado por el temporizador cuando finaliza el intervalo mínimo
        public synchronized void finTemporizador() throws InterruptedException {
            pistaOcupada = false;
            notifyAll();
        }
    }
    ```
