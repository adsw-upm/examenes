---
id: ex-2014-02
year: 2014
exam: parcial 1 recuperacion
tags:
 - monitores
---

En un museo se exhibe un cortometraje de corta duración repetidamente, con un breve descanso entre proyecciones. La capacidad de la sala es de 50 personas. En el descanso, se vacía la sala y pueden entrar los visitantes que lo deseen, sin sobrepasar la capacidad de la sala. Una vez comenzada la proyección, no se permite el acceso a nuevos visitantes, que quedan esperando al siguiente descanso.

- (a) (5 puntos) Escriba una clase Monitor que controle el acceso a la sala. Cada visitante es modelado como una hebra, que invoca el método `accederASala()` del Monitor cuando desea ver la proyección. Además hay otra hebra, Proyector, que periódicamente invoca el método `comienzaProyección()` y, tras la finalización de la proyección, invoca el método `terminaProyección()`.

El monitor debe permitir acceso a la Sala a las hebras `Visitante` siempre que:
    
    * No se sobrepase la capacidad de la sala;
    
    * No haya comenzado la proyección.

Cuando la proyección termine, se debe permitir que los visitantes que estaban esperando accedan a la sala. Se entiende que TODOS los asistentes a una proyección salen de la sala al terminar la proyección.

SE PIDE EXCLUSIVAMENTE EL CÓDIGO DEL MONITOR. NO ESCRIBA EL CÓDIGO DE VISITANTE.

A continuación se incluye el código del Proyector:

```java
public class Proyector extends Thread
{
    private final Monitor monitor;
    private final int duracionProyeccion = 15000;
    private final int duracionDescanso = 5000;

    Proyector (Monitor monitor) {
        this.monitor = monitor;
        this.start();
    }

    @Override
    public void run() {
        while (true) {
            try {
                sleep(duracionDescanso);
                monitor.comienzaProyeccion();
                sleep(duracionProyeccion);
                monitor.terminaProyeccion();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

??? note "Mostrar solución"
    ```java
    private int N= 10;
    private int numVisitantes;
    private boolean proyectando;

    Monitor() {
        numVisitantes= 0;
        proyectando= false;
    }

    public synchronized void comienzaProyeccion() {
        proyectando= true;
    }

    public synchronized void terminaProyeccion() {
        proyectando= false;
        numVisitantes= 0;
        notifyAll();
    }

    public synchronized void accederASala() {
        while ( proyectando || numVisitantes >= N)
        {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }
        numVisitantes++;
    }
    ```
