---
id: ex-2013-02
year: 2013
exam: extraordinario
tags:
    - monitores
---

- (a) (3 puntos) Escriba un monitor en Java que controle el acceso a un parking de coches. El parking tiene un número de plazas N y dispone de dos accesos, Este y Oeste.

Si el parking no está lleno, se admiten entradas por ambos accesos libremente. Si el parking está lleno, los coches deben esperar a que haya plazas disponibles. Cuando queda una plaza libre, el monitor debe alternar los accesos de entrada entre Este y Oeste. Cuando un coche abandona el parking, se considera irrelevante el acceso que usa para salir.

El esqueleto del monitor con los nombres de los métodos es el siguiente:

```java
class Monitor {
    ...
    Monitor(int numPlazas) { ... }
    ...
    entraCochePorEste(...) { ... }
    ...
    entraCochePorOeste(...) { ... }
    ...
    saleCoche(...) { ... }
}
```

??? note "Mostrar solución"
    Una solución correcta es:
    ```java
    public class Monitor {

        private int numPlazas, numCoches;
        private boolean turnoEste, turnoOeste;
        private int esperaEnEste, esperaEnOeste;

        public Monitor(int numPlazas) {
            this.numPlazas = numPlazas;
            numCoches = 0;
            turnoEste = turnoOeste = true;
            esperaEnEste = esperaEnOeste = 0;
        }

        public synchronized void entraCochePorEste() throws InterruptedException {
            esperaEnEste++;
            while ((numCoches >= numPlazas) || (turnoOeste && (esperaEnOeste > 0))) {
                wait();
            }
            esperaEnEste--;
            numCoches++;
            if (numCoches == numPlazas) {
                turnoEste = false;
                turnoOeste = true;
            }
        }

        public synchronized void entraCochePorOeste() throws InterruptedException {
            esperaEnOeste++;
            while ((numCoches >= numPlazas) || (turnoEste && (esperaEnEste > 0))) {
                wait();
            }
            esperaEnOeste--;
            numCoches++;
            if (numCoches == numPlazas) {
                turnoEste = true;
                turnoOeste = false;
            }
        }

        public synchronized void saleCoche() {
            numCoches--;
            notifyAll();
        }
    }
    ```
