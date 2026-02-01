---
id: ex-2025-03
year: 2025
exam: practicas
tags:
 - hebras
---

- (a) (6 puntos) Escriba las modificaciones necesarias en `AnalizadorConcurrente` para asegurar que nunca haya más más tareas pendientes (en la cola) que hebras procesadoras de tareas.

??? note "Mostrar solución"
    El método `addTarea` debe bloquear cuando haya demasiadas tareas en cola. Además, el método `getTarea` debe notificar cuando libera una tarea.

    ```java
    public synchronized void addTarea(TareaCamino tarea) {
      while(tareas.size() >= numHebras) {
        wait();
      }
      tareas.add(tarea);
      notifyAll();
    }

    public synchronized TareaCamino getTarea(HebraWorker hw) throws InterruptedException {
      while (tareas.isEmpty() && hw.keepWorking) {
        wait();
      }
      if (!hw.keepWorking) {
        return null;
      }
      Tarea t = tareas.remove(0);
      notifyAll();
      return t;
    }
    ```


- (b) (4 puntos) Explique con detalle cómo comprobaría que las modificaciones realizadas funcionan correctamente.

??? note "Mostrar solución"
    Realizaría una o varias pruebas unitarias, y/o un smoketest. El código tendría que implementar el caso que queremos probar: intentar añadir más tareas que hebras disponibles, y comprobar que realmente se bloquée la ejecución.

    Por ejemplo, se podrían añadir manualmente más tareas que `NUM_HEBRAS` a un pool de hebras. Las tareas podrían ser simples, como un tablero con jaque mate, para que no resulten en más tareas. La comprobación tendría que asegurar que se ha bloqueado la ejecución de `addTarea`.

    Una forma sencilla de hacer la comprobación sería añadir aserciones tras la línea en `addTarea` que añade la tarea a la cola: `assert tareas.size() <= NUM_HEBRAS`.

    Nota: en este caso el pool de hebras arranca las hebras procesadoras en el constructor, lo que implica que las hebras procesadoras estarán constantemente intentando consumir tareas. Debemos asegurar que se añaden suficientes tareas suficientemente rápido. Por ejemplo, añadiendo `10*NUM_HEBRAS` tareas en bucle.

    Otras formas incluyen:
    - Modificar el código en `addTarea` para mantener un contador de veces en que se ha bloqueado (antes del `.wait()`). Se puede comprobar este contador en la prueba.  (fácil)
    - Suspender manualmente las hebras proceadoras con `suspend` mientras se añaden las tareas. Para ello hace falta acceso a la lista de hebras. Una forma sería implementar los métodos `pararHebras` y `reanudarHebras` en `PoolHebras`. (medio)
    - Usar hebras que consuman tareas mucho más lentamente para poder medir los bloqueos con tiempo. Para ello, habría que permitir a `PoolHebras` utilizar hebras distintas de `HebraWorker`. Por ejemplo, pasando la clase como argumento al constructor. (difícil)
